import requests
import json
uri = "https://jsonplaceholder.typicode.com/comments"

response = requests.get(url=uri) #saving the GET response to a variable called response
data = response.json()           #Response body parsed as JSON (returns Python dict)
print("ResponseCode:", response.status_code)
print(type(data))
filtered_data1 = []
filtered_dataall = []              #Prepare the filtered data for further processing
if isinstance(data, list):
 print("LIST DataType Found:")
 for data in data:
   if str(data["id"]).startswith("1"):
     print("ID:",data["id"], "-> Name:",data["name"], "-> Email:", data["email"])
     filtered_data1.append(data)
   else:
     print("ID:",data["id"], "-> Name:",data["name"], "-> Email:", data["email"])
     filtered_dataall.append(data)
elif isinstance(data, dict):
  print("DICT DataType Found:")
  if str(data["id"]).startswith("1"):
     print("ID:",data["id"], "-> Name:",data["name"], "-> Email:", data["email"])
     filtered_data1.append(data)
  else:
     print("Non 1 ID found")
     print("ID:",data["id"], "-> Name:",data["name"], "-> Email:", data["email"])
     filtered_dataall.append(data)
  
with open("NameEmailID1.json", "w") as json_file:
    json.dump(filtered_data1, json_file, indent=1)
with open("NameEmailID.json", "w") as json_file:
    json.dump(filtered_dataall, json_file, indent=1)


'''
- This cane be used for GET https://jsonplaceholder.typicode.com/
- /posts,/albums,/comments,/photos,/todos,/usrs'''
   
