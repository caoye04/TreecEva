from collections import defaultdict, Counter

# Simulated sensor data from wind turbine array
turbine_data = [
    [104, 110, 120, 98, 105],
    [97, 103, None, 101, 99],
    [112, 115, 118, 111, 114],
    [None, 95, 93, 97, 96],
    [125, 127, 126, 124, 128]
]

# Fault codes from diagnostic subsystem (1 = minor, 2 = critical)
fault_codes = [0, 2, 1, 0, 2]

# Irrelevant auxiliary data (distractor)
system_logs = [
    {'timestamp': '10:01', 'event': 'OK'},
    {'timestamp': '10:02', 'event': 'WARNING'},
    {'timestamp': '10:03', 'event': 'OK'},
    {'timestamp': '10:04', 'event': 'ERROR'},
    {'timestamp': '10:05', 'event': 'OK'}
]

# Dead computation path: processes logs but never used
def analyze_logs(logs):
    count = defaultdict(int)
    for log in logs:
        count[log['event']] += 1
    return count

log_analysis = analyze_logs(system_logs)  # Unused result

# Misleading intermediate calculation (distractor)
avg_log_interval = sum((int(log['timestamp'].split(':')[1]) 
                        for log in system_logs)) / len(system_logs)

# Real processing begins here
status_map = {0: 'normal', 1: 'warning', 2: 'critical'}
fault_flags = [status_map[code] for code in fault_codes]

# Decoy function that looks important but isn't used in final path
def calculate_variance(data):
    mean = sum(x for x in data if x is not None) / len([x for x in data if x is not None])
    return sum((x - mean) ** 2 for x in data if x is not None)

# Another decoy: builds structure but unused
turbine_profiles = {}
for i, readings in enumerate(turbine_data):
    valid_readings = [r for r in readings if r is not None]
    if valid_readings:
        turbine_profiles[f'turbine_{i}'] = {
            'min': min(valid_readings),
            'max': max(valid_readings),
            'range': max(valid_readings) - min(valid_readings)
        }

# Key data transformation with distractors
adjusted_averages = []
for idx, (readings, flag) in enumerate(zip(turbine_data, fault_flags)):
    # Extract only non-null sensor values
    clean_readings = [r for r in readings if r is not None]
    
    # Distractor: this modifies local state but doesn't affect outcome
    if flag == 'critical' and clean_readings:
        baseline = sum(clean_readings) / len(clean_readings)
        adjusted = [r * 0.95 for r in clean_readings]  # Simulate correction
    else:
        adjusted = clean_readings
    
    # Actual relevant computation
    if adjusted:
        avg = sum(adjusted) / len(adjusted)
        adjusted_averages.append(avg)

# Another red herring: complex bit manipulation on fault flags
bit_encoded = 0
for i, flag in enumerate(fault_flags):
    shift = {'normal': 0, 'warning': 1, 'critical': 2}[flag]
    bit_encoded |= (i + 1) << (shift * 4)

# Unused nested comprehension (dead code path)
recovery_sequences = {
    f'turbine_{i}': [
        (j, val * (1.05 if flag == 'critical' else 1))
        for j, val in enumerate(turbine_data[i])
        if val is not None
    ]
    for i, flag in enumerate(fault_flags)
}

# Core logic buried among distractions
def aggregate_metrics(data, flags):
    # Use Counter to track contribution weights by fault status
    weight_counter = Counter()
    total_contribution = 0.0
    total_weight = 0
    
    for readings, status in zip(data, flags):
        clean_vals = [r for r in readings if r is not None]
        if not clean_vals:
            continue
            
        # Assign weights based on fault severity
        weight = {'normal': 1, 'warning': 2, 'critical': 3}[status]
        weight_counter[status] += weight
        
        raw_avg = sum(clean_vals) / len(clean_vals)
        weighted_avg = raw_avg * weight
        total_contribution += weighted_avg
        total_weight += weight
    
    # Final metric is total weighted average
    final_score = total_contribution / total_weight if total_weight else 0
    
    # Secondary metric derived from distribution
    all_avgs = [
        sum(r for r in row if r is not None) / len([r for r in row if r is not None])
        for row in data
    ]
    stability_penalty = max(all_avgs) - min(all_avgs)
    
    # The real answer combines both
    return int(final_score - stability_penalty)

# Execution point of interest
final_diagnostic = aggregate_metrics(turbine_data, fault_flags)
print(f"Target result: {final_diagnostic}")