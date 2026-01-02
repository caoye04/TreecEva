from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def dummy_normalization(data):
    return [x / sum(data) for x in data if x > 0]

# Misleading intermediate computation
temp_offsets = [0.1, -0.2, 0.3, -0.4]
offset_correction = sum([abs(x) for x in temp_offsets]) * 0.5

# Simulated sensor readings with noise (distractor)
sensor_data = [23.4, 25.1, 22.8, 26.3, 24.9]
valid_readings = [x for x in sensor_data if 20 <= x <= 30]
avg_reading = sum(valid_readings) / len(valid_readings) if valid_readings else 0

# System configuration map (partially relevant)
config_params = {
    'threshold': 0.75,
    'mode': 'turbo',
    'version': '2.1a'
}

# Efficiency lookup with nested structure (relevant)
efficiency_map = defaultdict(lambda: defaultdict(float))
efficiency_map['high']['A'] = 0.88
efficiency_map['high']['B'] = 0.76
efficiency_map['low']['A'] = 0.54
efficiency_map['low']['B'] = 0.42

# Process flags influencing thermal behavior (relevant)
process_flags = [
    {'type': 'A', 'load': 'high', 'active': True, 'priority': 1},
    {'type': 'B', 'load': 'high', 'active': False, 'priority': 3},
    {'type': 'A', 'load': 'low', 'active': True, 'priority': 2}
]

# Decoy statistical calculation (irrelevant)
data_counts = Counter([p['type'] for p in process_flags])
total_types = sum(data_counts.values())
entropy = -sum((count/total_types) * math.log2(count/total_types) for count in data_counts.values())

# Auxiliary transformation matrix (red herring)
transform_matrix = [
    [1.1, -0.1],
    [0.05, 1.15]
]

# Fake optimization pass (dead code)
def optimize_schedule(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['priority'])
    return [t for t in sorted_tasks if t['active']]

scheduled = optimize_schedule(process_flags)

# Core calculation logic (relevant)
def apply_efficiency(flag, e_map):
    load = flag['load']
    typ = flag['type']
    base_eff = e_map[load][typ]
    adjustment = 0.1 if flag['active'] and load == 'high' else 0.05
    return base_eff + adjustment

def calculate_thermal_properties(flags, e_map):
    total_weight = 0.0
    composite_score = 0.0
    
    for flag in flags:
        if not flag['active']:
            continue
            # Following lines are unreachable (misleading)
            redundant_calc = flag['priority'] ** 2
            total_weight += redundant_calc
        
        raw_eff = apply_efficiency(flag, e_map)
        priority_factor = max(1, 3 - flag['priority'])  # Boost higher priority
        contribution = raw_eff * priority_factor
        
        if flag['load'] == 'high':
            # Additional turbo mode boost
            if config_params['mode'] == 'turbo':
                contribution *= 1.15
            
        composite_score += contribution
    
    # Final nonlinear scaling (key step)
    scaled = math.log2(composite_score + 1) * 100
    
    # Red herring: unused transformation
    normalized_scaled = scaled / (math.pi * offset_correction) if offset_correction else scaled
    
    return int(scaled)  # Discretized capacity

# Trigger point: this assignment contains the answer
temperature_buffer = [avg_reading] * 3
thermal_capacity = calculate_thermal_properties(process_flags, efficiency_map)

# Spurious post-processing (irrelevant)
if len(temperature_buffer) > 2:
    smoothed_temp = sum(temperature_buffer[-3:]) / 3
    temperature_buffer.append(smoothed_temp * 1.05)

# Output the target result
print(f"Result: {thermal_capacity}")