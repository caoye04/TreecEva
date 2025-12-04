from collections import Counter

# Simulating vote counts from different precincts
precinct_votes = [3, 7, 5, 3, 2, 5, 7, 3, 5, 7, 2, 3, 5, 7, 3]
frequency_counter = Counter(precinct_votes)

# Calculate total votes excluding candidate with ID 5
total_votes = sum(frequency_counter.values())
candidate_5_votes = frequency_counter[5]
result = total_votes - candidate_5_votes

print(f"Result: {result}")