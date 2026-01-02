def analyze_performance(records):
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    outlier_threshold = 100
    
    for record in records:
        if record['value'] < outlier_threshold:
            valid_count += 1
            temp_sum += record['value']
    
    average_valid = temp_sum / valid_count if valid_count else 0
    return average_valid

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return sum(x ** 2 for x in data) // len(data) if data else 0

# Simulated sensor readings with metadata
data_log = [
    {'sensor': 'A1', 'value': 45, 'status': 'OK'},
    {'sensor': 'A2', 'value': 120, 'status': 'ERROR'},
    {'sensor': 'A3', 'value': 67, 'status': 'OK'},
    {'sensor': 'A4', 'value': 89, 'status': 'OK'},
    {'sensor': 'A5', 'value': 210, 'status': 'ERROR'}
]

# Extract values and classify
clean_values = [entry['value'] for entry in data_log if entry['status'] == 'OK']
error_values = [entry['value'] for entry in data_log if entry['status'] == 'ERROR']

duplicates_check = set()
duplicate_count = 0
for v in clean_values:
    if v in duplicates_check:
        duplicate_count += 1
    duplicates_check.add(v)

# Additional irrelevant aggregation
squared_map = {x: x**2 for x in clean_values}
inverse_map = {x: round(1/x, 4) for x in clean_values if x != 0}

# Core computation begins
baseline = analyze_performance(data_log)

evaluation_weights = {
    'base': 0.6,
    'bonus': 0.3,
    'penalty': 0.1
}

stats = {
    'mean_clean': sum(clean_values) / len(clean_values),
    'count_clean': len(clean_values),
    'outlier_count': len(error_values)
}

modifiers = {
    'efficiency': 1.2 if stats['count_clean'] > 2 else 1.0,
    'stability': 0.9 if duplicate_count > 0 else 1.1
}

# Red herring: complex dictionary operation that doesn't impact final result
snapshot = {
    k: (v * modifiers['efficiency']) for k, v in squared_map.items()
}
snapshot_checksum = sum(snapshot.values()) % 1000

# Actual scoring logic
def calculate_final_score(metrics, adjustments):
    base_score = metrics['mean_clean'] * evaluation_weights['base']
    bonus_score = metrics['count_clean'] * 5 * adjustments['efficiency'] * evaluation_weights['bonus']
    penalty = metrics['outlier_count'] * 3 * evaluation_weights['penalty']
    stability_factor = adjustments['stability']
    
    # Intermediate irrelevant calculation
    hypothetical_max = (metrics['mean_clean'] + 10) * adjustments['efficiency']
    decay_correction = hypothetical_max * 0.05  # unused in final logic
    
    raw_score = (base_score + bonus_score - penalty) * stability_factor
    return int(round(raw_score))

final_score = calculate_final_score(stats, modifiers)
print(f"Target result: {final_score}")