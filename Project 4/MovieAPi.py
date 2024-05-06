import requests

def get_top_movies(api_key, num_movies=20):
    """Fetch top-rated movies from TMDb."""
    movies = []
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        movies.extend(data['results'][:num_movies])
    else:
        print("Failed to fetch data:", response.status_code)
    return movies

def get_movie_details(api_key, movie_id):
    """Fetch detailed information for a specific movie."""
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


api_key = 'e6bf020deaf3a86a8ad31461a801b6a0'

# Get top 20 movies
top_movies = get_top_movies(api_key)

# Fetch and display details for each movie
for movie in top_movies:
    details = get_movie_details(api_key, movie['id'])
    if details:
        print(f"Title: {details['title']}")
        print(f"Release Date: {details['release_date']}")
        print(f"Popularity: {details['popularity']}")
        print(f"Vote Average: {details['vote_average']}")
        print("-" * 40)
