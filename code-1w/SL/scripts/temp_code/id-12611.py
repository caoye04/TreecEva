def calculate_final_score(records):
    base_score = 0
    bonus_multiplier = 1
    
    for entry in records:
        if len(entry['name']) > 5:
            base_score += 3
        
        name_hash = sum([ord(c) for c in entry['name']])
        if name_hash % 7 == 0:
            bonus_multiplier *= 1.5
    
    temperature = 25
    unrelated_list = [1, 4, 9]
    scaling_factor = 0.8
    
    raw_total = base_score * bonus_multiplier
    final_score = int(raw_total * scaling_factor)
    
    return final_score

# Data preparation
data = [
    {'name': 'Alice', 'active': True},
    {'name': 'Bob', 'active': False},
    {'name': 'Charlie', 'active': True},
    {'name': 'Dana', 'active': True}
]

result = calculate_final_score(data)
print(f"Result: {result}")