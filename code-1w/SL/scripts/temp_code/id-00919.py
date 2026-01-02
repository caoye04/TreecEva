import itertools

# Simulated sensor data processing with performance evaluation
raw_data_stream = [0.85, 0.92, 0.78, 0.96, 0.88, 0.73, 0.91]
decoy_data = [x ** 2 for x in raw_data_stream if x > 1]  # Dead path: no elements satisfy condition

# Irrelevant transformation chain
temp_buffer = ''.join([str(int(x * 100)) for x in raw_data_stream])
split_chunks = temp_buffer.split('88')
reshaped = [int(chunk) for chunk in split_chunks if len(chunk) > 0]
filtered_noise = list(itertools.dropwhile(lambda x: x < 90, reshaped))  # Misleading intermediate result

# Actual metric computation setup
baseline_shift = sum([x for x in raw_data_stream if x > 0.85])
penalty_factor = len([x for x in raw_data_stream if x < 0.8])
adjusted_baseline = baseline_shift - (penalty_factor * 0.1)

# Distractor: complex but unused statistical calculation
mean_val = sum(raw_data_stream) / len(raw_data_stream)
variance = sum((x - mean_val) ** 2 for x in raw_data_stream) / len(raw_data_stream)
std_deviation = variance ** 0.5
deviation_normalized = [round((x - mean_val) / std_deviation, 3) for x in raw_data_stream]

# Red herring function that's never called
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
    return trend_score * 0.05

# Unused bitwise manipulation (distractor)
flag_register = 0b1010
flag_register ^= 0b1100
flag_register |= 0b0011
status_mask = flag_register & 0b1111

# Real processing begins here — hidden among noise
raw_results = [x * 100 for x in raw_data_stream]  # Scale to percentage

# Weighting scheme obscured by irrelevant mappings
all_metrics = {'precision': 0.91, 'recall': 0.87, 'f1': 0.89}
metric_names = list(all_metrics.keys())
metric_weights = {name: 0.35 for name in metric_names}
metric_weights['f1'] = 0.3  # Override

# Decoy dictionary operation
shadow_copy = {k: v * 1.1 for k, v in all_metrics.items()}

# Core logic buried in conditional structure
def apply_weighting(metrics, weights, values):
    total = 0.0
    for i, key in enumerate(metrics):
        if key == 'f1':
            total += weights[key] * values[i % len(values)]
        elif key == 'precision':
            total += weights[key] * (values[(i+2) % len(values)] + 0.5)
        else:
            total += weights[key] * values[(i+1) % len(values)]
    return total

# Another red herring: string slicing distraction
data_string = "sensor_log_2024"
segment_key = data_string[7:11]  # 'log_' — unused
suffix_check = data_string.endswith('24') and data_string.startswith('sensor')

# Key statement embedded in setup
evaluation_matrix = list(itertools.product([0.35], [85, 87, 89]))
final_score = 0

# Actual answer derivation via non-obvious indexing and weighting
effective_values = [raw_results[1], raw_results[3], raw_results[5]]  # 92, 96, 73
final_score = apply_weighting(metric_names, metric_weights, effective_values)

# Final adjustment based on baseline (ties back to earlier calculation)
final_score += adjusted_baseline

print(f"Result: {final_score}")