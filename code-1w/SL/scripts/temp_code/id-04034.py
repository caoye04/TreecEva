import itertools

def analyze_system_performance():
    # System parameters
    base_frequency = 12
    modulation_factor = 3
    tolerance_threshold = 0.05
    calibration_sequence = [1, 2, 3, 5, 8, 13]
    
    # Simulated sensor readings (with noise)
    raw_readings = [14.2, 13.9, 14.5, 13.7, 14.1, 14.3, 13.8]
    filtered_readings = [x for x in raw_readings if abs(x - 14.0) < 0.6]
    
    # Auxiliary tracking variables (some are distractions)
    temp_buffer = []
    diagnostic_log = {}
    anomaly_count = 0
    total_power_draw = 0.0
    
    # Core process cycles
    cycle_count = 0
    total_output = 0
    efficiency_score = 0
    
    # Simulate processing under varying loads
    for load in range(1, 6):
        cycle_count += 1
        
        # Complex workload pattern generation
        workload_patterns = list(itertools.product([load], [2, 3]))
        pattern_sum = sum(a * b for a, b in workload_patterns)
        
        # Red herring computation: power draw simulation (not used in final score)
        segment_power = base_frequency * load * 0.87
        total_power_draw += segment_power
        
        # Actual output contribution
        output_contribution = 0
        for i, val in enumerate(calibration_sequence):
            if i >= load:
                break
            offset = (val + modulation_factor) ** 2 % 7
            output_contribution += offset
        
        # Update total output
        total_output += pattern_sum + int(output_contribution)
        
        # Logging (distraction)
        temp_buffer.append((load, segment_power, output_contribution))
        diagnostic_log[f'cycle_{load}'] = {'status': 'ok', 'power': segment_power}
        
        # Unnecessary conditional check (dead logic path)
        if load == 10:
            anomaly_count += 1  # Never reached

    # Key statement: compute final efficiency score
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Extra irrelevant transformation
    normalized_diagnostic = {k: v for k, v in diagnostic_log.items() if 'cycle_2' not in k}
    
    # Final result output
    print(f"Result: {efficiency_score}")

analyze_system_performance()