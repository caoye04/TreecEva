# Social Media Friend Recommendation System

def calculate_compatibility_score(profile1, profile2):
    # Extract interests from profiles
    user1_interests = set(profile1['interests'])
    user2_interests = set(profile2['interests'])
    
    # Calculate potential matches based on location proximity
    location_match = profile1['city'] == profile2['city']
    country_match = profile1['country'] == profile2['country']
    location_score = 10 if location_match else (5 if country_match else 0)
    
    # Generate age group categories (not used in final calculation)
    age_groups = {range(18, 25): 'young_adult', range(25, 35): 'adult', range(35, 50): 'mid_age', range(50, 100): 'senior'}
    user1_age_group = next((group for age_range, group in age_groups.items() if profile1['age'] in age_range), 'unknown')
    user2_age_group = next((group for age_range, group in age_groups.items() if profile2['age'] in age_range), 'unknown')
    
    # Find common interests between users
    common_interests = len(user1_interests.intersection(user2_interests))
    
    # Calculate interest diversity score (not used in final calculation)
    all_interests = user1_interests.union(user2_interests)
    diversity_score = len(all_interests) * 0.5
    
    # Calculate final compatibility
    compatibility = common_interests * 3 + location_score
    
    # Apply bonus for matching education level
    if profile1['education'] == profile2['education']:
        compatibility += 7
    
    return common_interests, compatibility

# User profiles
user1 = {
    'name': 'Alex',
    'age': 28,
    'city': 'Boston',
    'country': 'USA',
    'education': 'Bachelor',
    'interests': ['hiking', 'photography', 'cooking', 'travel', 'music']
}

user2 = {
    'name': 'Jordan',
    'age': 31,
    'city': 'Chicago', 
    'country': 'USA',
    'education': 'Master',
    'interests': ['cooking', 'gaming', 'reading', 'travel']
}

# Calculate match data
common_count, match_score = calculate_compatibility_score(user1, user2)

# Other potential matches (not used in calculation)
potential_matches = {
    'Taylor': 42,
    'Morgan': 38,
    'Casey': 51
}

print(f"Result: {common_count}")