# Movie recommendation system - finding common interests between users

# User preferences (favorite genres)
user1_preferences = {'action', 'comedy', 'sci-fi', 'thriller', 'documentary'}
user2_preferences = {'romance', 'comedy', 'thriller', 'horror', 'animation'}
user3_preferences = {'documentary', 'drama', 'thriller', 'comedy', 'western'}

# Popularity scores (not directly relevant to final calculation)
popularity_scores = {
    'action': 85,
    'comedy': 92,
    'sci-fi': 78,
    'thriller': 88,
    'documentary': 65,
    'romance': 76,
    'horror': 73,
    'animation': 81,
    'drama': 79,
    'western': 62
}

# Calculate average popularity of each user's preferences
user1_avg_score = sum(popularity_scores[genre] for genre in user1_preferences) / len(user1_preferences)
user2_avg_score = sum(popularity_scores[genre] for genre in user2_preferences) / len(user2_preferences)
user3_avg_score = sum(popularity_scores[genre] for genre in user3_preferences) / len(user3_preferences)

# Find potential movie matches
all_genres = user1_preferences.union(user2_preferences)
total_unique = len(all_genres)

# Check which user has the highest average popularity score
highest_score_user = max(user1_avg_score, user2_avg_score, user3_avg_score)

# Identify common preferences between users 1 and 2
common_genres = len(user1_preferences.intersection(user2_preferences))

# Calculate compatibility score (not used in final answer)
compatibility = (common_genres / total_unique) * 100
rounded_compatibility = int(compatibility)

# Potential movie recommendations count (not used in final result)
potential_recommendations = common_genres * 5

print(f"Result: {common_genres}")