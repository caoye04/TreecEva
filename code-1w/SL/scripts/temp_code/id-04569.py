import math

# Simulated sensor fusion and data optimization system
def analyze_readings(raw_values):
    filtered = [x for x in raw_values if x > 0]
    normalized = [v / sum(filtered) for v in filtered]
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)
    return normalized, entropy

# Legacy function – irrelevant but looks important
def calculate_legacy_metric(data):
    total = 0
    for i in range(len(data)):
        total += (i + 1) * data[i] ** 2
    return total // 3 if total > 100 else total

# Core transformation pipeline
def transform_sequence(seq):
    shifted = [(x << 1) ^ 3 for x in seq]
    mapped = list(map(lambda y: y + 5 if y % 2 == 0 else y - 2, shifted))
    return [z for z in mapped if z % 3 == 0]

# Data calibration with red herring computations
def calibrate_buffer(input_data):
    temp_store = {}
    running_sum = 0
    decoy_accum = 0

    for idx, val in enumerate(input_data):
        temp_store[f'entry_{idx}'] = val * 1.5 + 2.3
        running_sum += val
        # Distractor: complex-looking but unused calculation
        decoy_accum += int((val ** 2 + idx) % 7) * 13

    avg_val = running_sum / len(input_data) if input_data else 0
    
    # Irrelevant conditional block (never alters output)
    if avg_val > 10:
        adjustment = sum([v // 4 for v in input_data if v > 5])
        avg_val -= adjustment * 0.1

    return avg_val

# Main processing logic
raw_sensor_data = [7, 2, 9, 4, 5]
processed_batch = transform_sequence(raw_sensor_data)

# Multiple assignments and distractors
baseline, info_entropy = analyze_readings(processed_batch)
duplicate_entropy_calc = -sum(math.log(x) for x in baseline if x > 0)  # Unused

intermediate_stats = {
    'count': len(processed_batch),
    'peak': max(processed_batch),
    'floor': min(processed_batch),
    'total': sum(processed_batch)
}

# Decoy structure with misleading metrics
device_profile = {
    'calibration': calibrate_buffer(processed_batch),
    'version': 'X2-alpha',
    'metrics': [
        {'type': 'A', 'value': intermediate_stats['peak'] * 2},
        {'type': 'B', 'value': intermediate_stats['floor'] - 1}
    ]
}

# Conditional expression mixing relevant and irrelevant paths
efficiency_flag = 'high' if intermediate_stats['peak'] > 20 else 'low'
scale_factor = 3 if efficiency_flag == 'high' else 2

# Key computation chain
adjusted_values = [v * scale_factor for v in processed_batch]
consolidated_data = {
    'items': adjusted_values,
    'size': len(adjusted_values),
    'checksum': sum(v & 7 for v in adjusted_values),
    'flag': efficiency_flag
}

# Final processing with lambda and dictionary op
process_results = lambda data: {
    **data,
    'optimized_score': sum(data['items']) // data['size'] if data['size'] > 0 else 0
}

final_output = process_results(consolidated_data)
optimized_score = final_output['optimized_score']

# Misleading print statements (distractors)
# print(f'Debug entropy: {info_entropy}')
# print(f'Decoherence level: {decoy_accum}')

Result: {optimized_score}