from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'X' and i % 2 == 0:
            count += 1
    return count

def validate_entry(record):
    # Irrelevant validation logic (dead end)
    if not record.get('active'):
        return False
    if len(record['id']) < 3:
        return False
    return True

def compute_weighted_sum(indices, weights):
    total = 0.0
    for idx, w in zip(indices, weights):
        total += idx * w
    return total

def evaluate_performance(results, multiplier):
    base_points = 0
    penalty = 0
    
    # Real logic path
    for res in results:
        if res['success']:
            base_points += res['level']
        else:
            penalty += 1
    
    # Distractor: complex but unused combinatorics
    all_pairs = list(combinations(results, 2))
    pair_score = 0
    for p in all_pairs:
        if p[0]['level'] == p[1]['level']:
            pair_score += 1  # Not used later
    
    # Another distractor variable
    temp_flag = any(r['status'] == 'critical' for r in results)
    
    # Actual computation
    raw_score = base_points * multiplier - (penalty * 2)
    adjustment = len(results) // 4
    final_score = int(raw_score - adjustment)
    
    # Print at critical point
    return final_score

# Main execution
if __name__ == '__main__':
    task_data = [
        {'level': 3, 'success': True, 'status': 'normal', 'meta': 'A'},
        {'level': 5, 'success': True, 'status': 'normal', 'meta': 'B'},
        {'level': 2, 'success': False, 'status': 'warning', 'meta': 'C'},
        {'level': 4, 'success': True, 'status': 'normal', 'meta': 'D'},
        {'level': 1, 'success': False, 'status': 'critical', 'meta': 'E'}
    ]

    # Preprocessing with enumerate and string method (semi-relevant)
    processed = []
    for i, item in enumerate(task_data):
        item['id'] = f"T{i+1}".upper()
        item['active'] = True
        processed.append(item)
    
    # Filtering valid entries (some are invalid but all here are valid)
    filtered = [p for p in processed if validate_entry(p)]
    
    # Extract indices and dummy weights for irrelevant calculation
    indices = [i for i, _ in enumerate(filtered) if _['success']]
    weights = [0.5, 1.0, 1.5]  # Mismatched length — causes truncation in zip
    dummy_sum = compute_weighted_sum(indices, weights)
    
    # Pattern analysis on fake status codes
    status_codes = ''.join([f"{item['status'][0].upper()}" for item in filtered])
    pattern_match_count = analyze_pattern(status_codes + "XX")
    
    base_multiplier = 10
    final_score = evaluate_performance(filtered, base_multiplier)
    print(f"Result: {final_score}")