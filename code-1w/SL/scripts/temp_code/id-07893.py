from collections import defaultdict, Counter
import math

# Simulated sensor array data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    processed = []
    noise_floor = 0.003
    scaling_factor = 2.718
    for val in raw_readings:
        if abs(val) < noise_floor:
            continue
        corrected = (val ** 2) * scaling_factor
        if corrected > 100:
            corrected = 100 + math.log(corrected - 100 + 1)
        processed.append(round(corrected, 4))
    return processed

# Irrelevant auxiliary function - dead path
def deprecated_filter(x):
    return [i for i in x if i % 3 == 0]

# Core transformation with red herring operations
def transform_signal(data_seq):
    shifted = [(x * 1.5) + 2 for x in data_seq]
    inverted = [abs(1 / x) if x != 0 else 0 for x in shifted][-10:]
    # Meaningless statistical distraction
    stats_summary = {
        'max': max(inverted),
        'min': min(inverted),
        'range': max(inverted) - min(inverted),
        'median_guess': sorted(inverted)[len(inverted)//2]
    }
    # Actual relevant output
    return [int(x * 10) / 10.0 for x in shifted[:15]]

# Misleading complexity: unused recursive structure
def recursive_denoise(signal, depth=0):
    if depth >= 3 or len(signal) < 2:
        return signal
    reduced = [signal[i] for i in range(0, len(signal), 2)]
    return recursive_denoise(reduced, depth + 1)

# Real processing step disguised among decoys
def generate_threshold_map(values):
    base_threshold = sum(values) / len(values)
    variation = math.sqrt(sum((x - base_threshold) ** 2 for x in values) / len(values))
    # Decoy dictionary entries
    return {
        'nominal': base_threshold,
        'tolerance_band': variation,
        'upper_limit': base_threshold + variation * 1.5,
        'lower_limit': base_threshold - variation * 0.8,
        'bogus_metric_x': sum(v % 1 for v in values),
        'dummy_scale_y': len([v for v in values if v > 1])
    }

# Critical analysis function — actual logic path
def analyze_pattern(dataset, config):
    count_high = 0
    cumulative_shift = 0
    for item in dataset:
        if item > config['upper_limit']:
            count_high += 1
            cumulative_shift += item - config['nominal']
    if count_high == 0:
        return config['tolerance_band'] * 100
    else:
        return int(cumulative_shift / count_high * 100) // 1  # Discrete impact score

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == '__main__':
    # Raw input data
    sensor_inputs = [0.002, -0.001, 4.1, 5.3, 6.8, 4.2, 5.9, 7.1, 6.3, 5.0, 5.5, 6.0, 7.4, 6.7, 5.8, 6.2]
    
    # Step 1: Preprocess (filter noise and scale)
    clean_data = preprocess_readings(sensor_inputs)
    
    # Step 2: Transform signal — produces working dataset
    transformed_data = transform_signal(clean_data)
    
    # Distraction: unused derived set
    sparse_sample = recursive_denoise(transformed_data)
    
    # Step 3: Build configuration map from subset
    threshold_map = generate_threshold_map(transformed_data[::2])
    
    # Irrelevant sorting distraction
    sorted_pairs = sorted(Counter(transformed_data).items(), key=lambda x: x[1], reverse=True)
    
    # Step 4: Perform final diagnostic analysis
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")