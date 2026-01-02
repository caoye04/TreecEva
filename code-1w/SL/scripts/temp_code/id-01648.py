from itertools import combinations


def analyze_patterns(sequence):
    # Irrelevant pattern analysis (distractor)
    patterns = []
    for i in range(2, len(sequence) + 1):
        for comb in combinations(sequence, i):
            if sum(comb) % 3 == 0:
                patterns.append(comb)
    return len(patterns)  # Not used in final computation

def validate_entry(value, rules):
    # Semi-relevant validation logic
    if value < rules['min'] or value > rules['max']:
        return False
    if value % rules['step'] == 0:
        return False
    return True

def compute_modular_weight(val, base):
    # Used in scoring
    return (val * val) % base

def compute_final_score(data, thresholds):
    temp_result = 0
    debug_flags = []
    
    # Real computation begins
    for idx, item in enumerate(data):
        # Misleading state tracking
        flag = (idx + item['value']) % 7 == 0
        debug_flags.append(flag)
        
        # Actual logic: only items passing filter contribute
        if not validate_entry(item['value'], thresholds['filter']):
            continue
            
        weight = compute_modular_weight(item['value'], thresholds['base'])
        adjustment = 1
        
        # Nested conditional with early exit (relevant)
        if item['category'] == 'A':
            adjustment = 2
            secondary_check = (item['value'] + idx) % 5
            if secondary_check > 3:
                adjustment = 3
        elif item['category'] == 'B':
            adjustment = -1
        else:
            adjustment = 0
            
        contribution = weight * adjustment
        temp_result += contribution

    # Final transformation
    final_score = abs(temp_result) % 97
    
    # Dead code path (distraction)
    if final_score == 0:
        fallback = 0
        for d in debug_flags:
            fallback += int(d)
        final_score = fallback % 50
        
    return final_score

# Main execution
if __name__ == "__main__":
    data = [
        {'value': 12, 'category': 'A'},
        {'value': 7, 'category': 'B'},
        {'value': 15, 'category': 'A'},
        {'value': 4, 'category': 'C'},
        {'value': 9, 'category': 'B'},
        {'value': 18, 'category': 'A'}
    ]
    
    thresholds = {
        'min': 5,
        'max': 20,
        'step': 3,
        'base': 13
    }
    
    # Unused auxiliary variables (distractors)
    outlier_count = 0
    total_patterns = analyze_patterns([d['value'] for d in data])
    config_flag = True
    
    final_score = compute_final_score(data, thresholds)
    print(f"Result: {final_score}")