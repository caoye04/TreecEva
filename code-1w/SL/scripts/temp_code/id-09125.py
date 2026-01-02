from collections import defaultdict, Counter
import math

# Simulated sensor readings (irrelevant data)
sensor_data = [104, 112, 95, 104, 117, 95, 104, 123, 112]
frequency_map = Counter(sensor_data)
spurious_sum = sum(x * 2 for x in frequency_map.keys() if x > 100)

# Engine diagnostic system
def analyze_engine_stability(metrics):
    cumulative_score = 0
    for i, val in enumerate(metrics):
        if i % 3 == 0:
            cumulative_score += int(math.sqrt(val))
        elif val % 2 == 0:
            cumulative_score -= (val % 7)
    return cumulative_score

# Red herring function - never called
def deprecated_calibration(sequence):
    adjustment = 0
    for x in sequence:
        adjustment = (adjustment << 1) ^ x
    return adjustment % 19

# Core logic disguised among distractions
def evaluate_combustion_efficiency(rpm, temp, load):
    base = rpm // 100
    factor = 1 if temp > 85 else 0.5
    penalty = 2 if load > 75 else 0
    return (base * factor) - penalty

# Another decoy: signal processing (unused)
raw_signals = [0.8, 1.2, 0.9, 1.5]
filtered = [x for x in raw_signals if x > 1.0]
signal_baseline = sum(filtered) / len(filtered) if filtered else 0.0

engine_modes = ['idle', 'cruise', 'boost', 'idle', 'cruise']
mode_count = defaultdict(int)
for mode in engine_modes:
    mode_count[mode] += 1

# Critical status variables
engine_rpm = 3600
engine_temp = 92
engine_load = 68
current_phase = "combustion_cycle_3"

temp_history = [88, 90, 89, 92, 91]
stable_threshold = all(th > 85 for th in temp_history[-3:])

# Misleading intermediate calculation
diagnostic_code = 0
for ch in current_phase:
    diagnostic_code += ord(ch) % 5

diagnostic_code = (diagnostic_code % 100) + 1000  # Fake error code

# Primary control flow with nested logic
if engine_rpm > 3000 and stable_threshold:
    efficiency = evaluate_combustion_efficiency(engine_rpm, engine_temp, engine_load)
    if efficiency > 25:
        status_flag = 0b1010
    elif efficiency > 15:
        status_flag = 0b0110
    else:
        status_flag = 0b0010

    # Bit manipulation distraction
    masked_flag = status_flag & 0b1101
    shifted_flag = (masked_flag << 2) | (masked_flag >> 2)

    # Key branching logic
    if bin(shifted_flag).count('1') > 3:
        engine_status = 'optimal'
    elif shifted_flag % 3 == 0:
        engine_status = 'degraded'
    else:
        engine_status = 'nominal'
else:
    engine_status = 'inactive'

# Unused list comprehension red herring
reindexed = [i * 2 for i in range(len(temp_history)) if temp_history[i] < 90]
aggregate_offset = sum(reindexed) - len(reindexed)

# Function that appears important but only used once
memory_buffer = [0] * 5
def calculate_thermal_rating(status):
    base_rating = 0
    if status == 'optimal':
        base_rating = 97
    elif status == 'nominal':
        base_rating = 76
    else:
        base_rating = 63
    
    # Apply dynamic modifiers
    modifier = 1.0
    if engine_temp > 90:
        modifier += 0.1
    if engine_load < 70:
        modifier -= 0.05
    
    # Spurious bitwise adjustment
    adjusted = int(base_rating * modifier)
    adjusted = (adjusted ^ 0xA) & 0xFF  # Obfuscation
    adjusted = (adjusted + (adjusted & 0x3))  # Minor increment

    # Final nonlinear transformation
    final_rating = int((adjusted ** 1.05) - (engine_rpm / 600))
    
    # Dead code branch (never executes due to logic above)
    if final_rating < 0:
        recovery_state = [0]
        for _ in range(3):
            recovery_state[0] += 10
        final_rating = abs(final_rating)
    
    return final_rating

# Additional irrelevant counters
event_log = ['start', 'calibrate', 'start', 'update']
log_counter = Counter(event_log)
total_events = sum(log_counter.values())

# Trigger the key computation
thermal_capacity = calculate_thermal_rating(engine_status)

# Print required result
Target result: {thermal_capacity}