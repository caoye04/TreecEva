import math

# Simulated sensor data processing for aerospace subsystem diagnostics
def analyze_sensor_readings(raw_readings, calibration_factor):
    processed = []
    temp_buffer = []
    for idx, val in enumerate(raw_readings):
        if idx % 3 == 0:
            adjusted = (val * calibration_factor) + 0.5
        elif idx % 5 == 0:
            adjusted = val * 1.1
        else:
            adjusted = val
        temp_buffer.append(adjusted)
    
    # Irrelevant smoothing pass (dead code path - not used later)
    smoothed = [sum(temp_buffer[i:i+3]) / 3 for i in range(len(temp_buffer) - 2)]
    
    # Actual relevant transformation
    for i in range(len(temp_buffer)):
        if temp_buffer[i] > 100:
            temp_buffer[i] = math.sqrt(temp_buffer[i])
    return temp_buffer

# Legacy function - never called (decoy)
def legacy_calibrate(x):
    return [e * 0.95 for e in x if e > 50]

# Auxiliary diagnostic weight assignment
def compute_health_score(status_code, severity_map):
    base = 100
    for key, val in severity_map.items():
        if status_code & key:
            base -= val
    return max(base, 0)

# Core diagnostic aggregation with distractors
def aggregate_diagnostics(log_entries, flags):
    weights = {'critical': 10, 'warning': 5, 'info': 1}
    decoy_weights = {'high': 8, 'medium': 3}  # Unused
    total_risk = 0
    risk_counter = 0
    
    # Complex nested structure with red herrings
    intermediate_results = []
    for entry_idx, entry in enumerate(log_entries):
        timestamp = entry['time']
        code = entry['code']
        category = entry['type']
        
        # Distractor: irrelevant time-based filtering
        if timestamp % 7 == 0:
            adjustment = 0.8
        elif timestamp < 50:
            adjustment = 1.2
        else:
            adjustment = 1.0
        
        # Real computation
        score = compute_health_score(code, {1: 20, 4: 15, 8: 30, 16: 10})
        
        # Misleading normalization
        normalized_score = score / 100.0
        scaled = normalized_score * weights.get(category, 1)
        
        # Key logic step
        if flags['override_safety'] and code & 8:
            scaled *= 1.5
        
        intermediate_results.append(scaled)
    
    # Secondary processing with slicing distraction
    sliced_part = intermediate_results[::2]  # Every other element - unused
    
    # Actual accumulation
    for val in intermediate_results:
        if val > 4:
            risk_counter += 1
        total_risk += val
    
    # Final formula
    final_index = total_risk * (1 + 0.1 * risk_counter)
    return int(round(final_index))

# Main execution flow
if __name__ == "__main__":
    # Simulated raw sensor input
    sensor_data = [120, 45, 200, 67, 89, 300, 105, 73, 180, 95]
    
    # Irrelevant constants (distractors)
    MAX_BUFFER_SIZE = 256
    TIMEOUT_THRESHOLD = 1500
    RETRY_LIMIT = 3
    
    # Process sensor readings
    processed_data = analyze_sensor_readings(sensor_data, calibration_factor=0.88)
    
    # Build diagnostic log
    diagnostics_log = [
        {'time': 23, 'code': 1, 'type': 'warning'},
        {'time': 42, 'code': 12, 'type': 'critical'},
        {'time': 65, 'code': 16, 'type': 'info'},
        {'time': 78, 'code': 24, 'type': 'critical'},
        {'time': 91, 'code': 5, 'type': 'warning'}
    ]
    
    # System configuration with misleading flag
    system_flags = {
        'debug_mode': True,
        'safe_mode': False,
        'override_safety': True,  # Enables multiplier in aggregation
        'audit_trail': 'enabled'
    }
    
    # Dead code - unreachable function
    def unused_cleanup(data):
        return [x for x in data if x > 0]
    
    # Trigger the key statement
    final_diagnostic = aggregate_diagnostics(diagnostics_log, system_flags)
    print(f"Result: {final_diagnostic}")