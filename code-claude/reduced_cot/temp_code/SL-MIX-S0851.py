# Calculate average rating for movies with more than 100 views
movie_data = [
    ("The Matrix", 4.7, 220),
    ("Inception", 4.8, 180),
    ("Interstellar", 4.9, 150),
    ("Memento", 4.5, 90),
    ("Primer", 4.3, 50)
]

# Extract movies with view count
views_threshold = 100
all_ratings = [(name, rating) for name, rating, views in movie_data]
filtered_ratings = [(name, rating) for name, rating, views in movie_data if views > views_threshold]

# Calculate the average rating of popular movies
rating_count = len(filtered_ratings)
average_rating = sum(map(lambda x: x[1], filtered_ratings)) / len(filtered_ratings)

# Display results with enumeration for reference
print("All movies:")
for i, (name, _) in enumerate(all_ratings):
    print(f"{i+1}. {name}")
    
print(f"\nNumber of popular movies: {rating_count}")
print(f"Average rating of popular movies: {average_rating}")