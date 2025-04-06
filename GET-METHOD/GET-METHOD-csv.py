import requests
import csv
uri = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url=uri)
pydict = response.json()

filter_data1 = []
filter_dataall = []

if isinstance(pydict, list):
    print(" Response Data is a LIST")
    for data in pydict:
        if str(data["id"]).startswith("1"):
            filter_data1.append(data)
        else:
            filter_dataall.append(data)
elif isinstance(pydict, dict):
    print(" Response Data is a DICT")
    if str(pydict["id"]).startswith("1"):
        filter_data1.append(pydict)
    else:
        filter_dataall.append(pydict)

with open("NameEmail1.csv", "w", newline="") as csv_file:
    columns = ["id", "name", "email"]
    nonone = csv.DictWriter(csv_file, fieldnames=columns, extrasaction="ignore")
    nonone.writeheader()
    nonone.writerows(filter_data1)

with open("NameEmail.csv", "w", newline="") as csv_file:
    columns= ["id", "name", "email"]
    writer = csv.DictWriter(csv_file, fieldnames=columns, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(filter_dataall)

'''
Line	Purpose
columns = [...]	Defines what data to write in the CSV
DictWriter(...)	Creates a writer that understands how to pull those fields from a dict
writeheader()	uses the fieldnames list provided in csv.DictWriter, to write the column names as the first row in the CSV file.
writerows(...)	Writes multiple rows of filtered data, ignoring extra fields
'''

