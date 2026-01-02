import itertools

# Simulated sensor array diagnostics with mixed data types and red herrings
def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing (distractor)
    normalized = [x * calibration_factor for x in raw_readings if x > 0]
    filtered_peaks = list(filter(lambda x: x > 0.7 * max(normalized), normalized))
    
    # Dead code path - never executed due to condition (misleading)
    anomaly_score = 0
    if len(filtered_peaks) > 100:
        anomaly_score = sum(itertools.islice(itertools.cycle([1.5]), len(filtered_peaks)))

    # Core relevant transformation (subtle due to noise)
    shifted = [(x * 1.08 + 2.3) for x in raw_readings]
    categorized = []
    for val in shifted:
        if val < 15.0:
            categorized.append(('low', val))
        elif val < 30.0:
            categorized.append(('medium', val))
        else:
            categorized.append(('high', val))
    
    # Distractor: complex but unused data structure
    history_log = [{'entry_id': i, 'value': v, 'status': 'reviewed'} 
                   for i, v in enumerate(itertools.accumulate(normalized[:10]))]
    
    return categorized

# Secondary transformation with decoy logic
def apply_correction(profile, mode='standard'):
    corrected = []
    temp_cache = []  # Unused cache (red herring)
    
    for category, value in profile:
        if category == 'low':
            corrected.append(value * 0.95)
        elif category == 'medium':
            corrected.append(value * 1.02)
        elif category == 'high':
            # Early exit that looks important but isn't triggered here
            if value > 50:
                return [0.0] * len(corrected)
            corrected.append(value * 1.1)
    
    # Decoy operation chain
    if mode == 'aggressive':
        corrected = [x + 1.5 for x in corrected]
    
    # Never used function inside function (dead abstraction)
    def validate_stability(data):
        return all(x > 0 for x in data)
    
    return corrected

# Final processing with conditional branching distraction
def process_metrics(signal, config_map):
    base_values = signal
    adjustment = config_map.get('sensitivity', 1.0)
    offset = config_map.get('baseline_offset', 0.0)
    
    # Real computation buried in multiple operations
    adjusted = [round(x * adjustment + offset, 4) for x in base_values]
    
    # Misleading statistical diversion
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    
    # Critical early break in loop that affects result (key logic step)
    final_sum = 0
    for idx, val in enumerate(adjusted):
        contribution = val * (0.95 ** idx)
        if contribution < 0.5:
            break  # This break is essential for correct answer
        final_sum += contribution
    
    # Dead branch with plausible-looking calculation
    if variance_proxy > 100:
        final_sum *= 0.8
    
    return round(final_sum, 4)

# Orchestration with irrelevant setup
if __name__ == '__main__':
    # Input data - realistic sensor readings
    sensor_input = [8.5, 12.3, 14.1, 18.7, 22.5, 26.8, 31.0, 35.2, 38.9, 42.1, 45.3]
    
    # Unused alternative configurations (distractors)
    alt_configs = {
        'mode_a': {'sensitivity': 1.3, 'baseline_offset': -2.0},
        'mode_b': {'sensitivity': 0.9, 'baseline_offset': 1.5},
        'debug_mode': {'sensitivity': 1.0, 'baseline_offset': 0.0, 'extra_flag': True}
    }
    
    # Relevant configuration map
    threshold_map = {'sensitivity': 1.15, 'baseline_offset': -1.8}
    
    # Chain execution with intermediate results that look important
    stage_one = analyze_sensor_array(sensor_input, calibration_factor=1.05)
    transformed_data = apply_correction(stage_one, mode='standard')
    
    # Key statement containing the answer
    final_diagnostic = process_metrics(transformed_data, threshold_map)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")