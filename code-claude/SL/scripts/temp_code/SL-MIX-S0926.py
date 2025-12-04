def calculate_weighted_value(value, multiplier=1.5, threshold=75):
    weighted = value * multiplier
    if weighted > threshold:
        return threshold
    return weighted

# Recipe ratings data with user_id, rating, and cooking_time in minutes
ratings_data = [
    (101, 4.8, 45),  # user_id, rating, cooking_time
    (102, 3.2, 30),
    (103, 4.5, 60),
    (104, 2.7, 25),
    (105, 5.0, 40),
    (106, 3.8, 35),
    (107, 4.2, 50)
]

# Ingredient availability (not directly used in final calculation)
ingredient_stock = {
    'flour': 1200,  # grams
    'sugar': 800,   # grams
    'eggs': 6,      # count
    'butter': 500,  # grams
    'milk': 1000    # ml
}

# Process the ratings
adjusted_ratings = []
time_penalties = []

# Track users who rated above 4.0
premium_users = []
for user_id, rating, time in ratings_data:
    # Apply time penalty for long cooking times
    time_factor = 1.0
    if time > 40:
        time_factor = 0.9
        time_penalties.append((user_id, 0.1))
    
    # Calculate adjusted rating
    adj_rating = rating * time_factor
    adjusted_ratings.append(adj_rating)
    
    # Track premium users (not used in final calculation)
    if rating > 4.0:
        premium_users.append(user_id)

# Calculate statistics
avg_rating = sum(adjusted_ratings) / len(adjusted_ratings)
distance_from_avg = [abs(r - avg_rating) for r in adjusted_ratings]

# Apply normalization to the ratings
max_distance = max(distance_from_avg) if distance_from_avg else 1
normalized_distances = [d/max_distance for d in distance_from_avg]

# Generate scores based on distance from average
base_scores = []
for i, (rating, distance) in enumerate(zip(adjusted_ratings, normalized_distances)):
    # Higher rating and closer to average gets higher score
    score = rating * (1 - distance * 0.5)
    base_scores.append(score)

# Filter out scores below threshold
threshold = 3.0
valid_scores = [score for score in base_scores if score > threshold]

# Calculate the final score as the sum of valid scores
final_score = sum(valid_scores)

# Prepare ingredients report (not used in final calculation)
ingredient_usage = {}
for ingredient, amount in ingredient_stock.items():
    usage_percent = (amount / 1000) * 100 if amount > 500 else amount / 10
    ingredient_usage[ingredient] = usage_percent

print(f"Result: {final_score}")