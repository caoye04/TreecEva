# Calculate the average rating for movies released after 2010

movie_data = [
    {"title": "Inception", "year": 2010, "rating": 8.8},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0},
    {"title": "Interstellar", "year": 2014, "rating": 8.6},
    {"title": "Parasite", "year": 2019, "rating": 8.5},
    {"title": "Joker", "year": 2019, "rating": 8.4},
    {"title": "Avatar", "year": 2009, "rating": 7.8}
]

# Extract movies released after 2010
recent_movies = [movie for movie in movie_data if movie["year"] > 2010]

# Create a dictionary of movie titles and their ratings
movie_ratings = {movie["title"]: movie["rating"] for movie in movie_data}

# Filter ratings for only recent movies
filtered_ratings = {movie["title"]: movie["rating"] for movie in recent_movies}

# Calculate average rating of filtered movies
average_rating = sum(filtered_ratings.values()) / len(filtered_ratings)

# Display the number of movies considered
print(f"Number of movies considered: {len(filtered_ratings)}")

# Display the result
print(f"Result: {average_rating}")