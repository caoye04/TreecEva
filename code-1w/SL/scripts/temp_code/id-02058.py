from collections import defaultdict

# Simulate student quiz scores with potential retries
test_data = [
    ('Alice', 85), ('Bob', 90), ('Alice', 92), ('Charlie', 88),
    ('Bob', 87), ('Alice', 95), ('Charlie', 91)
]

# Aggregate scores using defaultdict
score_lists = defaultdict(list)
for name, score in test_data:
    score_lists[name].append(score)

# Compute average score for each student
averages = {name: sum(scores) / len(scores) for name, scores in score_lists.items()}

# Define penalty map (e.g., late submission penalties)
penalties = {'Alice': 3, 'Bob': 2, 'Charlie': 4}

# Higher-order function to adjust score based on penalty
apply_penalty = lambda score, penalty: score - penalty * 0.5

# Calculate final score as adjusted average minus penalty effect
def calculate_final_score(avg_dict, penalty_dict):
    total_adjusted = 0.0
    for student, avg in avg_dict.items():
        if student in penalty_dict:
            adjusted = apply_penalty(avg, penalty_dict[student])
            total_adjusted += adjusted
    return int(total_adjusted)  # Discrete final evaluation

# Execute calculation
result = calculate_final_score(averages, penalties)
print(f"Result: {result}")