import itertools

# Simulated sensor data from wind turbine array
turbine_ids = ['WT-01', 'WT-02', 'WT-03', 'WT-04']
sensor_readings = [
    [120, 85, 134, 92],  # Power output (kW)
    [78, 76, 82, 79],     # Gearbox temperature (°C)
    [14, 16, 15, 18],     # Vibration index
    [98, 95, 97, 96]      # Efficiency (%)
]

# Irrelevant baseline comparison set
dummy_readings = [[x**2 % 100 for x in range(10)] for _ in range(4)]

def normalize(data):
    # Distractor function – not used in critical path
    return [round(x / sum(data), 4) for x in data]

def rolling_average(values, window=2):
    # Another distractor – looks useful but unused
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def bitmask_anomaly(vibration_levels):
    # Bit manipulation red herring
    mask = 0
    for idx, val in enumerate(vibration_levels):
        if val > 15:
            mask |= (1 << idx)
    return mask  # Unused result

def validate_calibration(log_entries):
    # Dead code path – never called
    status = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            status += 1
    return status == 0

# Decoy data structure
calibration_log = [
    "CAL:WT-01:OK", "ERR:WT-02:SENSOR_TAMPER", 
    "CAL:WT-03:OK", "WARN:WT-04:DRIFT_DETECTED"
]

# Real processing begins here
turbine_data = dict(zip(turbine_ids, zip(*sensor_readings)))

# Extract primary metrics per turbine
power_outputs = [turbine_data[tid][0] for tid in turbine_ids]
efficiency_rates = [turbine_data[tid][3] for tid in turbine_ids]

# Misleading intermediate calculation
weighted_avg_efficiency = round(
    sum(efficiency_rates[i] * (power_outputs[i] / sum(power_outputs)) 
         for i in range(4)), 3)

# Thresholds for health check (real logic starts)
thresholds = {
    'overheat': 80,
    'vibration_cap': 17,
    'efficiency_floor': 95,
    'output_range': (90, 135)
}

# Secondary decoy transformation
shifted_temps = [(turbine_data[tid][1] + 5) % 100 for tid in turbine_ids]

# Core diagnostic logic with multiple concepts
healthy_count = 0
for tid, readings in turbine_data.items():
    temp, vib, eff = readings[1], readings[2], readings[3]
    output = readings[0]
    
    # Logical and relational comparisons with short-circuiting
    is_stable = (temp <= thresholds['overheat']) and \
                 (vib < thresholds['vibration_cap']) and \
                 (eff >= thresholds['efficiency_floor'])
    
    within_output = thresholds['output_range'][0] <= output <= thresholds['output_range'][1]
    
    # Integer division distractor
    proxy_health = output // (vib + 1)
    
    if is_stable and within_output:
        healthy_count += 1

# Bitwise operation red herring
status_flag = healthy_count ^ 7
status_flag = status_flag & 15 | 1

# Real aggregation using itertools and string ops
operational_codes = [f"OP-{str(i+1).zfill(2)}" for i in range(healthy_count)]
code_concat = ''.join(itertools.chain.from_iterable(zip(*operational_codes)))

def aggregate_metrics(data_dict, limits):
    # Final computation – combines arithmetic, logic, and summation
    total_power = 0
    penalty = 0
    
    for turbine_id, vals in data_dict.items():
        power, temp, vib, eff = vals
        
        # Multiple conditionals with nested logic
        if power < limits['output_range'][0]:
            penalty += 10
        elif power > limits['output_range'][1]:
            penalty += 15
        
        if temp > limits['overheat']:
            penalty += 5 * (temp - limits['overheat'])
        
        if vib >= limits['vibration_cap']:
            # XOR-based penalty weighting (actual use)
            penalty += 20 - (vib ^ 14)
        
        if eff < limits['efficiency_floor']:
            # String method distraction inside logic
            reason = "low_efficiency".upper().replace('_', ' ')
            penalty += 3
        
        total_power += power
    
    # Final formula: complex interaction
    base_score = total_power * 0.85
    adjusted = base_score - (penalty ** 1.5)
    
    # Key answer computation
    final_diagnostic = int(round(adjusted + 100))
    
    # Unused but plausible-looking derivative
    normalized_index = round(adjusted / (total_power * 0.9), 6)
    
    return final_diagnostic

# Execute main logic
final_diagnostic = aggregate_metrics(turbine_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")