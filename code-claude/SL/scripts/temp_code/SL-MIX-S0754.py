# Movie rating analyzer
movie_titles = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
movie_ratings = {}

# Adding ratings for each movie
movie_ratings[movie_titles[0]] = 8.8
movie_ratings[movie_titles[1]] = 8.7
movie_ratings[movie_titles[2]] = 8.6
movie_ratings[movie_titles[3]] = 9.0
movie_ratings[movie_titles[4]] = 8.9

# Calculate top-rated movie
top_rated = max(movie_ratings.values())
top_movie = ""
for movie, rating in movie_ratings.items():
    if rating == top_rated:
        top_movie = movie
        break

# Slice to get the first 3 movies for featured section
featured_movies = movie_titles[:3]

# Calculate average rating
average_rating = sum(movie_ratings.values()) / len(movie_ratings)

# Display results
print(f"Top rated movie: {top_movie}")
print(f"Featured movies: {featured_movies}")
print(f"Average rating: {average_rating}")
