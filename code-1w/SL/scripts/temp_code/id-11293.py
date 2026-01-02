def analyze_metrics(data):
    # Irrelevant preprocessing step (distractor)
    normalized = [x * 0.95 for x in data if x > 0]
    outliers = [x for x in data if x > 100]
    adjusted = [x for x in data if x <= 100]

    # Semi-relevant transformation
    scaled = [x * 1.1 for x in adjusted]
    
    # Core computation embedded within noise
    base_total = sum(scaled) / len(adjusted) if adjusted else 0
    bonus = len(outliers) * 2.5 if outliers else 0
    penalty = len([x for x in data if x < 0]) * 1.5
    return base_total + bonus - penalty


def calculate_performance(entries):
    # Misleading initialization
    temp_results = []
    intermediate_avg = 0
    snapshot = []
    
    for item in entries:
        if 'active' in item and item['active']:
            temp_results.append(item['value'])
    
    # Real processing hidden among irrelevant operations
    filtered_data = [item['value'] for item in entries if item.get('status') == 'valid']
    backup_copy = filtered_data.copy()
    backup_copy.append(sum(filtered_data) // len(filtered_data) if filtered_data else 0)

    # Key distraction: unused function call simulation
    debug_mode = False
    if debug_mode:
        snapshot = [x * 2 for x in backup_copy]

    # Actual logic for final score
    metric_a = analyze_metrics(filtered_data)
    metric_b = len([x for x in entries if x['value'] % 2 == 0 and x.get('tag') == 'primary'])
    adjustment = 0.75 * metric_b
    final_value = metric_a + adjustment
    
    # This is the actual answer variable
    final_score = int(round(final_value))
    return final_score

# Simulated dataset
benchmark_data = [
    {'value': 42, 'status': 'valid', 'active': True, 'tag': 'primary'},
    {'value': 85, 'status': 'valid', 'active': False, 'tag': 'secondary'},
    {'value': 105, 'status': 'invalid', 'active': True, 'tag': 'primary'},
    {'value': 24, 'status': 'valid', 'active': True, 'tag': 'primary'},
    {'value': -5, 'status': 'valid', 'active': True, 'tag': 'other'},
    {'value': 60, 'status': 'valid', 'active': True, 'tag': 'primary'},
    {'value': 110, 'status': 'valid', 'active': False, 'tag': 'primary'}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")