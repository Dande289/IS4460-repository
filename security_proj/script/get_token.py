import requests

token_url = 'http://localhost:8000/api-token-auth/'

credentials = {
    'username': 'Internal_User_01',
    'password': 'Just@T3mp',
}

response = requests.post(token_url, data=credentials)

if response.status_code == 200:
    token_data = response.json()

    print('token_data',token_data)

    token = token_data.get('token')

    if token:
        print(f"Authentication successful. Token: {token}")
    else:
        print("Token not found in response.")
else:
    print("Authentication failed. Status code:", response.status_code)
    with open('logfile.html', 'w', encoding='utf-8') as file:
        file.write(response.text)