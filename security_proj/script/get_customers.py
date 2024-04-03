import requests

api_url = 'http://localhost:8000/api/customers/'

token = '98d67f3158c9e9955f57c50b3bd03f0a3465117a'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url,headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(f"Customers retrieval successful. {response.text}")
else:
    print(f"Customers retrieval failed. {response.text}")