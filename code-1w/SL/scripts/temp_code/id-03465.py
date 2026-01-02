def sensor_calibration(sequence):
    calibrated = []
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            calibrated.append(val * 1.1)
        elif i % 5 == 0:
            calibrated.append(val + 2.5)
        else:
            calibrated.append(val * 0.95)
    return [round(x, 3) for x in calibrated]

# Irrelevant helper (distractor)
def compress_signal(data):
    return [d for i, d in enumerate(data) if i % 2 == 0]

def filter_outliers(stream, limit=100):
    # Only values within range are kept
    cleaned = [x for x in stream if abs(x) < limit]
    return sorted(cleaned, reverse=True)

# Another decoy function
def generate_checksum(items):
    checksum = 0
    for idx, item in enumerate(items):
        checksum += item * (idx + 1)
    return checksum % 1000

# Complex preprocessing with meaningful and irrelevant parts
def preprocess_readings(raw_readings):
    base_offset = 7.2
    adjusted = [r + base_offset for r in raw_readings]
    
    # Distractor: unused transformation
    inverted = [1.0 / (abs(x) + 1e-5) for x in adjusted]
    
    # Actual relevant path
    normalized = [(x - min(adjusted)) / (max(adjusted) - min(adjusted) + 1e-8) for x in adjusted]
    scaled = [int(x * 1000) for x in normalized]
    
    # Dead code path (never used)
    if len(scaled) > 100:
        bucketed = [x // 10 for x in scaled]
        return bucketed
    
    return scaled  # This is actually used

# Threshold logic with red herring parameters
def build_threshold_map(config_code):
    codes = {
        'A': lambda x: x > 500,
        'B': lambda x: x < 200 or x > 800,
        'C': lambda x: 300 < x < 700
    }
    default_func = lambda x: x != 0
    
    # Misleading: this map is not fully used
    full_map = {k: (v, default_func) for k, v in codes.items()}
    
    # But only this subset is actually applied later
    return {'threshold_500': codes['A'], 'sensitivity_C': codes['C']}

# Core analysis logic
def analyze_readings(data_points, rules):
    count_A = 0
    count_C = 0
    
    # Real computation
    for point in data_points:
        if rules['threshold_500'](point):
            count_A += 1
        if rules['sensitivity_C'](point) and point % 2 == 0:
            count_C += 1
    
    # Irrelevant counters (distractors)
    total_pairs = sum(1 for a, b in zip(data_points, data_points[1:]) if a + b > 500)
    sequence_runs = 0
    current_run = 0
    for x in data_points:
        if x > 300:
            current_run += 1
        else:
            if current_run > 2:
                sequence_runs += 1
            current_run = 0
    
    # Final diagnostic is based only on count_A and count_C
    stability_index = (count_A * 1.7) + (count_C * 2.3)
    return round(stability_index, 4)

# --- Main Execution with Distractions ---
if __name__ == "__main__":
    # Simulated sensor input (real data source)
    raw_sensor_data = [85, 92, 78, 101, 88, 76, 95, 110, 80, 98, 73, 105]
    
    # Distractor: alternate dataset never used
    legacy_stream = [102, 87, 91, 75, 89, 96, 84, 93, 88, 90, 86, 94]
    
    # Apply calibration (relevant)
    calibrated_readings = sensor_calibration(raw_sensor_data)
    
    # Preprocess readings (relevant)
    processed_data = preprocess_readings(calibrated_readings)
    
    # Build threshold rules (relevant)
    threshold_map = build_threshold_map('C')
    
    # Analyze the data (key statement)
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")