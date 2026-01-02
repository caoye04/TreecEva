from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis
def preprocess_readings(raw_data, scaling_factor=1.0):
    processed = []
    cumulative_noise = 0
    
    for item in raw_data:
        raw_value = item['value']
        sensor_type = item['type']
        
        # Irrelevant transformation for humidity sensors (dead logic path)
        if sensor_type == 'humidity':
            adjusted = raw_value * 0.9 + 2.1
            cumulative_noise += abs(adjusted - raw_value)
        
        # Only temperature readings are actually used later
        if sensor_type == 'temperature':
            corrected = (raw_value * scaling_factor) + 0.5
            processed.append(round(corrected, 3))
    
    # Dead return - never used
    return {'data': processed, 'noise': cumulative_noise}

# Misleading filtering function that looks important but isn't used in critical path
def legacy_filter(sequence, limit):
    result = []
    for x in sequence:
        if abs(x) > limit:
            result.append(x * 2)
    return result

# Unused utility: calculates statistical moments (distraction)
def compute_moments(data):
    n = len(data)
    if n == 0:
        return [0, 0, 0, 0]
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / n
    skewness = sum((x - mean)**3 for x in data) / (n * variance ** 1.5) if variance > 0 else 0
    kurtosis = sum((x - mean)**4 for x in data) / (n * variance ** 2) - 3 if variance > 0 else 0
    return [mean, variance, skewness, kurtosis]

# Real filtering: removes anomalous values above threshold
def filter_anomalous(readings, threshold):
    non_anomalous = []
    anomaly_count = 0
    
    for val in readings:
        if abs(val) <= threshold:  # Keep only non-anomalous
            non_anomalous.append(val)
        else:
            anomaly_count += 1
    
    # Return only the clean data (anomaly count unused downstream)
    return non_anomalous

# Configuration class that appears complex but only one field matters
class SystemConfig:
    def __init__(self):
        self.baseline_offset = -3.2
        self.gain = 1.8
        self.window_size = 7
        self.enable_smoothing = True
        self.normalization_mode = 'z-score'

# Main analysis function with multiple red herrings
def analyze_readings(valid_readings, config):
    if not valid_readings:
        return -999.99
    
    # Key computation
    offset = config.baseline_offset
    adjusted_values = [x + offset for x in valid_readings]
    
    # Distractor: complex smoothing logic that's bypassed
    if config.enable_smoothing and len(adjusted_values) >= config.window_size:
        smoothed = []
        window = config.window_size // 2
        for i in range(len(adjusted_values)):
            start = max(0, i - window)
            end = min(len(adjusted_values), i + window + 1)
            avg = sum(adjusted_values[start:end]) / (end - start)
            smoothed.append(avg)
    else:
        smoothed = adjusted_values  # Smoothing disabled by design due to short input
    
    # Real computation path
    magnitude = sum(abs(x) for x in smoothed)
    count = len(smoothed)
    
    # Secondary distraction: frequency analysis of digit patterns
    digit_counter = defaultdict(int)
    for val in valid_readings:
        int_part = int(abs(val))
        for digit in str(int_part):
            digit_counter[int(digit)] += 1
    
    common_digits = Counter(digit_counter).most_common(3)
    
    # Final diagnostic score based on average absolute deviation from baseline
    baseline_diagnostic = magnitude / count if count > 0 else 0
    
    # This is the actual answer variable
    final_diagnostic = round(baseline_diagnostic, 6)
    
    # Decoy variables that look important
    entropy_metric = -sum((count/len(digit_counter)) * math.log(count/len(digit_counter)) 
                         for count in digit_counter.values() if count > 0)
    system_score = baseline_diagnostic * 0.8 + entropy_metric * 0.2
    
    return final_diagnostic

# --- Execution Context ---
if __name__ == '__main__':
    # Raw sensor data (only 'temperature' type matters)
    readings = [
        {'type': 'temperature', 'value': 12.5},
        {'type': 'humidity', 'value': 45},
        {'type': 'temperature', 'value': 14.0},
        {'type': 'pressure', 'value': 1013},
        {'type': 'temperature', 'value': 11.8},
        {'type': 'temperature', 'value': 15.2},
        {'type': 'humidity', 'value': 52},
        {'type': 'temperature', 'value': 13.1}
    ]
    
    # Threshold for anomaly detection
    threshold = 18.0  # High enough to let all through
    
    # Baseline configuration
    baseline_config = SystemConfig()
    # Override the effective parameter
    baseline_config.baseline_offset = -3.2  # Critical value
    
    # Preprocess (only extracts and scales temperature)
    preprocessed = preprocess_readings(readings, scaling_factor=1.0)
    temp_only = [item['value'] for item in readings if item['type'] == 'temperature']
    
    # Filter anomalous readings
    filtered_readings = filter_anomalous(temp_only, threshold)
    
    # Analyze diagnostics
    final_diagnostic = analyze_readings(filtered_readings, baseline_config)
    
    # Output result
    print(f"Target result: {final_diagnostic}")