def analyze_sensor_data(data_sequence):
    checksum = 0
    for i, val in enumerate(data_sequence):
        if i % 3 == 0:
            checksum += val * 2
        elif i % 5 == 0:
            checksum -= val
    return checksum

sensor_readings = [7, 12, 5, 18, 21, 9, 14, 6, 11, 25]
raw_checksum = analyze_sensor_data(sensor_readings)

baseline_offset = 3.14159
phase_shift = raw_checksum % 8

# Irrelevant transformation chain (distractor)
transient_buffer = []
for x in sensor_readings:
    transient_buffer.append(x ** 0.5 + baseline_offset)

def compute_inertial_factor(seq):
    total = 0
    for j, item in enumerate(seq):
        if j < len(seq) // 2:
            total += item * (j + 1)
    return total // 2

inertial_rating = compute_inertial_factor(sensor_readings)
redundant_metric = inertial_rating * phase_shift - 7

# Real computation begins here — deeply nested and obscured
config_flags = [True, False, True]
efficiency_log = []

for idx, reading in enumerate(sensor_readings):
    temp_log = []
    for shift in range(3):
        shifted_val = (reading >> shift) & 1
        temp_log.append(shifted_val)
    
    bit_sum = sum(temp_log)
    if idx % 2 == 0:
        efficiency_log.append(bit_sum * 1.5)
    else:
        efficiency_log.append(bit_sum * 0.8)

# Decoy function — looks important but unused
def calculate_entropy(vector):
    import math
    entropy = 0.0
    norm = [v / sum(vector) for v in vector if v > 0]
    for p in norm:
        if p > 0:
            entropy -= p * math.log(p)
    return entropy

entropy_proxy = 0.0
for e in efficiency_log:
    if e > 2.0:
        entropy_proxy += e * 0.1

# Core logic hidden among distractions
base_rating = 0
for i, log_val in enumerate(efficiency_log):
    if i in [1, 3, 5, 7]:
        base_rating += int(log_val)
    elif i == 4:
        base_rating *= 2

# Another red herring: complex but unused structure
status_map = {i: ('active' if v % 2 == 0 else 'pending') for i, v in enumerate(transient_buffer)}

# Critical statement buried in conditional noise
if len(efficiency_log) > 5:
    adjustment_factor = 0
    for pos, (a, b) in enumerate(zip(efficiency_log, efficiency_log[1:])):
        if a > b:
            adjustment_factor += 1
        elif a < b:
            adjustment_factor -= 1
    
    def adjust_thermal_rating(rating, log_data):
        modifier = 1.0
        for index, entry in enumerate(log_data):
            if index % 4 == 0 and entry > 2.0:
                modifier *= 1.2
            elif index == len(log_data) - 1:
                modifier += entry / 10
        return int(rating * modifier)
    
    thermal_capacity = adjust_thermal_rating(base_rating, efficiency_log)
else:
    thermal_capacity = -999

# Dead code path — never executed, adds confusion
if False:
    backup_system = [x for x in sensor_readings if x > 10]
    thermal_capacity = sum(backup_system) // 3

# Final print statement required
print(f"Result: {thermal_capacity}")