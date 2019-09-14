class Transaction:

    def __init__(self, data): 

        self.longitude  = data["locationLongitude"]
        self.latitude   = data["locationLatitude"]
        self.country    = data["locationCountry"]
        self.region     = data["locationRegion"]
        self.city       = data["locationCity"]
        self.postalCode = data["locationPostalCode"]
        self.street     = data["locationStreet"]

        self.amount = data["currencyAmount"]
        self.source = data["source"]
        self.type   = data["type"]
        self.category = data["categoryTags"][0]
        self.date = data["originationDateTime"]

        self.description  = data["description"]
        self.merchantName = data["merchantName"]


class Transfer:

    def __init__(self, data):

        self.description = data["description"]
        self.type = data["type"]
        self.amount = data["currencyAmount"]
        self.date = data["originationDateTime"]
