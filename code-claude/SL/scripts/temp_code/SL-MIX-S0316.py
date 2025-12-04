# Movie recommendation system rating calculator

user_preferences = {'action': 7, 'comedy': 8, 'drama': 5, 'horror': 3}
genre_popularity = {'action': 0.8, 'comedy': 0.9, 'drama': 0.7, 'horror': 0.6, 'sci-fi': 0.85}

# Calculate base score from movie attributes
movie_genres = ['comedy', 'drama']
movie_length = 115  # minutes
movie_year = 2018

# Normalize movie length (shorter movies get slight boost)
length_factor = 100 / max(movie_length, 90)

# Calculate genre match score
matches = set(movie_genres).intersection(set(user_preferences.keys()))
mismatches = set(user_preferences.keys()) - set(movie_genres)

# Compute initial scores
base_score = 0
for genre in matches:
    # Add user preference score for matching genres
    base_score += user_preferences[genre] * genre_popularity.get(genre, 0.5)

# Apply small penalty for each non-matching genre (not used in final calculation)
penalty = sum(2 for _ in mismatches)

# Track premium features
is_premium = [False, True, False]

# Calculate recency bonus (not used in final calculation)
year_bonus = (movie_year - 2010) / 10 if movie_year > 2010 else 0

# Apply length factor to base score
base_score *= length_factor

# Round to nearest whole number
base_score = round(base_score)

# Premium users get a 15% boost
multiplier = 1.15

# Apply premium multiplier if any premium features
final_rating = base_score * multiplier if any(is_premium) else base_score

# Calculate engagement score (not used in final calculation)
engagement = base_score + year_bonus + (penalty * 0.5)

print(f"Result: {final_rating}")