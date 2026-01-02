from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(2, len(sequence) + 1):
        for combo in combinations(sequence, i):
            if sum(combo) % 3 == 0:
                count += 1
    return count

def validate_entry(record):
    if not record.get('active'):
        return False
    if record.get('age', 0) < 18:
        return False
    return True

def calculate_final_score(data, thresholds):
    raw_values = []
    temp_flags = {}
    total_weight = 0.0
    adjustment_factor = 1.2
    
    # Irrelevant pre-processing: analyzing string patterns in names
    name_analysis = {}
    for entry in data:
        name = entry.get('name', '')
        vowel_count = sum(1 for c in name.lower() if c in 'aeiou')
        name_analysis[name] = vowel_count
    
    # Actual processing begins
    for idx, entry in enumerate(data):
        if validate_entry(entry):
            base_value = entry.get('score', 0)
            multiplier = entry.get('level', 1)
            weighted_val = base_value * multiplier
            
            # Conditional branching based on threshold groups
            if weighted_val > thresholds['high']:
                weighted_val *= 1.5
            elif weighted_val > thresholds['medium']:
                weighted_val *= 1.2
            else:
                weighted_val *= 0.9
            
            raw_values.append(weighted_val)
            total_weight += multiplier

    # Dead code path - never accessed due to logic above
    if len(raw_values) == 0 and len(data) > 5:
        fallback = sum([d.get('score', 0) for d in data])
        temp_flags['fallback_used'] = True

    # Real computation
    base_score = sum(raw_values)
    if total_weight > 0:
        base_score /= total_weight
    
    # Apply adjustment using dict operation
    config = {'version': 'A', 'adjust': True}
    if config.get('adjust'):
        base_score *= adjustment_factor
    
    # Final pattern analysis (irrelevant but looks important)
    sequence = [int(x) for x in raw_values if x > 0]
    pattern_bonus = analyze_patterns(sequence) % 10
    
    final_score = int(base_score + pattern_bonus)  # Key assignment point
    
    print(f"Result: {final_score}")
    return final_score

data_set = [
    {'name': 'Alice', 'score': 85, 'level': 2, 'age': 25, 'active': True},
    {'name': 'Bob', 'score': 70, 'level': 3, 'age': 17, 'active': True},  # invalid due to age
    {'name': 'Charlie', 'score': 90, 'level': 1, 'age': 30, 'active': True},
    {'name': 'Diana', 'score': 60, 'level': 4, 'age': 22, 'active': False}, # inactive
    {'name': 'Eve', 'score': 95, 'level': 2, 'age': 28, 'active': True}
]

thresholds_config = {
    'low': 50,
    'medium': 75,
    'high': 90
}

final_score = calculate_final_score(data_set, thresholds_config)