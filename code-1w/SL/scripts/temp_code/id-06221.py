import itertools

# Simulated sensor data stream with mixed validity
raw_samples = [105, None, 203, 198, None, 201, 95, 110, 207, 190]

def validate_sample(x):
    return isinstance(x, int) and 100 <= x <= 200

def correct_anomaly(val):
    if val < 100:
        return 100
    elif val > 200:
        return 200
    return val

# Data filtering and correction pipeline
filtered_data = list(filter(lambda x: x is not None, raw_samples))
corrected_data = [correct_anomaly(x) for x in filtered_data]

# Irrelevant transformation: frequency analysis (distraction)
frequency_map = {}
for freq_key in corrected_data:
    frequency_map[freq_key] = frequency_map.get(freq_key, 0) + 1
mode_value = max(frequency_map, key=lambda k: frequency_map[k])

# Compute rolling average for stability check (semi-relevant)
window_size = 3
rolling_averages = [
    sum(corrected_data[i:i+window_size]) / window_size
    for i in range(len(corrected_data) - window_size + 1)
]
stability_deviation = sum(abs(avg - 150) for avg in rolling_averages)

# Core metric computation begins here
valid_range_count = sum(1 for x in corrected_data if 100 <= x <= 200)
total_energy = sum(corrected_data)
base_efficiency = total_energy / len(corrected_data)

# Conditional adjustment based on pattern symmetry (distractor logic)
data_pairs = list(itertools.combinations(corrected_data, 2))
symmetric_pairs = list(filter(lambda p: abs(p[0] + p[1] - 300) < 10, data_pairs))
ad_hoc_factor = len(symmetric_pairs) / 100 if symmetric_pairs else 0.0

# Efficiency model with weighted components
weight_a = 0.6 if valid_range_count > 5 else 0.4
weight_b = 0.4 - ad_hoc_factor  # Slight penalty or boost

# Final processing function
def process_metrics(data):
    nonlocal base_efficiency, weight_a, weight_b
    peak_load = max(data)
    normalized_peak = peak_load / 200.0
    efficiency_score = (base_efficiency * weight_a) + (normalized_peak * 100 * weight_b)
    
    # Dead code branch (red herring)
    if False:
        backup_calc = sum(data) * 0.01
        efficiency_score = max(efficiency_score, backup_calc)
    
    # Key assignment point
    final_result = round(efficiency_score, 4)
    return final_result

# Execution point of interest
data_stream = corrected_data
final_output = process_metrics(data_stream)
efficiency_score = final_output
print(f"Result: {efficiency_score}")