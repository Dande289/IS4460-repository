import requests
import json

id = 3

api_url = f'http://localhost:8000/api/movie_list/{id}/'

movie_data = {
    "title": "Terminator 2: Judgment Day",
    "description": "Another updated description about Terminator 2",
    "director": "James Cameron",
    "release_date": "1991-01-01",
    "genre": "Action/Adventure",
    "budget": "80.00",
    "rating": "0"

}

response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Movie updated successfully")
else:
    print("Error updating the movie.")