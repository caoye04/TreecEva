def calculate_final_score(records):
    valid_names = {name.capitalize() for name in ['alice', 'bob', 'charlie']}
    scores = []
    
    for entry in records:
        name = entry['name'].strip()
        if name.capitalize() not in valid_names:
            continue
        raw_score = entry['score'] * 0.9
        if raw_score < 60:
            adjusted = raw_score + 10
        else:
            adjusted = raw_score
        category_bonus = 5 if len(name) % 2 == 0 else 0
        total_entry = adjusted + category_bonus
        scores.append(total_entry)
    
    base_avg = sum(scores) / len(scores) if scores else 0
    penalty = 7 if any(s < 70 for s in scores) else 0
    return int(base_avg - penalty)

# Irrelevant utility function (minor interference)
def unused_helper(x):
    return x ** 2 + 1

# Main data
user_data = [
    {'name': 'Alice ', 'score': 85},
    {'name': 'BOB', 'score': 55},
    {'name': 'Charlie', 'score': 90},
    {'name': 'David', 'score': 75}  # Invalid name
]

final_score = calculate_final_score(user_data)
print(f"Result: {final_score}")