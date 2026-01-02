import math

# Sensor simulation and diagnostic system
def generate_synthetic_readings():
    raw_values = []
    for i in range(20):
        val = (i * i + 3 * i + 7) % 100
        raw_values.append(val)
    return raw_values

# Irrelevant auxiliary function (decoy)
def analyze_pattern(data):
    trend = 0
    for j in range(len(data) - 1):
        if data[j] < data[j+1]:
            trend += 1
    return trend > 5

# Real processing pipeline
def filter_outliers(data, threshold=75):
    result = []
    for x in data:
        if x <= threshold:
            result.append(x)
    return result

# Complex transformation with lambda and conditional logic
def apply_calibration(readings, factor):
    calibrated = []
    adjust = lambda x, f: round(x * f + math.sin(x), 4) if x % 2 == 0 else round(x * f + math.cos(x), 4)
    
    temp_store = []
    index_map = {}
    
    # Distractor loop - builds unused structure
    for idx, val in enumerate(readings):
        index_map[idx] = val * val + 2 * val + 1  # Unused quadratic mapping
    
    # Actual processing
    for val in readings:
        adjusted = adjust(val, factor)
        temp_store.append(adjusted)
        
    # Another decoy: sort but don't use sorted version
    temp_store.sort(reverse=True)
    
    # Return unsorted (original order preserved)
    return temp_store

# Secondary filtering based on decimal part
def truncate_to_decimal_limit(calibrated):
    limited = []
    for val in calibrated:
        decimal_part = val - int(val)
        if decimal_part < 0.7 or val > 90:
            limited.append(val)
    return limited

# Final aggregation logic
def compute_entropy(data):
    # Simulated entropy from distribution
    freq_map = {}
    total = len(data)
    for x in data:
        bin_key = int(x)
        freq_map[bin_key] = freq_map.get(bin_key, 0) + 1
    
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Main integration function
def process_readings(data_list, scale):
    step1 = filter_outliers(data_list, threshold=72)
    step2 = apply_calibration(step1, scale)
    step3 = truncate_to_decimal_limit(step2)
    
    # Dead code path - never accessed
    if len(step3) == 0:
        fallback = [x * scale for x in step1]
        return sum(fallback)
    
    # Core computation
    valid_count = len([x for x in step3 if x > 0])
    total_sum = sum(step3)
    average = total_sum / valid_count if valid_count > 0 else 0
    
    # Entropy-based adjustment
    entropy_value = compute_entropy(step3)
    adjustment_factor = math.sqrt(entropy_value) if entropy_value > 0 else 1
    
    # Final diagnostic score
    diagnostic_score = (average * adjustment_factor) - (len(data_list) - len(step3))
    
    # Red herring variables
    phantom_metric = sum([int(x) ^ 3 for x in step3])  # Bitwise XOR distraction
    dummy_flag = any(x < 0 for x in step3)  # Always false, irrelevant
    
    return round(diagnostic_score, 4)

# Misleading initialization block
initial_config = {
    'version': 'A7',
    'mode': 'diagnostic',
    'debug': True,
    'iterations': 3
}

# Unused signal smoothing (distractor)
def moving_average(signal, window=3):
    smoothed = []
    for i in range(len(signal) - window + 1):
        avg = sum(signal[i:i+window]) / window
        smoothed.append(avg)
    return smoothed

# Primary execution flow
data_source = generate_synthetic_readings()

# Spurious analysis call (no effect on result)
diagnostic_trend = analyze_pattern(data_source)

filtered_data = filter_outliers(data_source, 72)
calibration_factor = 1.08

# Key statement
final_diagnostic = process_readings(filtered_data, calibration_factor)

print(f"Result: {final_diagnostic}")