def analyze_metrics(data, threshold=10):
    count = 0
    temp_sum = 0
    outlier_count = 0
    for val in data:
        if val > threshold * 2:
            outlier_count += 1
        if val > threshold:
            count += 1
            temp_sum += val
    average_above = temp_sum / count if count else 0
    return average_above, count


def calculate_risk_factor(level, history):
    risk = 0
    for h in history:
        if h < level:
            risk += 0.1
    return risk if risk > 0 else 0.05


def evaluate_performance(records):
    base_values = [r['value'] for r in records]
    adjustments = [r['adj'] for r in records if 'adj' in r]
    adjusted_total = sum(base_values)
    
    # Irrelevant intermediate computation (distractor)
    peak_value = max(base_values) if base_values else 0
    normalized = [v / peak_value for v in base_values if peak_value > 0]
    pseudo_index = sum(1 for n in normalized if n > 0.5)
    
    # Actual logic path
    valid_entries = [v for v in base_values if v >= 5]
    if len(valid_entries) < 3:
        return 0
    
    avg_valid = sum(valid_entries) / len(valid_entries)
    
    # Secondary adjustment using helper logic
    history_flags = [1 if r.get('flag') else 0 for r in records]
    flag_density = sum(history_flags) / len(history_flags) if history_flags else 0
    
    # Distractor: unused complex list comprehension
    derived_weights = [0.1 * (i + 1) ** 0.5 for i in range(len(records))]
    weight_moment = sum([i * w for i, w in enumerate(derived_weights)]) if derived_weights else 0
    
    # Core scoring logic
    raw_score = avg_valid * 10
    penalty = 2 if flag_density > 0.7 else 0
    final_score = int(raw_score - penalty)
    
    # Additional irrelevant state tracking
    status_log = []
    status_log.append(f'Started with {len(records)} entries')
    status_log.append(f'Peak was {peak_value}')
    
    return final_score

# Main execution
records_data = [
    {'value': 8, 'flag': True},
    {'value': 12, 'flag': False},
    {'value': 7, 'adj': 1},
    {'value': 15, 'flag': True},
    {'value': 6}
]

# Analyze subset first (side calculation)
data_subset = [r['value'] for r in records_data if r['value'] > 9]
analyze_metrics(data_subset, threshold=8)

# Primary evaluation
final_score = evaluate_performance(records_data)
print(f"Result: {final_score}")