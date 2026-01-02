import itertools

# Simulated sensor data stream with noise and redundant readings
data_stream = [15, 0, 23, -7, 44, 0, 19, 31, 8, 0, 11, 56, -14, 22, 9]

# Irrelevant metadata (distractor)
sensor_specs = {
    'model': 'SEN-X9',
    'calibration': [0.98, 1.02],
    'units': 'mV',
    'version': 2.1
}

# Redundant transformation (dead code path)
def transform_legacy(signal):
    return [x * 1.05 for x in signal if x > 0]

# Unused helper function (misleading)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Simulate corrupted packets (irrelevant filtering)
corrupted_indices = {5, 10, 15}
valid_data = [data_stream[i] for i in range(len(data_stream)) if i not in corrupted_indices]

# Real processing begins here
raw_magnitudes = [abs(x) for x in data_stream]  # Remove sign for magnitude analysis

# Filter out zero values considered as inactive sensors
non_zero = list(filter(lambda x: x != 0, raw_magnitudes))

# Apply dynamic threshold: median of top 60% values
sorted_vals = sorted(non_zero)
threshold_index = len(sorted_vals) - len(sorted_vals) // 3
adaptive_threshold = sorted_vals[threshold_index] if threshold_index >= 0 else sorted_vals[0]

# Additional distraction: frequency analysis using itertools (unused)
frequency_map = {k: len(list(v)) for k, v in itertools.groupby(sorted(non_zero))}
dominant_magnitude = max(frequency_map, key=lambda x: frequency_map[x])

# Focus on high-energy signals above adaptive threshold
filtered_data = [x for x in non_zero if x > adaptive_threshold]

# Secondary distraction: pairing signals (not used in final output)
paired_combinations = list(itertools.combinations(filtered_data, 2))
avg_pair_product = sum(a * b for a, b in paired_combinations) / len(paired_combinations) if paired_combinations else 0

# Core logic: count how many times consecutive values increase
increasing_runs = 0
for i in range(1, len(filtered_data)):
    if filtered_data[i] > filtered_data[i-1]:
        increasing_runs += 1

# Introduce side computation with string encoding (completely irrelevant)
status_flag = ''.join(['1' if x % 2 else '0' for x in filtered_data])
checksum_str = status_flag[::-1].upper() + '_CHK'

# Main processing function with closure (key concept)
def process_signals(signals, limit):
    base_offset = 3
    
    def enhance(x):
        return x + base_offset if x < limit * 1.5 else x - base_offset
    
    enhanced = [enhance(val) for val in signals]
    
    # Extra distraction: reverse mapping (unused)
    inverted_map = {i: val for i, val in enumerate(reversed(enhanced))}
    
    # Actual result computation
    total_energy = sum(enhanced)
    peak_count = len([x for x in enhanced if x > limit])
    stability_score = abs(len(enhanced) - increasing_runs)  # Uses outer scope variable
    
    # Final deterministic formula
    result = (total_energy // (peak_count or 1)) - stability_score + base_offset
    return result

# Execute critical statement
final_output = process_signals(filtered_data, threshold=adaptive_threshold)

# Print required result
print(f"Result: {final_output}")