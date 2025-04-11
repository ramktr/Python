import requests
import json

owner = input("Enter the Owner of the Repo:")
repo = input("Enter the RepoName to check:")
token = input("Enter the Bearer Toekn:")

header = {
    "Authorization": f"Bearer {token}"
    }


uri = f"https://api.github.com/repos/{owner}/{repo}" #Use f"...{var}..." to dynamically build strings with variables.
print("url:",uri)

response = requests.get(url=uri, headers=header)
pydict = response.json()
print(type(pydict))
print(json.dumps(pydict, indent=1))

