# Student score analysis
primary_scores = [85, 92, 78, 90, 88, 76, 95, 89]
secondary_scores = {80, 85, 90, 95, 100}

# Initialize counters
total_primary = sum(primary_scores)
avg_primary = total_primary / len(primary_scores)

# Find scores that appear in both sets
common_elements = len(set(primary_scores).intersection(secondary_scores))

# Calculate weighted score
weighted_score = avg_primary * 0.6 + sum(secondary_scores) / len(secondary_scores) * 0.4

print(f"Result: {common_elements}")