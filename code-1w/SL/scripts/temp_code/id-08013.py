import math

# Simulated sensor data processing system for environmental monitoring
def fetch_raw_readings():
    return [23.4, 18.9, 25.1, 30.2, 17.8, 22.0, 26.5, 29.8, 20.3, 24.7]

def calibrate_sensor(value, factor=1.02):
    # Irrelevant calibration function (not actually used in final computation)
    return value * factor

def normalize(value, min_val=15, max_val=35):
    return (value - min_val) / (max_val - min_val)

def is_stable_reading(value, base=22.5, tolerance=3.5):
    return abs(value - base) <= tolerance

def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def detect_outliers(values, stdev_limit=2):
    mean = sum(values) / len(values)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
    return [i for i, x in enumerate(values) if abs(x - mean) > stdev_limit * std_dev]

def filter_data(readings):
    # Real preprocessing path
    normalized = [normalize(x) for x in readings]
    stabilized = [x for x in readings if is_stable_reading(x)]  # Only stable readings kept
    return stabilized

def generate_checksum(data):
    # Distractor: complex but unused checksum logic
    chk = 0
    for i, val in enumerate(data):
        chk ^= int(val * 10) << (i % 4)
    return chk % 97

def evaluate_trend(sequence):
    # Dead code path — never called
    increases = sum(1 for i in range(1, len(sequence)) if sequence[i] > sequence[i-1])
    return 'rising' if increases > len(sequence)/2 else 'falling'

def aggregate_metrics(data_list):
    metrics = {}
    for idx, val in enumerate(data_list):
        if idx % 2 == 0:
            metrics[f'even_{idx}'] = val * 0.9
        else:
            metrics[f'odd_{idx}'] = val * 1.1
    return metrics  # Unused in main flow

def analyze_readings(data, thresholds):
    # Core logic begins here
    base_ref = thresholds['critical']
    adjustment = 0
    for val in data:
        if val > thresholds['warning']:
            adjustment += 0.5
        elif val < thresholds['minimum']:
            adjustment -= 0.3
    
    # Key calculation branch
    if len(data) > 6:
        adjustment *= 1.2
    else:
        adjustment *= 0.8
    
    # Secondary influence
    variance_factor = compute_variance(data) / 10
    adjusted_score = base_ref + adjustment - variance_factor
    
    # Red herring: irrelevant transformation
    temp_result = [math.log(x + 5) for x in data if x > 20]
    dummy_agg = sum(temp_result) / len(temp_result) if temp_result else 0
    
    # Final interference: masking operation that doesn't affect outcome
    mask = sum(1 << (i % 8) for i in range(len(data))) & 0xFF
    masked_effect = (int(adjusted_score * 10) ^ mask) % 50
    
    # Actual answer derivation
    final_diagnostic = int(adjusted_score * 10) + 7  # Critical offset
    return final_diagnostic

# --- Main execution with distractions ---
raw_data = fetch_raw_readings()

# Irrelevant parallel processing chain
shadow_copy = [calibrate_sensor(x) for x in raw_data]
dummy_checksum = generate_checksum(shadow_copy)
dummy_metrics = aggregate_metrics(shadow_copy)

# Real data path
processed_data = filter_data(raw_data)

# Multiple misleading threshold sets
threshold_levels = {
    'minimum': 18.0,
    'warning': 24.0,
    'critical': 28.0,
    'emergency': 32.0  # Unused
}

aux_thresholds = {
    'low': 10, 'high': 40, 'alert': 26.5
}  # Never used

# Simulate intermediate logging (distraction)
current_status = 'NORMAL'
if any(x > 29 for x in raw_data):
    current_status = 'MONITORING'

# Trigger actual computation
final_diagnostic = analyze_readings(processed_data, threshold_levels)

# Additional red herring: unused recursive function
def trace_path(n):
    if n <= 1:
        return 1
    return trace_path(n-1) + trace_path(n-2)

# Output result as required
print(f"Result: {final_diagnostic}")