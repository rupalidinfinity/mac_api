import requests
r = requests.get('https://api.macaddress.io/v1?apiKey=at_8CnUDq5XAbNywiGrzj77SJEBkoQy2&output=json&search=44:38:39:ff:ef:57').json()
print(r)