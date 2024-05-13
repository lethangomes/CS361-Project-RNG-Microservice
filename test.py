import requests

url = "http://127.0.0.1:5000"

print("Unseeded Random numbers")
seed = "none"
response = requests.post(url + "/seed", json=seed).json()
print(response)
input()

data = {"min": 0, "max" : 10}
response = requests.post(url + "/generateOne", json=data).json()
print("One random number: " + str(response))
input()

data = {"min": 0, "max" : 10, "amount" : 5}
response = requests.post(url + "/generateList", json=data)
print("Five random numbers: " + str(response.json()))
input()

print("Seeded Random numbers")
seed = 13
response = requests.post(url + "/seed", json=seed)
print(response.json())
input()

data = {"min": 0, "max" : 10}
response = requests.post(url + "/generateOne", json=data)
print("One random number: " + str(response.json()))
input()

data = {"min": 0, "max" : 10, "amount" : 5}
response = requests.post(url + "/generateList", json=data)
print("Five random numbers: " + str(response.json()))