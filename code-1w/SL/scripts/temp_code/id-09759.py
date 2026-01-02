from collections import defaultdict
import itertools

# Simulate student test responses and compute diagnostic ranking
responses = [
    {'student': 'A', 'answers': [1, 2, 3, 4], 'time_spent': 45},
    {'student': 'B', 'answers': [1, 2, 0, 4], 'time_spent': 30},
    {'student': 'C', 'answers': [1, 2, 3, 4], 'time_spent': 60},
    {'student': 'D', 'answers': [0, 0, 0, 0], 'time_spent': 10},
    {'student': 'E', 'answers': [1, 2, 3, 4], 'time_spent': 50}
]

# Correct answers for each question
key = [1, 2, 3, 4]

# Irrelevant frequency map for distraction
timing_frequency = defaultdict(int)
for r in responses:
    bucketed_time = (r['time_spent'] // 15) * 15
    timing_frequency[bucketed_time] += 1

# Compute correctness per student
accuracy_map = {}
for r in responses:
    correct = sum(1 for i, ans in enumerate(r['answers']) if ans == key[i] and ans != 0)
    accuracy_map[r['student']] = correct / len(key)

# Group students by performance tier (distractor grouping)
performance_tiers = defaultdict(list)
for r in responses:
    score = sum(1 for i, ans in enumerate(r['answers']) if ans == key[i])
    tier = 'high' if score >= 3 else 'low'
    performance_tiers[tier].append(r['student'])

# Compute attempt statistics (partially relevant)
attempt_counts = [sum(1 for a in r['answers'] if a != 0) for r in responses]
avg_attempts = sum(attempt_counts) / len(attempt_counts)

# Bucket students by time efficiency and accuracy
buckets = []
for r in responses:
    accuracy = accuracy_map[r['student']]
    efficiency = r['time_spent'] / max(attempt_counts) if max(attempt_counts) > 0 else 0
    # Weighted composite score (actual logic start)
    raw_score = accuracy * 100 - efficiency * 10
    buckets.append({'student': r['student'], 'score': raw_score})

# Misleading sort: not used in final calculation
sorted_by_name = sorted(buckets, key=lambda x: x['student'])

# Actual processing: group by rounded score and count high performers
grouped = defaultdict(int)
for b in buckets:
    rounded = int(b['score'] // 10)
    grouped[rounded] += 1

# Secondary distraction: generate all pairs of students (unused)
all_pairs = list(itertools.combinations([r['student'] for r in responses], 2))

# Identify dominant performance cluster
max_group_size = max(grouped.values())
dominant_band = [k for k, v in grouped.items() if v == max_group_size][0]

# Calculate ranking score using only specific conditions
def calculate_ranking(bucket_list):
    total = 0
    for item in bucket_list:
        base = item['score']
        if base > 70:
            total += 3
        elif base > 50:
            total += 2
        else:
            total += 1
    # Apply multiplier based on dominant band (critical dependency)
    modifier = 2 if dominant_band >= 7 else 1.5
    return total * modifier

# Final computation
final_score = calculate_ranking(buckets)
print(f"Result: {final_score}")