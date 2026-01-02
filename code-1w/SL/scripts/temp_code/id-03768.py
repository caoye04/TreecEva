import math

# Simulated sensor array data with noise and calibration offsets
def fetch_raw_sensor_data():
    base_values = [2.1, 3.5, 4.8, 5.2, 6.9, 7.3, 8.0, 9.1]
    noise_offsets = [0.1 * i for i in range(8)]
    return [base_values[i] + noise_offsets[i] for i in range(len(base_values))]

def apply_calibration(readings, calib_factor=1.05, threshold=5.0):
    # Misleading branching: unused under current params
    if len(readings) > 10:
        return [r * 0.9 for r in readings]
    adjusted = []
    for r in readings:
        if r < threshold:
            adjusted.append(r * calib_factor)
        else:
            adjusted.append(r * (calib_factor - 0.05))
    return adjusted

def filter_outliers(data, limit=8.5):
    # Some values are above limit, but not filtered — misleading name
    return [x for x in data if x <= limit + 0.5]  # relaxed filter, all pass

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return entropy

def derive_key_metric(vals):
    # Complex transformation with red herring computation
    squared_sum = sum(v ** 2 for v in vals)
    linear_sum = sum(vals)
    dummy_variance = (squared_sum / len(vals)) - (linear_sum / len(vals)) ** 2
    # Actual metric used is simpler
    return linear_sum / len(vals)

# Unused decoy functions — dead code path
def deprecated_analysis(x):
    return sum(x) % 7

def temp_correction(arr, mode='none'):
    if mode == 'aggressive':
        return [a - 0.3 for a in arr]
    return arr

# Main processing pipeline
def main_pipeline():
    raw_data = fetch_raw_sensor_data()  # [2.1, 3.6, 5.1, 6.6, 8.1, 9.6, 10.0, 11.1]
    
    # Apply multiple transformations — some irrelevant
    calibrated = apply_calibration(raw_data, calib_factor=1.05)
    corrected = temp_correction(calibrated, mode='none')
    cleaned = filter_outliers(corrected)
    
    # Derive secondary metrics — one is a distraction
    entropy_value = compute_entropy(cleaned)  # ~1.98, never used
    avg_reading = derive_key_metric(cleaned)
    
    # Create composite diagnostic tuple — distractor elements included
    intermediate_diagnostics = (
        len(cleaned),
        round(avg_reading, 2),
        int(entropy_value * 10),
        sum(int(x) for x in cleaned)  # sum of truncated values
    )
    
    # Simulate historical comparison (static reference — no real effect)
    historical_norms = (8, 6.85, 19, 54)
    deviation_flags = [
        1 if abs(intermediate_diagnostics[i] - historical_norms[i]) > 1 else 0
        for i in range(4)
    ]
    flag_score = sum(deviation_flags)  # always 2 — misleading
    
    # Critical data restructuring: grouping by even/odd index
    grouped = [
        (cleaned[i], cleaned[i+1]) for i in range(0, len(cleaned)-1, 2)
    ]
    processed_data = []
    for pair in grouped:
        # Only first element of each pair is transformed meaningfully
        processed_data.append(pair[0] * 0.85)
        processed_data.append(pair[1] * 0.0)  # zeroed — red herring
    
    # Final analysis function
    def analyze_readings(seq):
        base = sum(seq)  # only non-zero contributions matter
        adjustment = math.floor(base * 0.1) if base > 20 else 0
        return int(base) + adjustment
    
    final_diagnostic = analyze_readings(processed_data)
    return final_diagnostic

# Execute and output result
def run_task():
    final_diagnostic = main_pipeline()
    print(f"Result: {final_diagnostic}")

run_task()