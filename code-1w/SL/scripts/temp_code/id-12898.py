import math

# Simulated sensor data processing pipeline with red herrings
def analyze_readings(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    squared_devs = [(x - sum(filtered)/len(filtered))**2 for x in filtered]
    variance = sum(squared_devs) / len(squared_devs)
    return variance

# Legacy function - unused but looks important
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [math.tanh((x - mean_val)/10) for x in data]

# Core transformation logic
def transform_signal(signal_sequence, factor=1.5):
    shifted = [int(x * factor) for x in signal_sequence]
    packed = list(zip(shifted[::2], shifted[1::2]))
    processed = [a ^ b for a, b in packed]  # XOR pairs
    return processed

# Advanced metric calculator with distractors
def compute_envelope(samples):
    envelope = []
    temp_log = []
    for i, val in enumerate(samples):
        if i % 3 == 0:
            temp_log.append(math.log(abs(val) + 1))
        elif i % 3 == 1:
            temp_log.append(math.sqrt(abs(val)))
        else:
            temp_log.append(val / 2)
    # Real computation path
    magnitude = sum(abs(x) for x in samples)
    penalty = len([x for x in samples if x < 0])
    return magnitude - penalty

# Main diagnostic processor
def process_metrics(data_chunk, base):
    # Irrelevant set operations (distractor)
    unique_vals = set(data_chunk)
    base_set = set(base)
    intersection_size = len(unique_vals & base_set)
    union_size = len(unique_vals | base_set)
    jaccard = intersection_size / union_size if union_size else 0
    
    # Dummy lambda that does nothing critical
    adjust_weight = lambda w: w * 1.7 if w > 5 else w * 0.8
    weights = [adjust_weight(jaccard)]
    
    # Actual relevant logic
    total_power = sum(x*x for x in data_chunk)
    reference_score = sum(base)
    trend = total_power - reference_score
    
    # More distraction: unused complex calculation
    spectral_density = []
    for i in range(len(data_chunk)):
        component = 0
        for j in range(1, 5):
            component += math.sin(i*j) * data_chunk[i]
        spectral_density.append(component)
    
    # Critical early return trap (never reached due to condition)
    if len(data_chunk) < 5:
        return -999
        extra_analysis = [x for x in data_chunk if x % 2 == 0]
        return sum(extra_analysis)

    # Real result
    return int(trend / (1 + jaccard))

# Initialization parameters (some irrelevant)
baseline_config = {
    'threshold': 23.5,
    'gain': 1.8,
    'window_size': 7
}

raw_sensor_data = [12, -7, 4, 19, 3, 8, -2, 11]
baseline = [2, 4, 6, 8, 10]

# Unused but plausible-looking preprocessing
filtered_stream = list(filter(lambda x: x >= 0, raw_sensor_data))
enumerated_pairs = list(enumerate(filtered_stream, start=1))
decoy_matrix = [[i*j for j in range(3)] for i in range(len(filtered_stream))]

# Transform data using core function
transformed_data = transform_signal(raw_sensor_data, factor=baseline_config['gain'])

# Additional distraction: fake analysis chain
shadow_copy = transformed_data.copy()
for idx, val in enumerate(shadow_copy):
    if val > 10:
        shadow_copy[idx] = val >> 2
    else:
        shadow_copy[idx] = val << 1

# Another decoy metric
def calculate_cohesion(seq):
    if not seq:
        return 0
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 3)

cohesion_index = calculate_cohesion(transformed_data)

# Real adjustment factor derived from multiple sources (but only some matter)
deflection = analyze_readings(raw_sensor_data)
scaling_hint = compute_envelope(transformed_data)
adjustment_factor = int(scaling_hint / 10)  # Only this part is used

# Final diagnostic - the target execution point
final_diagnostic = process_metrics(transformed_data, baseline) + adjustment_factor

print(f"Result: {final_diagnostic}")