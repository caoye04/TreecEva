def calculate_final_score(records):
    valid_names = set()
    total_points = 0
    
    for entry in records.split(','):
        name, raw_score = entry.strip().split(':')
        score = int(raw_score)
        
        if len(name) > 3 and 'test' not in name.lower():
            valid_names.add(name)
            total_points += score * (2 if name[0].isupper() else 1)
    
    bonus = len(valid_names) * 5
    final_score = total_points + bonus
    
    temp_debug = [x.upper() for x in valid_names]  # Irrelevant operation (distractor)
    return final_score

# Data input
raw_data = "Alice:10, Bob:5, testUser:8, Charlie:15, dave:7, Emma:12"
data_set = raw_data.replace(' ', '')

result = calculate_final_score(data_set)
print(f"Target result: {result}")