from math import comb

# Simulate a sequence of daily user engagements over a week
engagements = [12, 18, 22, 35, 27, 40, 33]

# Calculate number of unique pairs of users that can interact on each day
pair_counts = [comb(n, 2) for n in engagements]

# Focus only on mid-week dynamics using slicing
mid_week_pairs = pair_counts[2:5]

# Sum the interaction potential from the middle three days
comb_sliced_sum = sum(mid_week_pairs)

# Irrelevant distraction: unused variable representing weekend average
weekend_avg = sum(engagements[5:]) / 2

result = comb_sliced_sum
print(f"Result: {result}")