import math

# Simulated sensor array diagnostics with irrelevant auxiliary data
def analyze_sensor_health(raw_logs):
    cumulative_score = 0
    for log in raw_logs:
        if len(log) > 3:
            cumulative_score += ord(log[0]) - ord('A')
    return cumulative_score

# Irrelevant function: computes unused spectral weight
def compute_spectral_weight(data):
    weight = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            weight += math.sin(val / 10) * 1.5
    return round(weight, 4)

# Core transformation: normalize and filter sensor readings
def normalize_readings(readings):
    normalized = []
    base_offset = sum(readings) / len(readings)
    for val in readings:
        adjusted = val - base_offset + 2.5
        normalized.append(round(adjusted, 3))
    return normalized

# Misleading aggregation: uses dead logic path
def aggregate_diagnostics(metrics):
    temp_result = 0
    for i, (k, v) in enumerate(sorted(metrics.items())):
        if v > 10:
            temp_result += i * v
    # This function is never actually used in critical path
    return temp_result

# Key processing function with conditional logic and distractors
def process_readings(data, thresholds):
    temp_cache = {}
    result_stack = []
    
    for idx, reading in enumerate(data):
        key = chr(ord('X') + (idx % 3))
        temp_cache[key] = temp_cache.get(key, 0) + abs(reading)
        
        # Real logic: apply threshold logic from map
        category = 'A' if reading < thresholds['low'] else 'B' if reading < thresholds['med'] else 'C'
        
        # Conditional expression determining flow
        score = reading * 1.75 if category == 'A' else (reading * 0.85 if category == 'B' else reading * 0.35)
        
        # Bit manipulation red herring
        masked = int(score) & 0xFF
        if masked > 100:
            masked = masked ^ 0xAA
        
        result_stack.append(round(score - masked * 0.1, 3))
    
    # Actual answer derivation (non-obvious)
    final_value = 0
    for i, v in enumerate(result_stack):
        if i % 2 == 0:
            final_value += v * (i + 1)
    
    return int(round(final_value))

# Unused recursive decoy function
def trace_path_recursive(node, visited=None):
    if visited is None:
        visited = []
    if node < 2:
        return [node]
    return trace_path_recursive(node - 1, visited) + [node]

# Main execution block with distractions
if __name__ == "__main__":
    # Real input data
    sensor_readings = [12.5, 8.3, 15.7, 6.9, 23.1, 9.4, 11.0, 5.5]
    
    # Distractor variables
    calibration_matrix = [[1.1, 0.9], [1.05, 0.98], [1.02, 0.99]]
    metadata_log = ['SYS_OK', 'INIT_DONE', 'MODE_A', 'VER_2.1']
    debug_trace = {f"step_{i}": False for i in range(5)}
    
    # Irrelevant slicing operation
    window_slice = sensor_readings[2:6:2]
    
    # Normalize real data
    processed_values = normalize_readings(sensor_readings)
    
    # Filtering based on dynamic condition (real step)
    filtered_data = [val for val in processed_values if abs(val) > 1.5]
    
    # Threshold map used in actual computation
    threshold_map = {
        'low': 3.0,
        'med': 7.5,
        'high': 12.0
    }
    
    # Dead code path: unused aggregation
    metrics_summary = {
        'power': 12.4,
        'signal': 9.8,
        'noise': 6.1,
        'drift': 14.3
    }
    unused_diag = aggregate_diagnostics(metrics_summary)
    
    # Critical statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")