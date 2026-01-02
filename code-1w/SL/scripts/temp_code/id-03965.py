from collections import defaultdict

# Simulate user feedback analysis for a training module
ratings = [4, 5, 2, 3, 5, 5, 4, 1, 3, 4, 5, 2]
feedback_counter = defaultdict(int)
invalid_entries = 0
temp_sum = 0

# Count frequency of each rating
for r in ratings:
    if 1 <= r <= 5:
        feedback_counter[r] += 1
        temp_sum += r
    else:
        invalid_entries += 1

# Calculate average (unused distractor)
avg_rating = temp_sum / len(ratings) if ratings else 0

# Track cumulative distribution (semi-relevant)
cumulative = 0
distribution = {}
for i in sorted(feedback_counter.keys()):
    cumulative += feedback_counter[i]
    distribution[i] = cumulative

# Determine maximum frequency count
max_count = max(feedback_counter.values())
mode_candidates = [k for k, v in feedback_counter.items() if v == max_count]
mode_rating = min(mode_candidates)  # Smallest rating among most frequent

# Secondary metric: weighted boost based on high ratings
high_performers = 0
for rating, count in feedback_counter.items():
    if rating >= 4:
        high_performers += count

boost_factor = high_performers / len(ratings)
adjusted_mode = mode_rating + (boost_factor * 0.5)

# Core evaluation logic
max_rating = max(ratings)

def evaluate_performance(counter, peak):
    base = counter[5] * 10
    penalty = 0
    if counter[1] > 0:
        penalty = 5
    if counter[2] >= 2:
        penalty += 3
    return base - penalty

# Critical statement
final_score = evaluate_performance(feedback_counter, max_rating)

# Additional irrelevant computation (distractor)
total_pairs = 0
for i in range(len(ratings)):
    for j in range(i+1, len(ratings)):
        if abs(ratings[i] - ratings[j]) <= 1:
            total_pairs += 1

print(f"Result: {final_score}")