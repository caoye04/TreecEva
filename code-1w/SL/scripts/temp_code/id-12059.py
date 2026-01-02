from itertools import compress, cycle

# System configuration for a distributed sensor network
def normalize_readings(readings):
    avg = sum(readings) / len(readings)
    return [round(x / avg, 3) for x in readings]

# Irrelevant helper: simulates noise filtering (not used in final logic)
def apply_noise_filter(data_stream):
    filtered = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            filtered.append(val * 0.95)
        else:
            filtered.append(val)
    return filtered

# Core capacity calculation
def calculate_unit_load(base, mode, flags):
    load = base * 1.1
    if mode == 'high':
        load *= 1.3
    elif mode == 'low':
        load *= 0.7
    # Apply binary flag modulation (bitwise distraction)
    flag_value = flags.get('mod', 0)
    if flag_value & 1:
        load += 5
    if flag_value >> 1 & 1:
        load -= 3
    return round(load, 2)

def calculate_system_capacity(sensor_units, efficiency_lookup):
    loads = []n    modes = ['normal', 'high', 'low']
    mode_cycle = cycle(modes)
    
    temp_buffer = []  # Distractor: accumulates unused diagnostics
    for unit in sensor_units:
        uid = unit['id']
        base = unit['base_power']
        mode = unit.get('mode', 'normal')
        flags = unit.get('flags', {})
        
        raw_load = calculate_unit_load(base, mode, flags)
        
        # Real computation path
        efficiency_key = f"sensor_{uid % 3}"
        efficiency_factor = efficiency_lookup.get(efficiency_key, 1.0)
        adjusted_load = raw_load * efficiency_factor
        loads.append(adjusted_load)
        
        # Distractor: irrelevant diagnostic snapshot
        if uid % 5 == 0:
            temp_buffer.append(f"Diag-{uid}:{round(raw_load,1)}")
    
    # Actual result computation
    total_load = sum(loads)
    peak_factor = efficiency_lookup.get('peak_factor', 1.0)
    system_health = efficiency_lookup.get('health', 'optimal')
    health_factor = 0.9 if system_health == 'degraded' else 1.0
    
    # Final capacity formula
    capacity = total_load * peak_factor * health_factor
    
    # Dead code branch (misleading)
    if len(temp_buffer) > 10:
        capacity *= 0.95  # Never reached due to input size
    
    return int(capacity)

# Input data setup
sensor_readings = [102, 97, 108, 95, 110, 101, 99, 104]
normalized = normalize_readings(sensor_readings)  # Used only to seed unit base values

units = [
    {'id': 101, 'base_power': 85 + int(normalized[0]), 'mode': 'high', 'flags': {'mod': 3}},
    {'id': 102, 'base_power': 70 + int(normalized[1]), 'mode': 'normal'},
    {'id': 103, 'base_power': 90 + int(normalized[2]), 'mode': 'low', 'flags': {'mod': 1}},
    {'id': 104, 'base_power': 78 + int(normalized[3])},
    {'id': 105, 'base_power': 88 + int(normalized[4]), 'mode': 'high'}
]

# Efficiency characteristics
efficiency_map = {
    'sensor_0': 1.15,
    'sensor_1': 0.95,
    'sensor_2': 1.05,
    'peak_factor': 1.2,
    'health': 'optimal'
}

# Simulate auxiliary monitoring (irrelevant to final answer)
data_stream = [101, 99, 103, 100, 98]
filtered_data = apply_noise_filter(data_stream)
diagnostic_codes = list(compress(range(1000, 1050), cycle([1,0,0])))  # Unused list

# Key execution point
final_capacity = calculate_system_capacity(units, efficiency_map)
print(f"Result: {final_capacity}")