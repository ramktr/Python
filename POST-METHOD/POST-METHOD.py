import requests
import json
'''token = input("Enter the token:")'''
uri = "https://jsonplaceholder.typicode.com/comments"

header = {
    "Authorization" : f"Bearer { token }",
    "Content-Type" : f"application/json"
}

with open("payload.json", "r") as json_file:
  payload = json.load(json_file)


response = requests.post(url=uri, json=payload)
print(response.status_code)
print(response.text)