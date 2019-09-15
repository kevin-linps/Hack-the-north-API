class Transaction:

    def __init__(self, data, survey): 

        try:
            self.longitude  = data["locationLongitude"]
            self.latitude   = data["locationLatitude"]
        except:
            self.longitude  = 0
            self.latitude   = 0

        if survey == False:
            self.country    = data["locationCountry"]
            self.region     = data["locationRegion"]
            self.city       = data["locationCity"]
            self.postalCode = data["locationPostalCode"]
            self.street     = data["locationStreet"]
            self.description  = data["description"]
            self.merchantName = data["merchantName"]
            self.source = data["source"]
            self.type   = data["type"]

        self.amount = data["currencyAmount"]
        self.category = data["categoryTags"][0]
        self.date = data["originationDateTime"]




class Transfer:

    def __init__(self, data):

        self.description = data["description"]
        self.type = data["type"]
        self.amount = data["currencyAmount"]
        self.date = data["originationDateTime"]
