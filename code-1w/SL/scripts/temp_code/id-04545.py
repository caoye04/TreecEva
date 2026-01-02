import math

# Sensor simulation and filtering system
def collect_sensor_data():
    raw_readings = [i * 1.5 + (i % 7) for i in range(30)]
    noise_floor = 4.2
    adjusted = [x + noise_floor if x < 10 else x - noise_floor for x in raw_readings]
    return adjusted

def apply_calibration(data):
    # Real calibration logic
    calibrated = [round(x * 0.92, 3) for x in data]
    
    # Irrelevant diagnostic traces
    avg_val = sum(calibrated) / len(calibrated)
    peak = max(calibrated)
    outlier_count = len([x for x in calibrated if x > 25])
    status_codes = {1: 'OK', 2: 'CALIBRATING', 3: 'ERROR'}
    current_status = status_codes[1]
    
    # Dead computation branch - never used
    temp_analysis = []
    for val in calibrated:
        if val > 20:
            temp_analysis.append(val ** 0.5)
        elif val < 5:
            temp_analysis.append(val * -1)
    
    return calibrated

def filter_anomalies(data):
    anomalies = set()
    for i, x in enumerate(data):
        if abs(x - data[i-1]) > 8 if i > 0 else False:
            anomalies.add(i)
    cleaned = [data[i] for i in range(len(data)) if i not in anomalies]
    
    # Distractor: irrelevant statistical shadow variables
    median_guess = sorted(cleaned)[len(cleaned)//2]
    variance_proxy = sum((x - median_guess)**2 for x in cleaned) / len(cleaned)
    entropy_approx = -sum((x/sum(cleaned))*math.log(x/sum(cleaned)) for x in cleaned if x > 0)
    
    return cleaned

def build_lookup_table(data):
    # This function is called but its result is not used in final calculation
    table = {}
    for i, val in enumerate(data):
        key = int(val) % 10
        if key not in table:
            table[key] = []
        table[key].append(val)
    compression_factor = len(data) / (len(table) + 1)
    return {'table': table, 'factor': round(compression_factor, 2)}

def compute_derivatives(data):
    # Another red herring: computes first and second differences
    first_deriv = [data[i] - data[i-1] for i in range(1, len(data))]
    second_deriv = [first_deriv[i] - first_deriv[i-1] for i in range(1, len(first_deriv))]
    zero_crossings = sum(1 for i in range(1, len(first_deriv)) if first_deriv[i-1] * first_deriv[i] < 0)
    return {'first': first_deriv, 'second': second_deriv, 'crossings': zero_crossings}

def process_readings(data, threshold_fn):
    # Core processing with embedded logic
    normalized = [max(0, x - 2.5) for x in data]
    
    # Bit manipulation decoy
    bit_signature = 0
    for val in normalized[:5]:
        shifted = int(val) << 1
        bit_signature ^= shifted
        bit_signature &= 0xFF  # Keep within byte range
    
    # Conditional expression mix
    category = 'HIGH' if any(x > 20 for x in normalized) else 'LOW'
    scaling_factor = 1.75 if category == 'HIGH' else 0.85
    
    # Key transformation
    transformed = [x * scaling_factor for x in normalized]
    
    # Lambda-based filtering
    valid_only = list(filter(lambda x: threshold_fn(x), transformed))
    
    # Final aggregation - actual answer source
    base_score = sum(valid_only)
    penalty = len([x for x in valid_only if x < 3]) * 1.2
    bonus = len([x for x in valid_only if x > 10]) * 0.8
    final_score = base_score - penalty + bonus
    
    # Multiple distractor variables
    complexity_index = len(valid_only) * scaling_factor / (bit_signature + 1)
    stability_ratio = (max(valid_only) - min(valid_only)) / final_score if final_score != 0 else 0
    debug_trace = f'SCORE:{final_score:.2f}|SIG:{bit_signature}'
    
    return final_score

# Main execution flow
sensor_data = collect_sensor_data()
calibrated_data = apply_calibration(sensor_data)
filtered_data = filter_anomalies(calibrated_data)

# Unused but plausible computations (distractors)
lookup_map = build_lookup_table(filtered_data)
deriv_analysis = compute_derivatives(filtered_data)

# Threshold logic - part of critical path
threshold_func = lambda x: x > 1.8

# Critical statement
final_diagnostic = process_readings(filtered_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")