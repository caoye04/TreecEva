import itertools

def analyze_performance_log(data):
    # Irrelevant diagnostic function (dead code path)
    return sum(x * 2 for x in data if x > 5)

def bitmask_validate(key):
    # Distractor: Bit manipulation with no effect on main logic
    mask = 0b101010
    return (key ^ mask) & 0b1111 == 8

def recursive_hash(seq):
    # Misleading recursion that's never called
    if len(seq) <= 1:
        return seq[0] if seq else 1
    return seq[0] ^ recursive_hash(seq[1:])

def calculate_thermal_output(units, efficiency_profile):
    total_power = 0
    temp_buffer = []
    
    for unit in units:
        base_output = unit['output']
        status_flag = unit['status']
        
        # Real logic begins: only active units contribute
        if status_flag != 'active':
            continue
            
        # Apply dynamic efficiency modifier from map
        modifier = efficiency_profile.get(unit['type'], 1.0)
        adjusted = base_output * modifier
        
        # Accumulate only if passes checksum (simple bitwise check)
        checksum = (unit['id'] ^ 0xAAAA) & 0xFF
        if checksum % 3 == 0:
            total_power += adjusted
        
        temp_buffer.append(adjusted)
    
    # Summation with conditional inclusion using itertools
    valid_indices = [
i for i in range(len(temp_buffer))
    if (i + 1) % 2 == 1  # Only odd-positioned elements
    ]
    filtered_power = sum(itertools.compress(temp_buffer, 
                                            [(i in valid_indices) for i in range(len(temp_buffer))]))
    
    # Final thermal model applies logarithmic scaling if over threshold
    if filtered_power > 1500:
        import math
        scaled = math.log(filtered_power) * 100
    else:
        scaled = filtered_power + 50
    
    # Red herring: unused transformation
    inverted = [1.0 / (x + 1) for x in temp_buffer if x > 0]
    
    return int(scaled)

# Simulated engine telemetry data (real input)
engines = [
    {'id': 43690, 'output': 420, 'status': 'active', 'type': 'fusion'},
    {'id': 43691, 'output': 380, 'status': 'standby', 'type': 'plasma'},  # skipped
    {'id': 43692, 'output': 510, 'status': 'active', 'type': 'fusion'},
    {'id': 43693, 'output': 490, 'status': 'active', 'type': 'quantum'},
    {'id': 43694, 'output': 320, 'status': 'inactive', 'type': 'fusion'}, # skipped
]

# Efficiency modifiers by type (relevant data)
efficiency_map = {
    'fusion': 1.2,
    'quantum': 1.5,
    'plasma': 1.1
}

# Unused sensor array (distractor)
sensor_readings = [72, 68, 74, 80, 79, 85, 90, 88]
analyze_performance_log(sensor_readings)  # Called but result ignored

# Critical computation
thermal_capacity = calculate_thermal_output(engines, efficiency_map)

# Output result as required
print(f"Result: {thermal_capacity}")