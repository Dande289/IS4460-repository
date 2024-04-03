import requests
import json


api_url = 'http://localhost:8000/api/order/'


order_data = {
    "total_price": "20",
    "total_items": "5",
    "customer": 5
}


response = requests.post(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Order created successfully.")
else:
    print(f"Error creating order.")