class BankAccount:

    def __init__(self, data): 

        self.branch  = data["branchNumber"]
        self.acctNum = data["maskedAccountNumber"]
        self.type    = data["type"]
        self.openDate = data["openDate"]
        self.balance  = data["balance"]
        self.currency = data["currency"]


class CreditCardAccount:

    def __init__(self, data): 

        self.type     = data["type"]
        self.acctNum  = data["card"]["maskedNumber"]
        self.securityCode = data["card"]["securityCode"]
        self.balance  = data["balance"]
        self.openDate = data["openDate"]
