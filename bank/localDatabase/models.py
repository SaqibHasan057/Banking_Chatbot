from django.db import models

# Create your models here.
class Account(models.Model):
	#account number, account name, PIN, balance
	accountNumber = models.CharField(max_length=12,primary_key=True)
	accountName = models.CharField(max_length=500)
	PIN = models.CharField(max_length=4)
	balance = models.FloatField()

	def __str__(self):
		return self.accountNumber + " " + self.accountName + "\n"



class Transaction(models.Model):
	#from account number, to account number, amount, time and date of transaction
	fromAccountNumber = models.ForeignKey(Account, on_delete=models.CASCADE)
	toAccountNumber = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
	amount = models.FloatField()
	dateTime = models.DateTimeField()

	def __str__(self):
		return self.fromAccountNumber.accountNumber + " " + self.toAccountNumber.accountNumber + " " + "\n"


class CreditCard(models.Model):
	#credit card number, account, PIN, balance

	creditCardNumber = models.CharField(max_length=16,primary_key=True)
	account = models.ForeignKey(Account,on_delete=models.CASCADE)
	PIN = models.CharField(max_length=4)
	balance = models.FloatField()

	def __str__(self):
		return self.creditCardNumber + "\n"