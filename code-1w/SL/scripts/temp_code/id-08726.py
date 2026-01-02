from collections import defaultdict

# Simulate student quiz scores across multiple sessions
test_scores = [
    ('Alice', [85, 90, 88]),
    ('Bob', [78, 81, 85]),
    ('Charlie', [92, 88, 94]),
    ('Diana', [76, 85, 80])
]

# Irrelevant distractor: unused variable
unused_buffer = [0] * 100

total_sum = 0
averages = []

for name, scores in test_scores:
    session_count = len(scores)
    avg = sum(scores) / session_count
    averages.append(avg)
    total_sum += avg

# Compute overall group average (not used in final result)
group_avg = total_sum / len(averages) if averages else 0

# Key computation step
final_score = max(averages, default=0)

print(f"Result: {final_score}")