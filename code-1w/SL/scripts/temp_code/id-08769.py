def analyze_system_performance(data_stream):
    checksum = 0
    temp_buffer = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            checksum += val * 2
        elif i % 5 == 0:
            checksum -= val
        temp_buffer.append(val ^ (i + 1))

    return checksum


def transform_sequence(seq):
    reversed_seq = seq[::-1]
    shifted = [x << 1 for x in reversed_seq if x % 2 == 1]
    padding = [0] * (8 - len(shifted)) if len(shifted) < 8 else []
    return shifted + padding


def evaluate_stability(reading):
    if reading < 100:
        return 'LOW'
    elif reading < 250:
        return 'MEDIUM'
    else:
        return 'HIGH'

# Irrelevant helper that is never called
def deprecated_calibrator(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused constant array
CALIBRATION_MATRIX = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# Simulated sensor data (irrelevant to final result but looks important)
sensor_nodes = ['A1', 'B2', 'C3', 'D4']
node_readings = {
    'A1': [12, 15, 10],
    'B2': [8, 20, 13],
    'C3': [18, 17, 14],
    'D4': [9, 11, 19]
}

# Dead code path with misleading computation
aggregated_load = 0
for readings in node_readings.values():
    for r in readings:
        if r > 10:
            aggregated_load += r * 0.85

# Core logic disguised among distractions
baseline_values = [3, 6, 9, 12, 15]
efficiency_flags = [True if x % 3 == 0 else False for x in range(10)]

# Real input for main calculation
pulse_sequence = [4, 8, 15, 16, 23, 42]

# Distractor: complex-looking but unused transformation
encoded_pulse = []
for idx, val in enumerate(pulse_sequence):
    if val % 2 == 0:
        encoded_pulse.append(val | (idx << 2))
    else:
        encoded_pulse.append(val & (idx + 3))

# Key intermediate step
shifted_cycle = [x >> 1 for x in pulse_sequence if x > 10]

# Simulated log generation with side appearance of relevance
status_codes = {0: 'OK', 1: 'WARN', 2: 'ERR'}
log_entries = []
for cycle in shifted_cycle:
    code = cycle % 3
    log_entries.append(f"[{cycle}] Status={status_codes.get(code, 'UNKNOWN')}")

# Real processing begins here
def generate_efficiency_map(seq):
    return {i: (seq[i] * (i + 1)) for i in range(len(seq))}

def integrate_feedback(loop_log):
    total = 0
    for entry in loop_log:
        try:
            num_part = int(entry.split(']')[0][1:])
            total += num_part // 2
        except:
            continue
    return total

# Efficiency log is actually just a transformed baseline
efficiency_log = [x * 3 for x in baseline_values if x % 2 == 1]

# Critical function that uses efficiency_log
summed_diagnostic = sum([i * v for i, v in enumerate(efficiency_log)])

# Another decoy function
def compute_shadow_index(data):
    index = 0
    for d in data:
        index ^= (d * 5) % 19
    return index

# This function appears complex but only simple arithmetic matters
def calculate_thermal_rating(metrics):
    base_score = 0
    for i, m in enumerate(metrics):
        if i % 2 == 0:
            base_score += m * (i + 2)
        else:
            base_score -= m // (i + 1)
    
    # Red herring: irrelevant conditional
    if base_score > 100:
        adjustment = 0
        for j in range(5):
            adjustment += (base_score >> j) & 1
        base_score -= adjustment
    
    # Actual key computation
    final_factor = len(metrics) ** 2
    return base_score + final_factor

# Misleading post-processing
normalized_output = None
if summed_diagnostic > 0:
    normalized_output = round(summed_diagnostic / 7.0, 3)

# Unused list comprehension with zip and enumerate
audit_trail = [
    f"Node {n}: Cycle {c}" 
    for n, c in zip(
        [sensor_nodes[i] for i in range(len(sensor_nodes))], 
        [str(integrate_feedback(log_entries))]*4
    )
]

# The actual critical statement
thermal_capacity = calculate_thermal_rating(efficiency_log)

print(f"Result: {thermal_capacity}")