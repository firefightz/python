import requests


response = requests.get(f"https://api.genderize.io?name=ted")
print(type(response.json()))