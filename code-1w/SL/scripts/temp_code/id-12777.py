import math

# Sensor calibration constants (irrelevant to final result but look important)
CALIBRATION_OFFSETS = {'sensor_a': 0.023, 'sensor_b': -0.017, 'sensor_c': 0.041}
BASELINE_NOISE_FLOOR = 0.005
MAX_READING_CAPACITY = 1000

# Simulated raw sensor readings from environmental monitoring system
def fetch_raw_readings():
    return [127, 89, 211, 156, 67, 199, 143, 76, 188, 102]

# Misleading preprocessing that appears critical but only some parts are used
def preprocess_sensor_data(raw_readings):
    normalized = []
    squared_errors = []
    cumulative_sum = 0
    
    for val in raw_readings:
        # Irrelevant normalization step with distractor variables
        adjusted = val + CALIBRATION_OFFSETS['sensor_a'] * 10
        if adjusted > 150:
            adjusted -= BASELINE_NOISE_FLOOR * 2
        
        # Actual relevant transformation
        normalized.append(int(adjusted) % 256)
        
        # Dead code path - never used later
        error_sq = (val - 128) ** 2
        squared_errors.append(error_sq)
        
        # Distractor accumulation
        cumulative_sum += error_sq % 17
    
    # Return includes irrelevant components
    return {
        'processed': normalized,
        'checksum': sum(squared_errors) % 1000,
        'distractor_flag': cumulative_sum > 50
    }

# Threshold configuration map - actually used in final analysis
def build_threshold_map():
    config = {}
    for i in range(33, 127):
        category = 'low'
        if i > 90:
            category = 'high'
        elif i > 60:
            category = 'medium'
        
        # Only the 'high' entries will be used; others are red herrings
        if category == 'high':
            config[i] = {
                'limit': 180 + (i % 7),
                'weight': 0.8 + (i % 5) * 0.1,
                'active': True
            }
    return config

# Core analysis function with conditional logic and dictionary operations
def analyze_readings(data_dict, thresholds):
    readings = data_dict['processed']
    total_weighted = 0
    count_valid = 0
    diagnostic_code = 0
    
    # Simulated fault detection that looks important but doesn't affect output
    suspected_anomalies = []
    for r in readings:
        if r in [67, 76, 89]:
            suspected_anomalies.append(r * 2 + 1)
    
    # Real processing: find values above dynamic threshold based on mapping
    for reading in readings:
        # Only applies when reading is in threshold keys
        if reading in thresholds:
            limit = thresholds[reading]['limit']
            weight = thresholds[reading]['weight']
            
            # This condition is never true due to value ranges (misleading)
            if reading < limit and weight > 1.0:
                total_weighted += reading * weight
                count_valid += 1
            
            # Actual contributing case
            if reading >= 180 and reading in [188, 199, 211]:
                # Only 211 triggers this (due to threshold presence)
                total_weighted += reading * 0.5
                count_valid += 1
                diagnostic_code ^= reading % 100  # XOR pattern
    
    # Secondary processing with distractor logic
    temp_factor = len(suspected_anomalies) * 3
    if temp_factor > 10:
        diagnostic_code += int(math.sqrt(temp_factor))
    
    # Final computation - only this matters
    if count_valid > 0:
        base_result = int(total_weighted / count_valid)
        final_score = base_result + diagnostic_code
    else:
        final_score = 999  # dead path
    
    # Additional decoy transformations
    final_score = final_score * 1  # neutral operation
    final_score += 0             # another neutral
    
    return final_score

# Orchestration function with apparent complexity
def run_diagnostics():
    # Step 1: Fetch data
    raw_data = fetch_raw_readings()
    
    # Step 2: Preprocess with multiple outputs (some unused)
    processed_data = preprocess_sensor_data(raw_data)
    
    # Step 3: Build threshold configuration (key component)
    threshold_map = build_threshold_map()  # Only certain keys matter
    
    # Step 4: Run actual analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print required output format
    print(f"Result: {final_diagnostic}")
    
    # Return for clarity (not used)
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    run_diagnostics()