def calculate_score(set_a, set_b):
    # Calculate intersection weight
    common_elements = set_a.intersection(set_b)
    weight_factor = 10
    
    # This calculation doesn't affect the result
    potential_bonus = len(set_a) * 0.5
    engagement_metric = sum(1 for _ in set_a if _ % 2 == 0)
    
    # Main calculation
    return len(common_elements) * weight_factor

# User data setup
all_users = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}
active_users = {101, 103, 105, 107, 109}
premium_users = {102, 103, 105, 108, 110}
inactive_users = all_users - active_users

# Analyze user segments
user_segments = {}
for idx, user_id in enumerate(all_users):
    segment_code = (user_id % 3) + 1
    if segment_code not in user_segments:
        user_segments[segment_code] = []
    user_segments[segment_code].append(user_id)

# Calculate various metrics
total_users = len(all_users)
average_id = sum(all_users) / total_users

# Process user data with zip
user_status = []
for active, premium in zip(sorted(active_users), sorted(premium_users)):
    user_status.append((active, premium, active == premium))

# Calculate segment popularity (unused in final result)
segment_popularity = {}
for segment, users in user_segments.items():
    premium_count = len([u for u in users if u in premium_users])
    segment_popularity[segment] = premium_count / len(users) if users else 0

# Calculate the intersection score
intersection_score = calculate_score(active_users, premium_users)

# Calculate alternative scores (not used in final result)
alternative_score = calculate_score(active_users, inactive_users)
premium_ratio = len(premium_users) / total_users

print(f"Result: {intersection_score}")