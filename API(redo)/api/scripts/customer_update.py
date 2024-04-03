import requests
import json

id = 5

api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {
    "name": "Customer XXXXX",
    "email": "customerX@example.com",
    "phone_number": "8012224444"

}

response = requests.put(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Customers updated successfully")
else:
    print("Error updating the customer.")
