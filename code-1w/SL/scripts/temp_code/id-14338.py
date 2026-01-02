def analyze_performance(records):
    total_entries = len(records)
    success_count = 0
    temp_multiplier = 1.0
    cumulative_offset = 0

    for record in records:
        if record['status'] == 'success':
            success_count += 1
            cumulative_offset += record['value'] % 7
        else:
            temp_multiplier *= 0.95  # Irrelevant to final score

    success_rate = success_count / total_entries if total_entries > 0 else 0
    return success_rate, cumulative_offset


def calculate_complex_metric(data_list):
    metric = 0
    for item in data_list:
        metric += abs(item['value']) ** 0.5
    return metric  # Computed but not used in final result


def build_stats_map(raw_data):
    stats = {}
    for entry in raw_data:
        key = entry['category']
        if key not in stats:
            stats[key] = {'count': 0, 'sum': 0}
        stats[key]['count'] += 1
        stats[key]['sum'] += entry['value']
    return stats

# Main execution
raw_input_data = [
    {'category': 'A', 'value': 12, 'status': 'success'},
    {'category': 'B', 'value': -8, 'status': 'failure'},
    {'category': 'A', 'value': 15, 'status': 'success'},
    {'category': 'C', 'value': 5, 'status': 'success'},
    {'category': 'B', 'value': 20, 'status': 'success'},
    {'category': 'C', 'value': -3, 'status': 'failure'}
]

# Intermediate processing with distractors
size_factor = len(raw_input_data) * 0.1
offset_buffer = sum(d['value'] for d in raw_input_data if d['status'] == 'failure')
dummy_metric = calculate_complex_metric(raw_input_data)

# Build main structure
stats_dict = build_stats_map(raw_input_data)

# Extract relevant values
success_rate, offset_correction = analyze_performance(raw_input_data)
base_score = 0
for cat, data in stats_dict.items():
    base_score += data['sum'] // data['count']

# Apply correction based on success rate
if success_rate >= 0.5:
    base_score += 10
else:
    base_score -= 5

# Final computation
final_score = base_score + int(offset_correction)

# Additional irrelevant state tracking
snapshot_log = {
    'timestamp': 1678886400,
    'processed_items': len(raw_input_data),
    'final_score_snapshot': final_score
}

Result: {final_score}