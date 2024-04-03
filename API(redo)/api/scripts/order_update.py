import requests
import json

id = 2

api_url = f'http://localhost:8000/api/order/{id}/'

order_data = {
    "total_price": "8.99",
    "total_items": "3",
    "customer": 5

}

response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Order updated successfully")
else:
    print("Error updating the order.")