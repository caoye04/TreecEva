def sensor_calibrate(raw):    
    # Irrelevant calibration routine (dead code path)
    return [x * 0.98 for x in raw if x > 0]


def accumulate_segments(data):
    # Distractor function: looks important but unused
    segments = []
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        if len(chunk) == 3:
            segments.append(sum(chunk))
    return segments


def transform_signal(signal):
    # Real transformation used later
    adjusted = [s ** 0.5 if s > 0 else 0 for s in signal]
    normalized = [val / (max(adjusted) + 1e-6) for val in adjusted]
    return normalized


def filter_outliers(stream, threshold=2.0):
    mean_val = sum(stream) / len(stream)
    std_val = (sum((x - mean_val) ** 2 for x in stream) / len(stream)) ** 0.5
    return [x for x in stream if abs(x - mean_val) <= threshold * std_val]


def recursive_reduce(seq, factor=0.85):
    # Used in processing chain
    if len(seq) <= 1:
        return seq[0] if seq else 0
    mid = len(seq) // 2
    left = recursive_reduce(seq[:mid], factor)
    right = recursive_reduce(seq[mid:], factor * 0.95)
    return (left + right) * factor


def analyze_readings(data_list):
    # Core analysis logic
    stats = {}
    for idx, reading in enumerate(data_list):
        if idx % 2 == 0:
            stats[f'even_{idx}'] = reading * 1.1
        else:
            stats[f'odd_{idx}'] = reading * 0.9
    
    # Extract values and compute weighted diagnostic
    weights = [1.1 if i % 2 == 0 else 0.9 for i in range(len(data_list))]
    weighted_sum = sum(val * w for val, w in zip(data_list, weights))
    base_score = weighted_sum / len(data_list)
    
    # Secondary adjustment using recursive reduction
    trend_factor = recursive_reduce(data_list)
    
    # Final computation
    final_diagnostic = base_score * 0.7 + trend_factor * 0.3
    
    # Red herring variables (never used)
    temp_cache = {i: v**2 for i, v in enumerate(data_list)}
    checksum = sum(temp_cache[k] for k in temp_cache if k % 3 == 0)
    anomaly_flag = checksum > 500
    
    return final_diagnostic

# Simulated sensor input (real data)
raw_input = [16, 25, 9, 64, 36, 49, 81]

# Unused but plausible preprocessing
calibrated = sensor_calibrate(raw_input)

# Actual processing path
filtered = filter_outliers(raw_input, threshold=1.8)
transformed = transform_signal(filtered)
processed_data = [int(x * 100) / 100 for x in transformed]  # Round to 2 decimals

# Dead code - looks like aggregation
segment_sums = accumulate_segments(processed_data)

# Key statement
final_diagnostic = analyze_readings(processed_data)

# Output result
print(f"Result: {final_diagnostic}")