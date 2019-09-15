import Customer

## read in API Key from a text file
file1 = open("ApiKey.txt", "r")
key = file1.readline()
file1.close()

## read in customer ID
file2 = open("CustomerId.txt", "r")
Ids = file2.readlines()
file2.close()

customers = [Customer.Customer(Ids[i], key, True) for i in range(len(Ids))]
