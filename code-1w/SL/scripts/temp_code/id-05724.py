from collections import Counter

def analyze_pattern(sequence):
    count = Counter(sequence)
    most_frequent = count.most_common(1)[0][1]
    least_frequent = count.most_common()[-1][1]
    return most_frequent - least_frequent

def validate_entry(record):
    if not record.get('active'):
        return False
    tags = record.get('tags', [])
    if 'deprecated' in tags:
        return False
    return len(tags) > 0

def calculate_adjusted_score(points, penalties):
    base_modifier = 1.5 if points > 100 else 0.8
    penalty_deduction = min(penalties * 7, 50)
    adjusted = points * base_modifier - penalty_deduction
    
    # Distractor: complex string processing unrelated to score
    status_msg = f"Processing {points} points with {penalties} penalties"
    clean_msg = status_msg.replace('Processing', 'Analyzing').upper()
    word_count = len(clean_msg.split())
    char_count = len([c for c in clean_msg if c.isalpha()])
    
    # Irrelevant data structure manipulation
    temp_data = [{'step': i, 'val': i**2} for i in range(3)]
    temp_sum = sum(d['val'] for d in temp_data if d['step'] % 2 == 0)
    
    # Actual computation path
    if adjusted > 200:
        adjusted *= 0.95
    elif adjusted < 50:
        adjusted += 10
    
    # More distraction: unused conditional expression
    debug_flag = 'HIGH' if adjusted > 300 else 'LOW'
    log_entry = f"Score:{'Critical' if debug_flag=='HIGH' else 'Normal'}"
    
    return int(adjusted)

def main():
    raw_points = 180
    penalty_count = 6
    
    # Simulate data preprocessing (distractor)
    data_stream = [1, 2, 2, 3, 3, 3, 4]
    pattern_complexity = analyze_pattern(data_stream)
    
    # Mock validation of entries (semi-relevant but not used)
    records = [
        {'active': True, 'tags': ['urgent', 'verified']},
        {'active': False, 'tags': ['deprecated']}
    ]
    valid_records = [r for r in records if validate_entry(r)]
    
    # Core calculation
    final_score = calculate_adjusted_score(raw_points, penalty_count)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()