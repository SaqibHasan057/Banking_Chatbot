import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Transaction, CreditCard
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the local database index.")

@csrf_exempt
def balanceInquiry(request):
	accountNumber = request.POST['accountNumber']
	PIN = request.POST['PIN']


	valueSet = Account.objects.filter(accountNumber=accountNumber)
	response_data = {}

	if len(valueSet)>0:
		if (valueSet[0].PIN == PIN):
			response_data['result'] = valueSet[0].balance
			print(response_data)
		else:
			response_data['result'] = "!"
	else:
		response_data['result'] = "!"

	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def creditCardInquiry(request):
	creditCardNumber = request.POST['creditCardNumber']
	PIN = request.POST['PIN']

	valueSet = CreditCard.objects.filter(creditCardNumber=creditCardNumber)
	response_data = {}

	if len(valueSet)>0:
		if (valueSet[0].PIN == PIN):
			response_data['result'] = valueSet[0].balance
			print(response_data)
		else:
			response_data['result'] = "!"
	else:
		response_data['result'] = "!"

	return HttpResponse(json.dumps(response_data), content_type="application/json")



@csrf_exempt
def lastTransaction(request):
	accountNumber = request.POST['accountNumber']
	PIN = request.POST['PIN']

	valueSet = Account.objects.filter(accountNumber=accountNumber)
	response_data = {}

	if len(valueSet)>0:
		if (valueSet[0].PIN == PIN):
			transactionSet = Transaction.objects.filter(Q(fromAccountNumber=accountNumber) | Q(toAccountNumber=accountNumber)).order_by('dateTime').reverse()
			if len(transactionSet)>0:
				response_data['result'] = [transactionSet[0].fromAccountNumber.accountNumber,transactionSet[0].toAccountNumber.accountNumber,transactionSet[0].amount,transactionSet[0].dateTime.strftime("%d-%b-%Y (%I:%M %p)")]
			else:
				response_data['result'] = "!"
		else:
			response_data['result'] = "!"
	else:
		response_data['result'] = "!"

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def sendMoney(request):
	fromAccountNumber = request.POST['fromAccountNumber']
	toAccountNumber = request.POST['toAccountNumber']
	amount = float(request.POST['amount'])
	PIN = request.POST['PIN']

	valueSet = Account.objects.filter(accountNumber=fromAccountNumber)
	tempAccount = Account.objects.filter(accountNumber=toAccountNumber)
	response_data = {}

	if len(valueSet)>0 and len(tempAccount)>0:
		if (valueSet[0].PIN == PIN and valueSet[0].balance>=amount):
			tempTransaction = Transaction(fromAccountNumber=valueSet[0],toAccountNumber=tempAccount[0],amount=amount,dateTime=datetime.datetime.now())
			tempTransaction.save()

			valueSet[0].balance-=amount
			valueSet[0].save()

			tempAccount[0].balance+=amount
			tempAccount[0].save()

			response_data['result'] = '1'
		else:
			response_data['result'] = "!"
	else:
		response_data['result'] = "!"

	return HttpResponse(json.dumps(response_data), content_type="application/json")


