import math

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 0.87
CALIBRATION_B = 1.03
CALIBRATION_C = 2.15  # unused
dummy_offset = 42  # red herring

# Simulated sensor readings from environmental monitoring system
def fetch_raw_readings():
    return [127, 134, 129, 131, 140, 126, 133, 138, 130, 125, 132, 137, 128, 135, 139]

# Noise reduction via moving average with window slicing
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal) - window_size + 1):
        window = signal[i:i + window_size]
        avg = sum(window) / window_size
        smoothed.append(round(avg, 2))
    return smoothed

# Transform raw data into processed metrics
def process_metrics(data):
    squared = [x ** 2 for x in data]
    root_mean = math.sqrt(sum(squared) / len(squared))
    normalized = [round(x / root_mean * CALIBRATION_A, 2) for x in data]
    return normalized

# Legacy function - never called, but looks relevant
def legacy_process(seq):
    return [x * 0.9 for x in seq if x > 130]

# Analyze thresholds across zones
threshold_map = {
    'zone_a': {'low': 120, 'high': 135},
    'zone_b': {'low': 125, 'high': 140},
    'debug_flag': True,  # distractor
    'meta': {'version': '2.1', 'calibrated': False}
}

# Unused diagnostic function that appears important
def compute_variance(seq):
    mean_val = sum(seq) / len(seq)
    return sum((x - mean_val) ** 2 for x in seq) / len(seq)

# Main analysis engine
def analyze_readings(data_slice, limits):
    zone_a_count = 0
    zone_b_count = 0
    
    for val in data_slice:
        if limits['zone_a']['low'] <= val <= limits['zone_a']['high']:
            zone_a_count += 1
        if limits['zone_b']['low'] <= val <= limits['zone_b']['high']:
            zone_b_count += 1

    # Complex conditional logic with early returns
    if zone_a_count > 5 and zone_b_count < 3:
        return zone_a_count * 17
    elif zone_b_count == 0:
        temp_diag = sum(data_slice) // len(data_slice)
        anomaly_score = temp_diag - 115
        return anomaly_score * 3  # misleading path, not triggered
    else:
        base = zone_a_count + zone_b_count
        adjustment = abs(zone_a_count - zone_b_count)
        result = base * 10 + adjustment
        
        # Final transformation using bit manipulation (relevant)
        shifted = (result << 2) ^ 7  # XOR with prime
        return shifted

# Irrelevant helper function
def format_report(code):
    prefix = f"ERR-{(code % 100):03d}"
    return {"code": code, "label": prefix}

# --- Execution Pipeline ---
raw_data = fetch_raw_readings()
smoothed_data = smooth_signal(raw_data)
processed_data = process_metrics(smoothed_data)

# Dead code path: this variable is never used
intermediate_checksum = sum(raw_data[i] * (i+1) for i in range(len(raw_data))) % 1000

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Debug print (mimics real system output)
print(f"Target result: {final_diagnostic}")