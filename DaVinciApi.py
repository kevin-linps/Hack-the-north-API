import Customer

## read in API Key from a text file
file1 = open("ApiKey.txt", "r")
key = file1.readline()
file1.close()

## read in customer ID
file2 = open("CustomerId.txt", "r")
Id = file2.readline()
file2.close()       

c = Customer.Customer(Id, key)
