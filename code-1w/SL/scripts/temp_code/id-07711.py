from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_stream(raw_readings):
    processed = []
    temp_buffer = []
    for val in raw_readings:
        if val < 0:
            temp_buffer.append(abs(val))
        elif val % 3 == 0:
            processed.append(val ** 0.5)
        else:
            processed.append(val * 2)
    return processed

# Irrelevant transformation: time-domain shift (unused later)
def time_shift_signal(signal, offset=1):
    return signal[offset:] + signal[:offset]

# Core transformation function used in computation
def transform_signal(x):
    if x < 10:
        return (x ** 2) + 1
    elif x < 20:
        return (x * 3) - 5
    else:
        return int(x / 2)

# Data normalization (distractor - not used in final path)
def normalize_readings(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val * 100, 2) for x in data]

# Main pattern analysis with multiple logic layers
def analyze_pattern(seq, reference):
    history_map = defaultdict(int)
    score_cache = []
    
    # Step 1: Count frequencies of differences
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))] if len(seq) > 1 else [0]
    diff_counts = Counter(diffs)
    
    # Step 2: Apply masking based on reference cycle (key logic)
    masked_values = []
    for i, val in enumerate(seq):
        mask = reference[i % len(reference)]
        if i % 3 == 0:
            masked_values.append(val ^ mask)  # Bitwise XOR distraction
        elif i % 4 == 0:
            masked_values.append(val | (mask >> 1))
        else:
            masked_values.append(val + mask)  # Actual path contributing to result
    
    # Step 3: Filter and aggregate relevant components
    filtered = [v for v in masked_values if v % 2 == 1]  # Keep only odd values
    
    # Step 4: Accumulate diagnostic metric
    accumulator = 0
    for idx, item in enumerate(filtered):
        if idx % 2 == 0:
            accumulator += item * (idx + 1)
        else:
            accumulator -= item // (idx + 1)

    # Step 5: Apply decay factor from secondary sequence (decoy calculation)
    decay_factor = 0.0
    for d in diffs:
        if d > 5:
            decay_factor += math.log(d, 2)
    # But decay is NOT applied — intentional misdirection

    # Step 6: Final adjustment using hidden rule
    adjustment = len([x for x in seq if x > 15])
    accumulator += adjustment * 3

    return accumulator

# Auxiliary function: dead code path
def calculate_entropy(data):
    counts = Counter(data)
    probs = [count / len(data) for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs)

# Generate base data
base_readings = [5, 8, 12, 14, 6, 21, 18, 7]

# Apply preprocessing (only this output is used)
processed_data = preprocess_sensor_stream(base_readings)

# Transform each element through piecewise function
transformed_data = [transform_signal(x) for x in processed_data]

# Create key sequence with slicing and manipulation (used in analysis)
key_sequence = [3, 1, 4, 1, 5]
extended_key = (key_sequence * 3)[::2][:len(transformed_data)]  # Slicing operation

# Dead-end variables (distractors)
smoothed_data = normalize_readings(transformed_data)
shifted_signal = time_shift_signal(transformed_data, 2)
entropy_value = calculate_entropy(transformed_data)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_sequence)

print(f"Result: {final_diagnostic}")