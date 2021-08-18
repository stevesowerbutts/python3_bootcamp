import requests
url = "https://icanhazdadjoke.com/"
#url = "http://www.google.com"

# API needs to be confiugred to respond with data in the correct way.
# eg. set url to www.google.com - does not return plain text
# response = requests.get(url, headers={"Accept": "text/plain"})
# print(response.text)

response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()

print(data["joke"])
print(f"status: {data['status']}")
