import math

# Simulated sensor data preprocessing pipeline
raw_readings = [3.2, 5.7, 1.8, 9.9, 4.6, 7.1, 2.3, 8.0, 6.5, 5.0]

def apply_calibration(readings):
    # Irrelevant calibration logic (not used in final path)
    offset = 0.5
    calibrated = [r + offset for r in readings]
    return [round(c, 1) for c in calibrated]

def filter_outliers(data, threshold=8.0):
    # Red herring function: looks important but not actually used
    return [x for x in data if x <= threshold]

def compute_entropy(values):
    # Distractor: computes information-theoretic entropy (unused)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def rolling_window_avg(sequence, window_size=3):
    # Unused advanced processing
    averages = []
    for i in range(len(sequence) - window_size + 1):
        averages.append(sum(sequence[i:i+window_size]) / window_size)
    return averages

def extract_peaks(signal):
    # Dead code path — never called
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

# Key transformation chain
baseline_correction = lambda x: (x ** 2) - (x * 1.5)

corrected_data = [baseline_correction(val) for val in raw_readings]

transformed_data = []
for val in corrected_data:
    if val < 10:
        transformed_data.append(val * 1.2)
    elif val < 20:
        transformed_data.append(val * 1.1)
    else:
        transformed_data.append(val * 0.9)

# Decoy statistical summaries
temp_stats = {
    'mean': sum(transformed_data) / len(transformed_data),
    'max': max(transformed_data),
    'min': min(transformed_data),
    'range': max(transformed_data) - min(transformed_data)
}

# Irrelevant bit manipulation layer (distractor)
def encode_flag(value):
    shifted = int(value * 10) << 2
    masked = shifted & 0xFF
    return masked ^ 0xAA  # XOR obfuscation (unused)

encoded_values = [encode_flag(x) for x in transformed_data]

# Real computation begins here — hidden among distractions
thresholds = {"low": 5.0, "high": 15.0, "critical": 25.0}

# Aggregate logic that depends on prior transformations
def aggregate_metrics(data, config):
    count_low = count_high = count_critical = 0
    running_sum = 0.0
    
    for reading in data:
        running_sum += reading
        if reading < config["low"]:
            count_low += 1
        elif reading < config["high"]:
            count_high += 1
        elif reading < config["critical"]:
            count_critical += 1
    
    # Complex weighting scheme
    weight = 1.0
    if count_critical > 2:
        weight *= 1.3
    if count_low == 0:
        weight *= 0.8
    if count_high % 2 == 0:
        weight *= 1.1
    
    # Final diagnostic score
    base_score = running_sum / len(data)
    adjusted_score = base_score * weight
    
    # Normalize using trigonometric scaling (necessary step)
    normalized = adjusted_score * math.cos(math.pi / 5)
    
    # Critical dependency on earlier lambda-based correction
    return round(normalized, 6)

# Unused alternative aggregation
# def legacy_aggregate(seq): return sum(s**0.5 for s in seq if s > 0)

# Actual execution point
interim_snapshot = transformed_data.copy()  # Misleading checkpoint

final_diagnostic = aggregate_metrics(transformed_data, thresholds)

# Output required result
print(f"Result: {final_diagnostic}")