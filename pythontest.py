import requests

mac_address=input('Please Enter MAC:')
if len(mac_address)>0:
    r = requests.get('https://api.macaddress.io/v1?apiKey=at_8CnUDq5XAbNywiGrzj77SJEBkoQy2&output=json&search='+mac_address).json()
    print("%s MAC Address is Associated with  Company %s ." %(mac_address, r['vendorDetails']['companyName']))
else :
    print('Please Enter Proper MAC Address.')
