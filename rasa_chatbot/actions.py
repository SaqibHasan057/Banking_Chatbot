# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset
import requests 
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class balanceInquiryForm(FormAction):

	def name(self):
		return "balance_inquiry_form"

	@staticmethod
	def required_slots(tracker):
		return ["accountNumber","PIN",]

	def slot_mappings(self):
		return {
		"accountNumber": self.from_entity(entity="accountNumber"),
		"PIN": self.from_entity(entity="PIN"),
		}

	def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
		URL = "http://localhost:8000/localDatabase/balanceInquiry"

		accountNumber = tracker.get_slot("accountNumber")
		PIN = tracker.get_slot("PIN")
		
		DATA = {'accountNumber':accountNumber, 'PIN':PIN}
		r = requests.post(url = URL, data = DATA) 
		data = r.json() 

		balance = data['result']
		#print(balance)

		if(balance=='!'):
			dispatcher.utter_message("আপনি ভুল তথ্য দিয়েছেন। আবার চেষ্টা করুন।")
		else:
			dispatcher.utter_message("আপনার ব্যাল্যান্স হলো ৳"+str(balance))


		
		return [AllSlotsReset()]

class lastTransactionForm(FormAction):

	def name(self):
		return "last_transaction_form"

	@staticmethod
	def required_slots(tracker):
		return ["accountNumber","PIN",]


	def slot_mappings(self):
		return {
		"accountNumber": self.from_entity(entity="accountNumber"),
		"PIN": self.from_entity(entity="PIN"),
		}

	def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
		URL = "http://localhost:8000/localDatabase/lastTransaction"

		accountNumber = tracker.get_slot("accountNumber")
		PIN = tracker.get_slot("PIN")
		
		DATA = {'accountNumber':accountNumber, 'PIN':PIN}
		r = requests.post(url = URL, data = DATA) 
		data = r.json() 

		balance = data['result']
		#print(balance)

		if(balance=='!'):
			dispatcher.utter_message("আপনি ভুল তথ্য দিয়েছেন। আবার চেষ্টা করুন।")
		else:
			dispatcher.utter_message("আপনি শেষ " + balance[1] + " একাউন্টে ৳ " + str(balance[2]) + " পাঠিয়েছেন " + balance[3] + " তারিখ এবং ঘটিকায়।")


		return [AllSlotsReset()]


class sendMoney(FormAction):

	def name(self):
		return "send_money_form"

	@staticmethod
	def required_slots(tracker):
		return ["fromAccountNumber","toAccountNumber","amount","PIN",]


	def slot_mappings(self):
		return {
		"fromAccountNumber": self.from_entity(entity="accountNumber"),
		"toAccountNumber": self.from_entity(entity="accountNumber"),
		"amount": self.from_entity(entity="amount"),
		"PIN": self.from_entity(entity="PIN"),
		}

	def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
		URL = "http://localhost:8000/localDatabase/sendMoney"

		fromAccountNumber = tracker.get_slot("fromAccountNumber")
		toAccountNumber = tracker.get_slot("toAccountNumber")
		amount = tracker.get_slot("amount")
		PIN = tracker.get_slot("PIN")

		DATA = {'fromAccountNumber':fromAccountNumber,'toAccountNumber':toAccountNumber,'amount':amount,'PIN':PIN}
		r = requests.post(url=URL, data=DATA)
		data = r.json()

		balance = data['result']
		#print(balance)

		if(balance=='!'):
			dispatcher.utter_message("আপনি ভুল তথ্য দিয়েছেন। আবার চেষ্টা করুন।")
		else:
			dispatcher.utter_message("আপনার ট্রানসাকসান ঠিকমতো হয়েছে!")


		return [AllSlotsReset()]

class creditCardInquiryForm(FormAction):

	def name(self):
		return "credit_card_inquiry_form"

	@staticmethod
	def required_slots(tracker):
		return ["creditCardNumber","PIN",]

	def slot_mappings(self):
		return {
		"creditCardNumber": self.from_entity(entity="creditCardNumber"),
		"PIN": self.from_entity(entity="PIN"),
		}

	def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
		URL = "http://localhost:8000/localDatabase/creditCardInquiry"

		accountNumber = tracker.get_slot("creditCardNumber")
		PIN = tracker.get_slot("PIN")
		
		DATA = {'creditCardNumber':accountNumber, 'PIN':PIN}
		r = requests.post(url = URL, data = DATA) 
		data = r.json() 

		balance = data['result']
		#print(balance)

		if(balance=='!'):
			dispatcher.utter_message("আপনি ভুল তথ্য দিয়েছেন। আবার চেষ্টা করুন।")
		else:
			dispatcher.utter_message("আপনার ক্রেডিট কার্ড ব্যাল্যান্স হলো ৳"+str(balance))


		
		return [AllSlotsReset()]