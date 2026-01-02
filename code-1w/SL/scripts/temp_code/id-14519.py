def analyze_performance(metrics):
    base_score = 0
    bonus_factor = 1.2
    penalty_factor = 0.8
    intermediate_sum = 0
    temp_result = set()

    for key, values in metrics.items():
        if 'response' in key:
            avg = sum(values) / len(values)
            if avg > 50:
                base_score += avg * bonus_factor
                temp_result.add(avg)
            else:
                base_score += avg * penalty_factor
        elif 'error_rate' in key:
            max_error = max(values)
            base_score -= max_error * 2
        else:
            # Dead code path – never executed due to current input
            fallback = min(values) // 10
            base_score += fallback

    return base_score, temp_result


def normalize_entries(raw_entries):
    normalized = []
    total_entries = len(raw_entries)
    scale_factor = 100 / total_entries if total_entries > 0 else 1
    
    for entry in raw_entries:
        scaled = entry * scale_factor
        normalized.append(round(scaled))
    
    # Irrelevant transformation
    reversed_normalized = [n for n in reversed(normalized)]
    return normalized


def calculate_final_score(data_dict):
    score = 0
    adjustments = []
    history_log = []  # Unused tracking variable

    keys = list(data_dict.keys())
    keys.sort()  # Unnecessary sort

    for k in keys:
        item = data_dict[k]
        if isinstance(item, list) and len(item) > 0:
            item_set = set(item)
            unique_count = len(item_set)
            range_val = max(item) - min(item)
            
            # Relevant computation
            contribution = unique_count * (range_val % 7)
            adjustments.append(contribution)
            
            # Distractor: complex but unused dict op
            stats_snapshot = {
                'span': range_val,
                'peak': max(item),
                'floor': min(item),
                'flagged': True if range_val > 20 else False
            }
            history_log.append(stats_snapshot)

    # Final aggregation
    if adjustments:
        raw_total = sum(adjustments)
        modifier = len(adjustments) + (4 if raw_total > 100 else 2)
        score = raw_total // modifier
    
    return score

# Main execution
raw_metrics = {
    'response_times': [45, 60, 60, 30, 75],
    'throughput_data': [20, 25, 25, 30],
    'error_rate_1': [5, 12, 8],
    'redundant_key': [10, 10, 10]  # Will be processed as generic list
}

# Step 1: Analyze performance (uses dict and set ops)
base_score, _ = analyze_performance(raw_metrics)

# Step 2: Normalize unrelated metric (distractor)
dummy_entries = [10, 20, 30, 40]
normalized_dummy = normalize_entries(dummy_entries)

# Step 3: Prepare data for final scoring
processed_data = {}
for key, val in raw_metrics.items():
    if 'response' in key or 'throughput' in key:
        processed_data[key] = [v for v in val if v >= 25]  # Filtering
    else:
        processed_data[key] = val[:]  # Copy

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")