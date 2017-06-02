import requests

r = requests.get("https://patient.heal.com/api")

print(r.text)
print("Response printed")
