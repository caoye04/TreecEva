# Social Media Interest Analysis

def calculate_compatibility(profiles):
    # Analyze text case distribution
    uppercase_count = sum(1 for c in profiles[0]['bio'] if c.isupper())
    lowercase_count = sum(1 for c in profiles[0]['bio'] if c.islower())
    case_ratio = uppercase_count / (lowercase_count + 1)  # Avoid division by zero
    
    # Extract interests from profiles
    user1_interests = set(profiles[0]['interests'])
    user2_interests = set(profiles[1]['interests'])
    
    # Calculate metrics
    total_interests = len(user1_interests.union(user2_interests))
    shared_interests = len(user1_interests.intersection(user2_interests))
    unique_interests = total_interests - shared_interests
    
    # Generate similarity score (not used in final calculation)
    similarity_score = (shared_interests / total_interests) * 100 if total_interests > 0 else 0
    
    # Process interest categories
    categories = {'music': 0, 'sports': 0, 'tech': 0, 'food': 0}
    for interest in user1_interests:
        for category in categories:
            if category in interest.lower():
                categories[category] += 1
    
    # Calculate weighted score (distraction)
    weighted_score = 0
    for i, (category, count) in enumerate(categories.items()):
        weighted_score += count * (i + 1)
    
    # Extract ages and calculate age difference
    age_diff = abs(profiles[0]['age'] - profiles[1]['age'])
    
    # Final compatibility metric (not relevant to question)
    compatibility = shared_interests * 10 - age_diff + (case_ratio * 5)
    
    return shared_interests, unique_interests, compatibility

# User profiles data
user_profiles = [
    {
        'name': 'Alex',
        'age': 28,
        'bio': 'Love hiking and PHOTOGRAPHY! Tech enthusiast.',
        'interests': ['hiking', 'photography', 'technology', 'coffee', 'travel']
    },
    {
        'name': 'Jordan',
        'age': 31,
        'bio': 'Foodie, music lover, and outdoor adventurer.',
        'interests': ['cooking', 'concerts', 'hiking', 'photography', 'camping']
    }
]

# Calculate match statistics
shared, unique, match_score = calculate_compatibility(user_profiles)

# Print results
print(f"Result: {shared}")