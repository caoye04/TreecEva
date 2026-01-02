def calculate_final_score(students, threshold):
    total_scores = []
    bonus_applied = 0

    for student in students:
        name = student['name']
        score = student['score']
        active = student['active']

        if not active:
            continue

        if score > threshold:
            score += 5
            bonus_applied += 1

        # Normalize name and check length condition
        normalized_name = name.strip().lower()
        if len(normalized_name) > 6:
            score -= 1

        total_scores.append(score)

    # Apply final adjustment based on bonus frequency
    if bonus_applied >= 2:
        final_adjustment = len(total_scores)
    else:
        final_adjustment = -1 * (threshold // 10)

    return sum(total_scores) + final_adjustment


# Data setup
students_data = [
    {'name': 'Alice Johnson', 'score': 88, 'active': True},
    {'name': 'Bob', 'score': 92, 'active': True},
    {'name': 'Charlie Davis', 'score': 76, 'active': False},
    {'name': 'Diana Lee', 'score': 85, 'active': True},
    {'name': 'Eve', 'score': 90, 'active': True}
]

threshold_value = 84

# Irrelevant utility function (distractor)
def get_average_name_length(data):
    names = [entry['name'] for entry in data if entry['active']]
    return sum(len(n) for n in names) / len(names) if names else 0

# Main computation
final_score = calculate_final_score(students_data, threshold_value)
print(f"Result: {final_score}")