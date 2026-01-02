def analyze_readings(sensor_data, config):
    temp_cache = []
    for idx, reading in enumerate(sensor_data):
        if idx % 3 == 0:
            temp_cache.append(reading * 1.05)
        elif idx % 4 == 0:
            temp_cache.append(reading * 0.95)
        else:
            temp_cache.append(reading)

    adjusted = [round(x, 2) for x in temp_cache]
    return adjusted


def generate_thresholds(base_levels):
    decoy_map = {k: v**2 for k, v in base_levels.items()}
    valid_map = {k: max(5, int(v / 2.5)) for k, v in base_levels.items()}
    extra_calc = sum(decoy_map.values()) // len(decoy_map)  
    return valid_map


def collect_diagnostics(log_series, rules):
    diagnostic_set = set()
    for i, entry in enumerate(log_series):
        for j, char in enumerate(entry):
            if char.isdigit():
                diagnostic_set.add(i + j + int(char))
    
    filtered = {x for x in diagnostic_set if x % 2 == 1}
    return list(filtered)


def merge_signals(primary, secondary):
    merged = []
    for p, s in zip(primary, secondary):
        merged.append(p + s)
    return merged


def process_metrics(sequence, thresholds):
    accumulator = 0
    history = []
    
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            accumulator += val * thresholds.get('T1', 1)
        elif i % 3 == 0:
            accumulator -= val // thresholds.get('T2', 2)
        else:
            accumulator += (val + i) % thresholds.get('T3', 3)
        
        if accumulator > 100:
            accumulator = accumulator // 2
        
        history.append(abs(accumulator))
    
    outlier_check = [h for h in history if h > 80]
    if len(outlier_check) > 2:
        final_score = sum(history) // len(history)
    else:
        final_score = history[-1] + len(history)
    
    return final_score

# Irrelevant initialization block (red herring)
data_log = ['err01', 'log2', 'chk3', 'dbg0', 'cap5']
base_config = {'gain': 10, 'offset': 5, 'scale': 8}
decoys = [x * 2 for x in range(10)]  

# Core execution path begins here
calibration_input = [12, 18, 27, 14, 33, 21, 16, 25]
threshold_params = {'T1': 3, 'T2': 4, 'T3': 5}

# Step 1: Adjust sensor readings
calibration_sequence = analyze_readings(calibration_input, base_config)

# Step 2: Generate valid thresholds (ignore decoy_map inside function)
threshold_map = generate_thresholds(threshold_params)

# Step 3: Create dummy diagnostics (unused result)
diag_results = collect_diagnostics(data_log, {'rule_a': 1})

# Step 4: Merge with dummy signal (irrelevant to final result)
dummy_signal = [1 for _ in calibration_sequence]
merged_trace = merge_signals(calibration_sequence, dummy_signal)

# Step 5: Process metrics to compute final diagnostic
final_diagnostic = process_metrics(calibration_sequence, threshold_map)

print(f"Result: {final_diagnostic}")