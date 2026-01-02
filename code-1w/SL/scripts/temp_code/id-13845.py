def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Semi-relevant filtering
    passed = [m for m in metrics if m >= thresholds['min_pass']]
    excellence_count = sum(1 for m in metrics if m >= thresholds['excellence'])

    # Misleading accumulation (not used in final result)
    cumulative_sum = 0
    temp_values = []
    for i, val in enumerate(passed):
        cumulative_sum += val * (i + 1)
        temp_values.append(cumulative_sum)

    # Core logic hidden among distractions
    valid_entries = 0
    penalty = 0
    for i, m in enumerate(metrics):
        if m < thresholds['min_pass']:
            penalty += thresholds['penalty_per_failure']
        else:
            valid_entries += 1

    base_score = valid_entries * thresholds['base_per_entry']
    bonus = excellence_count * thresholds['bonus_per_excellence'] if excellence_count >= 2 else 0

    # Use of zip and enumerate together (required Python features)
    adjustments = 0
    for idx, (raw, norm) in enumerate(zip(metrics, normalized)):
        if raw > thresholds['min_pass'] and idx % 2 == 0:
            adjustments += norm * 0.05

    return base_score + bonus - penalty + int(adjustments)


def calculate_final_score(data_str, config):
    # String processing distraction
    raw_parts = data_str.strip().split(',')
    parsed_metrics = [int(p.replace('M:', '')) for p in raw_parts if p.startswith('M:')]
    
    # Unused but plausible parsing
    tags = [t for t in raw_parts if t.startswith('T:')]
    metadata_pairs = [t.split(':') for t in tags]
    meta_dict = {k: v for k, v in metadata_pairs}

    # Slicing distraction
    reversed_slice = parsed_metrics[::-1]
    mid_section = reversed_slice[1:4] if len(reversed_slice) > 4 else []

    # Actual calculation uses only parsed_metrics and config
    score = analyze_performance(parsed_metrics, config)
    
    # Secondary adjustment
    if len(parsed_metrics) >= config['stability_window']:
        recent = parsed_metrics[-config['stability_window']:]
        if all(r >= config['min_pass'] for r in recent):
            score += config['stability_bonus']
    
    return score

# Main execution
configuration = {
    'min_pass': 60,
    'excellence': 90,
    'base_per_entry': 15,
    'bonus_per_excellence': 20,
    'penalty_per_failure': 10,
    'stability_window': 3,
    'stability_bonus': 25
}

data_input = "M:75,M:45,M:92,M:88,T:source,AI,T:region,US,M:95"

intermediate_list = [x for x in range(10)]  # Dead code path (not used)
shadow_value = sum(i**2 for i in intermediate_list)  # Distractor computation

final_score = calculate_final_score(data_input, configuration)
print(f"Result: {final_score}")