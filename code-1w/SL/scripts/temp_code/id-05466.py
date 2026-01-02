import itertools

# Sensor array simulation with noise masking and calibration logic
def collect_sensor_data(base_signal, noise_level=0.1):
    return [base_signal + i * noise_level for i in range(8)]

# Irrelevant auxiliary function - decoy for signal smoothing (dead path)
def smooth_signal(data, passes=2):
    temp = data.copy()
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[(i+1) % len(temp)]) / 3 for i in range(len(temp))]
    return temp

# Core transformation: apply non-linear response curve to sensor inputs
def apply_response_curve(val):
    if val < 0.5:
        return val ** 3
    elif val < 2.0:
        return val ** 1.5
    else:
        return val * 2 - 1

# Data masking based on dynamic threshold (partially relevant)
def mask_outliers(data, threshold_multiplier=1.5):
    median_val = sorted(data)[len(data)//2]
    mad = sorted([abs(x - median_val) for x in data])[len(data)//2]  # Median Absolute Deviation
    limit = threshold_multiplier * mad
    return [x if abs(x - median_val) <= limit else median_val for x in data]

# Red herring: simulate thermal drift compensation (unused in final chain)
def compensate_thermal_drift(data, ambient_temp=25.0):
    drift_factor = 0.02 * (ambient_temp - 20)
    return [x * (1 - drift_factor) for x in data]

# Key processing: transform valid readings into diagnostic metric
def process_readings(data):
    transformed = list(map(lambda x: apply_response_curve(x), data))
    amplified = [val * 1.75 for val in transformed]
    return sum(itertools.accumulate(amplified, lambda a, b: a * 0.9 + b))

# Main execution flow
if __name__ == "__main__":
    raw_readings = collect_sensor_data(0.8, noise_level=0.05)
    
    # Apply outlier masking (relevant)
    cleaned_readings = mask_outliers(raw_readings, threshold_multiplier=1.8)
    
    # Simulate redundant validation checks (distractors)
    validation_flags = []
    for idx, reading in enumerate(cleaned_readings):
        flag = (idx % 2 == 0) and (reading > 0.5)
        validation_flags.append(flag)
    
    # Dummy correction pass (misleading intermediate result)
    corrected_readings = [val * 0.98 for val in cleaned_readings if val > 0.4]
    secondary_adjustment = sum(corrected_readings[:3]) / 3
    
    # Final filtering based on position (key relevance)
    filtered_data = [cleaned_readings[i] for i in range(len(cleaned_readings)) if validation_flags[i]]
    
    # Unused diagnostic branch - dead code path
    if sum(cleaned_readings) > 8.0:
        baseline_offset = 0.25
        adjusted_offsets = [baseline_offset * (i % 3) for i in range(6)]
    else:
        adjusted_offsets = [0] * 6
    
    # Critical computation step
    final_diagnostic = process_readings(filtered_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")