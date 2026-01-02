from collections import defaultdict, Counter

# Simulate student test responses across multiple sections
responses = [
    ('Alice', 'Math', 'correct'), ('Bob', 'Math', 'incorrect'),
    ('Alice', 'Math', 'correct'), ('Charlie', 'Math', 'correct'),
    ('Bob', 'Science', 'correct'), ('Charlie', 'Science', 'incorrect'),
    ('Alice', 'Science', 'correct'), ('Bob', 'Science', 'correct')
]

# Aggregate responses by subject and student
subject_data = defaultdict(lambda: defaultdict(int))
response_counter = Counter()

for student, subject, result in responses:
    subject_data[subject][student] += 1 if result == 'correct' else 0
    response_counter[student] += 1

# Extract raw counts (some used later, some not)
total_responses_per_student = dict(response_counter)
dummy_aggregation = [len(subject_data[sub]) for sub in subject_data]  # Distractor

# Normalize scores per subject
normalized = {}
for subject, students in subject_data.items():
    total_correct = sum(students.values())
    max_possible = len([r for r in responses if r[1] == subject])
    normalized[subject] = total_correct / max_possible if max_possible > 0 else 0

# Bucket students by performance tier (distractor structure)
performance_tier = defaultdict(list)
for student, count in response_counter.items():
    tier = 'high' if count >= 3 else 'medium' if count == 2 else 'low'
    performance_tier[tier].append(student)

# Create score buckets based on normalized subject performance
buckets = []
for subject, score in normalized.items():
    if score >= 0.5:
        buckets.append((subject, round(score * 100, 2)))

# Irrelevant slicing operation (partial distractor)
sliced_buckets = buckets[::1]  # Redundant slice

# Additional irrelevant computation
shadow_copy = [b for b in buckets if b[1] > 50]
shadow_total = sum(sb[1] for sb in shadow_copy)  # Not used later

# Core ranking logic
def calculate_ranking(bucket_list):
    if not bucket_list:
        return 0
    base_rank = sum(entry[1] for entry in bucket_list)
    bonus = len(bucket_list) * 5
    penalty = 0
    for entry in bucket_list:
        if entry[1] < 75:
            penalty += 10
    return int(base_rank + bonus - penalty)

# Key execution point
final_score = calculate_ranking(buckets)

print(f"Result: {final_score}")