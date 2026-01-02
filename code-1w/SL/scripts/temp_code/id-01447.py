def analyze_performance(records):
    base_multiplier = 1.5
    temp_offset = 0.87
    cumulative = 0
    adjustments = []
    
    for i, record in enumerate(records):
        index_weight = i + 1
        raw_value = record['value'] * base_multiplier
        if record['flag']:
            raw_value += temp_offset
        cumulative += raw_value
        adjustments.append(raw_value * 0.1)
    
    return cumulative, adjustments


def calculate_rating(metrics, factor):
    rating = 0
    penalty = 0.05
    temp_sum = 0
    
    for idx, (key, val) in enumerate(zip(metrics.keys(), metrics.values())):
        temp_sum += val * (idx + 1)
        if val < 10:
            penalty += 0.01
    
    scaled = temp_sum * factor
    intermediate_result = scaled - penalty * 100
    
    # Dead code path - never executed due to fixed input
    if len(metrics) > 100:
        fallback = sum(metrics.values())
        return fallback
    
    rating = int(intermediate_result + 0.5)
    return rating

# Main execution
log_data = [
    {'value': 12, 'flag': True},
    {'value': 8, 'flag': False},
    {'value': 15, 'flag': True},
    {'value': 7, 'flag': True}
]

quality_metrics = {
    'clarity': 12,
    'consistency': 8,
    'efficiency': 15,
    'readability': 7
}

efficiency_factor = 1.2

# Irrelevant helper
def dummy_util(data):
    return [x**2 for x in range(len(data))]

dummy_results = dummy_util(log_data)

# Unused transformation
shifted_values = [d['value'] + 3 for d in log_data if d['flag']]

# Key analysis step
aggregate, deltas = analyze_performance(log_data)

# Secondary metric (unused in final calculation)
baseline = sum(d['value'] for d in log_data)

# Critical statement
final_score = calculate_rating(quality_metrics, efficiency_factor)

print(f"Result: {final_score}")