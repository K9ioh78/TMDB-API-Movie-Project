import requests

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer 324484c43b7b66c0989196b54906bc6e"  # if you're using bearer token
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    movies = response.json().get('results', [])
    for movie in movies:
        print(f"{movie['title']} - Rating: {movie['vote_average']} - Release: {movie['release_date']}")
else:
    print("Failed to fetch data:", response.status_code)
