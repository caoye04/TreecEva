import itertools

# System calibration constants (some are red herrings)
CALIBRATION_FACTOR = 0.87
OFFSET_ADJUST = -2.1
UNUSED_CONSTANT = 5.6  # Dead constant, never used
MAX_PHASE_SHIFT = 128

# Sensor input data: temperature readings across 3 zones over 4 intervals
readings = [
    [23.5, 24.1, 22.9, 25.3],
    [26.0, 25.8, 26.2, 25.9],
    [21.7, 22.3, 21.9, 22.0]
]

# Misleading auxiliary calculation - appears important but unused later
baseline_avg = sum(sum(zone) for zone in readings) / (len(readings) * len(readings[0]))
evaluated_offsets = [abs(temp - baseline_avg) for temp in itertools.chain(*readings)]
adjusted_readings = [[t * CALIBRATION_FACTOR for t in zone] for zone in readings]  # Looks critical, not actually used

# Phase transition flags based on threshold logic
phase_flags = []
for i, zone in enumerate(readings):
    zone_flags = []
    for temp in zone:
        if temp > 25.5:
            flag = 3  # Overheating phase
        elif temp > 24.0:
            flag = 2  # Elevated phase
        elif temp > 22.0:
            flag = 1  # Normal phase
        else:
            flag = 0  # Subnormal phase
        zone_flags.append(flag)
    phase_flags.append(zone_flags)

# Simulate system state with bit-encoded status (3-4 levels of logic)
active_sensors = 0b101
maintenance_mode = 0b010
system_state = active_sensors ^ maintenance_mode  # XOR to toggle diagnostic mode

if system_state & 0b001:
    system_state |= 0b1000  # Enable extended logging

# Aggregate phase transitions using bitwise accumulation
aggregate_phases = 0
for flags in phase_flags:
    for f in flags:
        aggregate_phases ^= (f << 2)  # Scramble using XOR shift
        aggregate_phases += (f % 3)     # Add modulo noise
        aggregate_phases &= 0b111111   # Clamp to 6 bits

# Decoy function - looks relevant but never called
def compute_entropy(data):
    import math
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Real transformation function (called once)
def adjust_thermal(phase_sum, state):
    modifier = 1.0
    if state & 0b1000:
        modifier *= 1.15
    if state & 0b0100:
        modifier *= 0.90
    
    # Complex adjustment with red herring operations
    temp_val = phase_sum * 3.2
    temp_val -= OFFSET_ADJUST  # Uses distracting global
    temp_val += (state & 0b11) * 0.5
    
    # Apply non-linear correction
    temp_val = abs(temp_val) ** 0.9
    
    # Irrelevant branching based on parity
    if temp_val % 2 == 0:
        temp_val += 1.0  # Never reached due to decimal result
    
    return round(temp_val, 4)

# Secondary decoy: advanced filtering that isn't used
denoised = [
    list(itertools.compress(zone, (t >= 22.0 for t in zone)))
    for zone in readings
]

# Key computation
thermal_capacity = adjust_thermal(aggregate_phases, system_state)

# Output requirement
print(f"Result: {thermal_capacity}")