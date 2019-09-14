import requests
import json
import Account
import Transaction

class Customer:

    def __init__(self, ID, ApiKey): 

        self.ID = ID
        self.key = ApiKey
        self.getPersonalInfo()
        self.getAccounts()
        self.getTransactions()
        

    def getPersonalInfo(self):

        ## obtain customer personal information from the API
        response = requests.get('https://api.td-davinci.com/api/customers/' + self.ID,
                                headers = { 'Authorization': self.key })
        data = response.json()

        ## class variables storing personal info
        self.name = data["result"]["givenName"] + " " + data["result"]["surname"]
        self.age  = data["result"]["age"]
        self.bday = data["result"]["birthDate"]
        self.income = data["result"]["totalIncome"]
        self.workType   = data["result"]["workActivity"]
        self.occupation = data["result"]["occupationIndustry"]
        self.relationship = data["result"]["relationshipStatus"]

    def getAccounts(self):

        ## obtain customer account information from the API
        response = requests.get('https://api.td-davinci.com/api/customers/' + self.ID + "/accounts",
                                headers = { 'Authorization': self.key })
        data = response.json()
        
        self.bankAccts = [Account.BankAccount(data["result"]["bankAccounts"][i]) for i in range(len(data["result"]["bankAccounts"]))]        
        self.creditCardAccts = [Account.CreditCardAccount(data["result"]["creditCardAccounts"][i]) for i in range(len(data["result"]["creditCardAccounts"]))]

    def getTransactions(self):

        ## obtain customer account information from the API
        response = requests.get('https://api.td-davinci.com/api/customers/' + self.ID + "/transactions",
                                headers = { 'Authorization': self.key })
        data = response.json()

        self.transactions = []
        self.transfers = []
        for i in range(len(data["result"])):
            if data["result"][i]["categoryTags"][0] in ["Food and Dining", "Shopping"]:
                tr = Transaction.Transaction(data["result"][i])
                self.transactions.append(tr)
            else:
                tr = Transaction.Transfer(data["result"][i])
                self.transfers.append(tr)
