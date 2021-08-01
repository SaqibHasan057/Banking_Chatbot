
import requests 
  
# api-endpoint 
URL = "http://localhost:8000/localDatabase/creditCardInquiry"
  
# location given here 
accountNumber = "1000100010001111"
a2 = "100010011112"
amount = 5000
PIN = 1342
  
# defining a params dict for the parameters to be sent to the API 
DATA = {'creditCardNumber':accountNumber,'toAccountNumber':a2, 'amount':amount,'PIN':PIN} 
  
# sending get request and saving the response as response object 
r = requests.post(url = URL, data = DATA) 
  
# extracting data in json format 
data = r.json() 
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
balance = data['result']
  
# printing the output 
print("Transaction Success:",balance) 


"""
from random import randint

for i in range(0,20):
	x=randint(1000000000000000, 9999999999999999)
	print("- ["+str(x)+"](creditCardNumber)")

"""