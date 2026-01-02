def analyze_signal_strength(signal):
    if len(signal) < 5:
        return 0
    threshold = sum(signal) / len(signal)
    count = 0
    for val in signal:
        if val > threshold:
            count += 1
    return count

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for f in freq.values():
        prob = f / total
        entropy -= prob * log(prob)
    return entropy

# Unused diagnostic mode flag (red herring)
diagnostic_mode_active = True
legacy_buffer = [0] * 1024
compression_level = 3

# Core data structures
baseline_readings = (85, 92, 78, 96, 88)
sensor_offsets = {1: -3, 2: 5, 3: -2, 4: 4, 5: 1}

temp_log = ['ERR_404', 'OK', 'WARN_01', 'OK', 'OK']
status_filter = set(temp_log)

# Misleading intermediate calculation (dead path)
effective_bandwidth = 0
for i in range(3):
    for j in range(3):
        effective_bandwidth += (i + j) ** 2

# Actual relevant data
calibration_sequence = [x + 2 for x in baseline_readings]
fault_flags = [analyze_signal_strength(calibration_sequence) > 3]
fault_flags.append(len(baseline_readings) in sensor_offsets)
fault_flags.append('WARN_01' in status_filter)

# Bit manipulation red herring (irrelevant)
data_word = 0b110101
mask = 0b101110
scrambled = (data_word ^ mask) << 2

# Conditional expression with distractor
adjustment_factor = 1.5 if compression_level > 2 else 0.8
impact_score = adjustment_factor * len(legacy_buffer)  # Misleading large number

# Unused recursive function (decoy)
def resolve_conflict(depth):
    if depth <= 0:
        return 1
    return depth * resolve_conflict(depth - 2)

# Real processing logic
config_state = (True, False, True)
override_sequence = [not x for x in config_state]

# Key function combining boolean logic, sets, and conditional expressions
def process_metrics(seq, flags):
    s = set(seq)
    avg = sum(s) / len(s)
    
    # Use of string method (required feature)
    code_tag = "CALIBRATE::FINAL".lower().replace("::", "_")
    
    # Set operations (required feature)
    critical_values = {80, 90, 100}
    overlap_count = len(s & critical_values)
    
    # Conditional expression (required feature)
    base_score = avg * 2 if 'ERR' not in code_tag else -1
    
    # Boolean logic chain
    modifier = 1
    if flags[0] and flags[1]:
        modifier += 1
    if not flags[2]:
        modifier -= 1
    elif overlap_count >= 1:
        modifier += 2
    
    # Final computation
    result = int(base_score + (modifier * overlap_count * 10))
    
    # Dead code branch (distractor)
    if diagnostic_mode_active and False:  
        result = impact_score  # Never reached
        
    return result

# Execution point of interest
final_diagnostic = process_metrics(calibration_sequence, fault_flags)
print(f"Target result: {final_diagnostic}")