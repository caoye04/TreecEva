def analyze_trends(values):
    trend_data = {}
    avg = sum(values) / len(values)
    trend_data['mean'] = avg
    trend_data['deviations'] = [v - avg for v in values]
    trend_data['variance'] = sum(d**2 for d in trend_data['deviations']) / len(values)
    return trend_data

values = [12, 15, 10, 8, 14, 16, 11]

# Extraneous computation - not directly used
temp_analysis = analyze_trends([x * 1.1 for x in values])
smoothed = [round(v * 0.95, 2) for v in values]

# Weight dictionary with red herring keys
decay_weights = {
    'base': 0.3,
    'bonus': 0.1,
    'penalty': -0.05,
    'hidden_adjustment': 0.02,  # Not actually used
    'multiplier': 1.2
}

active_flags = [True, False, True]
flag_state = any(active_flags) and not all(active_flags)

# Core data and processing
weights = {'w1': 0.4, 'w2': 0.6}
data = {'input_a': 50, 'input_b': 30}

# Distractor: unused transformation
dummy_transform = {k: v * 1.5 for k, v in data.items()}

intermediate_result = data['input_a'] * weights['w1'] + data['input_b'] * weights['w2']

# Simulate conditional adjustment (always triggers due to flag_state)
if len(values) > 5:
    intermediate_result *= decay_weights['multiplier']

# Another distractor block: dead logic path
temp_offset = 0
if False:  # Dead code
    temp_offset = sum(smoothed[:3]) - temp_analysis['mean']

adjusted_base = intermediate_result + temp_offset

# Final processing function with dictionary usage
def process_metrics(inputs, w_map):
    result = 0
    mapping = {'input_a': 'w1', 'input_b': 'w2'}
    for key, val in inputs.items():
        weight_key = mapping[key]
        result += val * w_map[weight_key]
    if inputs['input_a'] > 40:
        bonus = 5
        # Nested conditional with redundant check
        if bonus > 0:
            sanity_check = sum(w_map.values()) > 0
            if sanity_check:
                result += bonus * 1.2
    return int(result)

final_score = process_metrics(data, weights)
print(f"Result: {final_score}")