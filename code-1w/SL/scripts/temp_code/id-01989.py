def analyze_metrics(data_points):
    if not data_points:
        return 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data_points) for x in data_points]
    squared_errors = [(x - 0.5)**2 for x in normalized]
    avg_error = sum(squared_errors) / len(squared_errors)
    
    # Real logic starts here
    raw_total = sum(data_points)
    adjustment_factor = 0.85 if raw_total > 30 else 1.15
    
    return raw_total * adjustment_factor


def calculate_performance(base, mods):
    # Semi-relevant transformation
    modified_base = base * (1 + sum(m['delta'] for m in mods if m['active']))
    
    # Distraction: complex filtering with no impact
    filtered_mods = [m for m in mods if m['type'] == 'enhancement' and m['level'] > 1]
    temp_boost = len(filtered_mods) * 0.05
    
    # Actual decision logic
    multiplier = 1.2 if any(m['critical'] for m in mods) else 0.9
    score = modified_base * multiplier
    
    # Conditional expression (required feature)
    score = score if score >= 0 else abs(score) * 0.5
    
    # Dead code path (distractor)
    if temp_boost > 1.0:
        score *= 1.1  # Never reached
    
    return int(score)

# Main execution
baseline_data = [4, 7, 9, 5, 8]

# Irrelevant statistical summary
mean_val = sum(baseline_data) / len(baseline_data)
std_dev = (sum((x - mean_val)**2 for x in baseline_data) / len(baseline_data))**0.5

# Key computation chain
baseline = analyze_metrics(baseline_data)

adjustments = [
    {'delta': 0.1, 'active': True, 'type': 'enhancement', 'level': 2, 'critical': False},
    {'delta': 0.05, 'active': True, 'type': 'correction', 'level': 3, 'critical': True},
    {'delta': -0.02, 'active': False, 'type': 'enhancement', 'level': 1, 'critical': False}
]

# Extra unused variable (distractor)
intermediate_result = [x * 1.5 for x in baseline_data if x % 2 == 0]

final_score = calculate_performance(baseline, adjustments)
print(f"Target result: {final_score}")