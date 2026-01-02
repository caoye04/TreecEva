import itertools

# Simulated multi-sensor array with diagnostic flags
def generate_sensor_data():
    raw_values = [14.2, 15.1, 0.0, 14.8, 16.0, 15.3, 0.0, 14.9, 15.0, 15.2]
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'WARNING', 'OK', 'ERROR', 'OK', 'OK', 'OK']
    timestamps = list(range(1000, 1010))
    return list(zip(raw_values, statuses, timestamps))

# Irrelevant transformation: converts readings to hex (dead path)
def legacy_encode(values):
    return [hex(int(v * 10)) for v in values]

# Decoy function: appears useful but unused in critical path
def validate_calibration(data):
    total_weight = sum(1 for d in data if d[1] == 'OK')
    return total_weight > 5

# Filters out unstable readings (ERROR flagged)
def filter_stable(data):
    stable = [d for d in data if d[1] != 'ERROR']
    return stable

# Extracts numeric component from filtered data
def extract_readings(filtered_data):
    return [item[0] for item in filtered_data]

# Applies moving average smoothing (3-point window)
def smooth_readings(readings):
    if len(readings) < 3:
        return readings
    smoothed = []
    for i in range(1, len(readings) - 1):
        smoothed.append((readings[i-1] + readings[i] + readings[i+1]) / 3)
    return smoothed

# Computes entropy-like metric for variation analysis
def compute_variability_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    return variance ** 0.5

# Main processing pipeline
def process_readings(sensor_data):
    # Extract only numerical values
    numeric_stream = extract_readings(sensor_data)
    
    # Apply smoothing to reduce noise
    cleaned = smooth_readings(numeric_stream)
    
    # Compute stability metric
    stability_score = compute_variability_index(cleaned)
    
    # Generate diagnostic code using set operations (irrelevant categorization)
    categories = {'low': {0,1}, 'mid': {2,3,4}, 'high': {5}}
    level_key = 'high' if stability_score > 0.3 else 'mid'
    diagnostic_set = categories[level_key]
    
    # Use itertools to create artificial expansion (distraction)
    expanded = list(itertools.chain.from_iterable(
        [(x, x*0.1) for x in cleaned if x > 14.5]
    ))
    
    # Final diagnostic is based on bit manipulation of rounded stability
    stability_int = int(round(stability_score * 100))
    masked = stability_int ^ 0b110101  # Arbitrary bit mask
    final_diagnostic = masked + len(expanded) // 2
    
    # Dead code: this would alter result but is never reached
    if False:
        backup = sum(numeric_stream) % 7
        final_diagnostic += backup * 2
    
    return final_diagnostic

# Unused utility: string-based log formatter (red herring)
def format_diagnostics_log(data, code):
    status_chars = ''.join(d[1][0] for d in data)
    code_hex = format(code, 'x')
    return f"LOG:{status_chars}:{code_hex.upper()}"

# Global variables (some irrelevant)
sensor_cluster = generate_sensor_data()
baseline_offset = 14.0
normal_range = (14.5, 15.5)
deprecated_flags = legacy_encode([1.0, 2.0])  # Unused

# Critical execution point
final_diagnostic = process_readings(filter_stable(sensor_cluster))

# Output result
print(f"Result: {final_diagnostic}")