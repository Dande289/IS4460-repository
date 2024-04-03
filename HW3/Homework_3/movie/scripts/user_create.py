import requests
import json

api_url = 'http://localhost:8000/api/users/'


user_data = {
    "username": "user_name_1",
    "password": "password1",
    "first_name": "First_Name_1",
    "last_name": "Last_Name_2",
    "email": "test@test.com"
}


response = requests.post(api_url, data=json.dumps(user_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("User created successfully.")
else:
    print(f"Error creating user.")