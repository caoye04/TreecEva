def analyze_trends(data, config):
    trend_indices = []
    adjustment_factor = config.get('factor', 1.0)
    baseline = sum(data) / len(data) if data else 0
    
    temp_buffer = [x * adjustment_factor for x in data]
    normalized = [round((x - baseline) / baseline * 100, 2) for x in temp_buffer]

    for i, val in enumerate(normalized):
        if val > 5:
            trend_indices.append(i)
    
    return trend_indices


def validate_inputs(entries):
    valid = []
    scores = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if 'value' in entry and 0 <= entry['value'] <= 100:
            valid.append(entry)
            score = entry['value'] ** 0.5
            scores.append(score)
    return valid, scores

def process_performance(metrics, thresholds):
    # Unpack metrics using dictionary operations
    raw_values = metrics.get('values', [])
    weights = metrics.get('weights', [1] * len(raw_values))
    
    # Irrelevant preprocessing (distractor)
    filtered_pairs = [(v, w) for v, w in zip(raw_values, weights) if v > 10]
    backup_state = {i: v*w for i, (v, w) in enumerate(filtered_pairs)}
    
    # Core computation with modular arithmetic and conditional logic
    total = 0
    penalty = 0
    for idx, (val, weight) in enumerate(zip(raw_values, weights)):
        contribution = val * weight
        if idx % 3 == 0:
            contribution = (contribution % 7) * 2
        elif idx % 3 == 1:
            contribution = max(contribution - 15, 5)
        else:
            contribution = min(contribution, 40)
        
        if contribution > thresholds.get('limit', 30):
            penalty += thresholds.get('penalty', 3)
        
        total += contribution

    # Sorting as part of state transformation (semi-relevant)
    sorted_vals = sorted([x * 0.9 for x in raw_values])
    mid_index = len(sorted_vals) // 2
    median_adjusted = sorted_vals[mid_index] if sorted_vals else 0

    # Final calculation
    stability_bonus = 10 if abs(median_adjusted - total / len(raw_values)) < 20 else 5
    final_score = int(total - penalty + stability_bonus)
    
    # Dead code path (distractor)
    if False:
        fallback = sum(backup_state.values())
        final_score = fallback

    return final_score

# Main execution context
entries_list = [
    {'value': 25}, {'value': 45}, {'value': 60}, {'value': 80}, {'value': 33}
]

valid_entries, computed_scores = validate_inputs(entries_list)

raw_data_stream = [item['value'] for item in valid_entries]
config_settings = {'factor': 1.1}

indices_of_interest = analyze_trends(raw_data_stream, config_settings)

metrics_package = {
    'values': [24, 48, 62, 75, 30],
    'weights': [1, 2, 1, 3, 2]
}
thresholds_config = {
    'limit': 35,
    'penalty': 4
}

final_score = process_performance(metrics_package, thresholds_config)
print(f"Target result: {final_score}")