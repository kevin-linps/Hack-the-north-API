import Customer
import requests
import json

## read in API Key from a text file
file1 = open("ApiKey.txt", "r")
key = file1.readline()
file1.close()

## retrieve 1000 customer IDs
response = requests.post('https://api.td-davinci.com/api/raw-customer-data',
    headers = { 'Authorization': key })
response_data = response.json()

## store the IDs into text files
file2 = open("CustomerId.txt", "w")
for i in range(len(response_data["result"]["customers"])):
    file2.write(response_data["result"]["customers"][i]["id"])
    file2.write("\n")
file2.close()

file3 = open("CustomerId.txt", "r")
Ids = file3.readlines()
file3.close()

Ids[-1] += "/n"

n = 0

coordinates = {}

for i in range(int(len(Ids)/5)):
    Ids[i] = Ids[i][:-1]
    c = Customer.Customer(Ids[i], key, True)

    for j in range(len(c.transactions)):

        if c.transactions[j].latitude != 0 and c.transactions[j].longitude != 0:
            coor = {}
            coor["longitude"] = c.transactions[j].longitude
            coor["latitude"] = c.transactions[j].latitude
            coordinates[str(n)] = coor
            n = n + 1

file3 = open("Coordinates.txt", "w")    
jstr = json.dump(coordinates, file3)
file3.close()
print(n, "done")
