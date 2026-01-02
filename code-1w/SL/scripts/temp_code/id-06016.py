def analyze_stress_levels(readings):
    cumulative_stress = 0
    for val in readings:
        if val > 75:
            cumulative_stress += val * 0.3
        elif val > 50:
            cumulative_stress += val * 0.1
    return cumulative_stress

# Irrelevant sensor calibration data (distractor)
calibration_map = {i: (i * 1.05 + 2) for i in range(10, 40)}
baseline_offset = sum(calibration_map.values()) / len(calibration_map)

# Simulate redundant preprocessing (dead path)
def preprocess_signal(data):
    return [x * 1.01 for x in data if x > 0]  # never called

# Real input data
sensor_readings = [45, 82, 67, 91, 53]

# Misleading intermediate transformation (red herring)
filtered_readings = [x for x in sensor_readings if x > 60]
aggregated_diagnostic = sum(filtered_readings) * 0.7  # looks important, unused

# Core logic obscured by abstraction
stress_factor = analyze_stress_levels(sensor_readings)

# Bit manipulation decoy (irrelevant)
mystery_flag = 0b101010
mystery_flag ^= 0b111111
mystery_flag &= 0b001100  # result unused

base_yield = 420

# Conditional expression with distractor condition
adjustment_hint = 'high' if stress_factor > 100 else 'low'
dummy_dict = {'mode': 'legacy', 'threshold': 95, 'debug': True}

# Key function with multiple concepts
def adjust_efficiency(yield_val, stress):
    efficiency_map = {
        'low': 0.95,
        'medium': 0.82,
        'high': 0.70
    }
    
    # Set operation red herring
    observed_levels = set(sensor_readings)
    critical_set = {x for x in observed_levels if x > 80}
    suppression_factor = 0.9 if len(critical_set) >= 2 else 1.0  # misleading!

    base_efficiency = efficiency_map[adjustment_hint]
    
    # Actual calculation buried in logic
    adjusted = yield_val * base_efficiency
    
    # Early return decoy (never triggers due to data)
    if yield_val < 100:
        return adjusted * 0.5
        
    # Real adjustment
    if stress > 80:
        adjusted *= 0.93  # additional degradation
    
    return int(adjusted)

# Critical execution point
thermal_output = adjust_efficiency(base_yield, stress_factor)

# Output result as required
print(f"Result: {thermal_output}")