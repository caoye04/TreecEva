import math

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 1.02
CALIBRATION_B = 0.98
CALIBRATION_C = 2.15  # unused
decoy_factor = 0.0034  # irrelevant

# Simulated environmental sensor readings
def get_raw_readings():
    return [14.2, 15.1, 13.8, 16.0, 14.5, 15.3, 13.9, 14.7, 15.0, 14.1]

# Noise injection for realism (but not actually affecting main logic)
def add_noise(value, level=0.05):
    return value + level * 0.1  # negligible effect, distraction

# Process raw sensor data with normalization
def process_sensor_data(raw):
    normalized = []
    base_ref = raw[0]
    for val in raw:
        corrected = val * CALIBRATION_A  # only A is used
        normalized.append(round(corrected, 2))
    return normalized

# Legacy function - appears important but unused
def legacy_calibrate(data):
    result = []
    for x in data:
        if x > 15.0:
            result.append(x * 0.9)
        else:
            result.append(x * 1.1)
    return result  # never called

# Analyze frequency distribution of readings
def compute_distribution(data):
    freq = {}
    for val in data:
        key = int(val)
        freq[key] = freq.get(key, 0) + 1
    sorted_keys = sorted(freq.keys())
    median_key = sorted_keys[len(sorted_keys)//2]
    return {'mode': max(freq, key=freq.get), 'median_approx': median_key}  # partial use

# Determine thresholds based on statistical spread
def generate_thresholds(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val)**2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return {
        'low': mean_val - 0.5 * std_dev,
        'high': mean_val + 0.5 * std_dev,
        'critical': mean_val + 1.2 * std_dev
    }

# Misleading diagnostic path - looks useful but unused
def assess_stability_metrics(data):
    peaks = 0
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks += 1
    trend = 'stable' if peaks < 3 else 'fluctuating'
    return {'peaks': peaks, 'trend': trend}  # computed but ignored later

# Core analysis: count how many readings exceed dynamic thresholds
def analyze_readings(data, thresholds):
    count_above_high = 0
    total_weight = 0.0
    weight_map = {14: 1.2, 15: 1.8, 16: 2.1}
    
    for reading in data:
        int_part = int(reading)
        if reading > thresholds['high']:
            count_above_high += 1
        if int_part in weight_map:
            total_weight += weight_map[int_part]
    
    # Final diagnostic combines count and weighted sum
    return int(count_above_high * total_weight * 10)  # deterministic computation

# Unused helper - adds distraction
def validate_readings_format(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    for item in data:
        if not isinstance(item, float):
            return False
    return True

# Main execution flow
if __name__ == "__main__":
    raw_data = get_raw_readings()
    processed_data = process_sensor_data(raw_data)
    
    # Compute distractor metrics (appear important)
    distribution_stats = compute_distribution(processed_data)
    stability_report = assess_stability_metrics(processed_data)  # computed but unused
    
    # Only this threshold map is used
    threshold_map = generate_thresholds(processed_data)
    
    # Dead code path - never executed
    debug_mode = False
    if debug_mode:
        print("Debug info:", processed_data)
    
    # Key statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Irrelevant set operation - red herring
    unique_ints = set(int(x) for x in processed_data)
    extra_calc = len(unique_ints.union({14, 15, 16, 17}))  # unused
    
    # Another decoy dictionary
    status_flags = {
        'calibrated': True,
        'no_noise': False,
        'finalized': None
    }
    status_flags['finalized'] = 'complete'  # side effect, not used
    
    Result: final_diagnostic