def calculate_final_score(records):
    base_points = 0
    bonuses = []
    for entry in records:
        if len(entry['name']) > 5:
            base_points += 10
        else:
            base_points += 5
        
        name_upper = entry['name'].upper()
        if 'X' in name_upper or 'Z' in name_upper:
            bonuses.append(7)
        
        # Irrelevant string transformation (minor distractor)
        reversed_name = entry['name'][::-1].capitalize()

    # Apply bonus: sum and scale by number of long names
    long_name_count = sum(1 for r in records if len(r['name']) > 5)
    extra_bonus = sum(bonuses) * (long_name_count // 2)
    
    final_score = base_points + extra_bonus
    
    return final_score

# Data setup
data = [
    {'name': 'Alice', 'level': 3},
    {'name': 'Bob', 'level': 1},
    {'name': 'Charlie', 'level': 4},
    {'name': 'Zane', 'level': 2}
]

result = calculate_final_score(data)
print(f"Result: {result}")