from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def calculate_humidity_index(readings):
    return sum(readings) / len(readings)

# Misleading auxiliary computation
electrical_load = [120, 135, 140, 128, 132]
load_profile = defaultdict(int)
for load in electrical_load:
    load_profile[load // 10] += 1

# Unused statistical transformation
normalized_load = [math.log(load + 1) for load in electrical_load]
mean_load = sum(normalized_load) / len(normalized_load)

# Core system parameters (some are decoys)
system_flags = {'calibrated': True, 'debug_mode': False, 'legacy_mode': False}
scaling_factor = 1.75
legacy_offset = -42  # Never actually used

# Simulated sensor data with red herring fields
data_stream = [
    {'temp': 22.1, 'flow': 1.5, 'phase': 'A', 'noise': 0.03},
    {'temp': 23.0, 'flow': 1.8, 'phase': 'B', 'noise': 0.07},
    {'temp': 24.5, 'flow': 1.6, 'phase': 'A', 'noise': 0.05},
    {'temp': 25.3, 'flow': 2.1, 'phase': 'C', 'noise': 0.09},
    {'temp': 26.0, 'flow': 1.9, 'phase': 'B', 'noise': 0.11}
]

# Decoy aggregation using Counter
phase_counter = Counter(entry['phase'] for entry in data_stream)

# Fake recursive smoothing (not connected to main logic)
def smooth_noise(values, depth=0):
    if depth >= 2:
        return values[0]
    return smooth_noise([v * 0.9 for v in values], depth + 1)

# Real processing begins here
process_stages = []
for entry in data_stream:
    stage = {}
    raw_temp = entry['temp']
    flow_rate = entry['flow']
    
    # Apply physical transformation
    adjusted_temp = raw_temp + (flow_rate * 0.3)
    efficiency_ratio = min(flow_rate / 2.0, 1.0)
    
    # Hidden correction factor based on phase (only A/B/C, no real impact from noise)
    if entry['phase'] == 'A':
        adjusted_temp *= 1.02
    elif entry['phase'] == 'B':
        adjusted_temp *= 1.01
    else:
        adjusted_temp *= 0.99
        
    stage['adjusted_temp'] = adjusted_temp
    stage['efficiency'] = efficiency_ratio
    process_stages.append(stage)

# Secondary transformation with distraction
intermediate_results = []
for i, stage in enumerate(process_stages):
    temp = stage['adjusted_temp']
    # Use of log and trigonometric red herring
    dummy_correction = math.sin(i * 0.5) * math.log(2 + i)
    fake_value = temp * dummy_correction  # Dead calculation
    intermediate_results.append(fake_value)

# Actual core logic: recursive accumulation of thermal effect
def calculate_thermal_output(stages):
    if not stages:
        return 0.0
    
    head = stages[0]
    rest = stages[1:]
    
    base_contribution = head['adjusted_temp'] * head['efficiency'] * scaling_factor
    
    if len(rest) == 0:
        return round(base_contribution, 4)
    
    residual = calculate_thermal_output(rest)
    return round(base_contribution + residual * 0.85, 4)

# Critical assignment point
thermal_capacity = calculate_thermal_output(process_stages)

# Print required result
print(f"Target result: {thermal_capacity}")