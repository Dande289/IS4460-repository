import requests
import json


api_url = 'http://localhost:8000/api/movie_list/'


movie_data = {
    "title": "Terminator 2: Judgment Day",
    "description": "Description about Terminator 2",
    "director": "James Cameron",
    "release_date": "1991-01-01",
    "genre": "Action/Adventure",
    "budget": "80.00",
    "rating": "0"
}


response = requests.post(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Movie created successfully.")
else:
    print(f"Error creating movie.")