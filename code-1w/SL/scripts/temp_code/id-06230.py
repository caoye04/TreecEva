import itertools

# Simulated sensor data preprocessing with red herrings
def collect_sensor_readings():
    raw_samples = [18, 22, 15, 47, 33, 28, 35]
    offset = 3
    calibrated = [(x - offset) * 0.9 for x in raw_samples]
    return calibrated

# Irrelevant transformation: spectral mirroring (dead logic path)
def mirror_spectrum(data):
    reversed_part = data[::-1]
    return [a + b for a, b in zip(data, reversed_part)]

# Legitimate preprocessing step: segmentation and noise filtering
def segment_and_filter(signal):
    threshold = 20.0
    segments = []
    current_seg = []
    for val in signal:
        if val > threshold:
            current_seg.append(val)
        else:
            if len(current_seg) > 0:
                segments.append(current_seg)
                current_seg = []
    if len(current_seg) > 0:
        segments.append(current_seg)
    
    # Distractor: unused compression attempt
    compressed = [sum(seg) / len(seg) for seg in segments if len(seg) > 1]
    
    # Actual output used later
    filtered = [seg for seg in segments if len(seg) >= 2]
    return filtered

# Misleading auxiliary function: entropy calculation (never called in execution path)
def calculate_entropy(data_list):
    import math
    freq_map = {}
    total = 0
    for item in itertools.chain(*data_list):
        freq_map[item] = freq_map.get(item, 0) + 1
        total += 1
    entropy = -sum((count / total) * math.log2(count / total) for count in freq_map.values())
    return entropy

# Decoy state tracker with fake progression
system_state = {
    'status': 'active',
    'mode': 'diagnostic',
    'checksum': 0,
    'version': '2.1.9'
}

def update_state(new_mode):
    global system_state
    temp_checksum = 0
    for c in new_mode:
        temp_checksum ^= ord(c)
    system_state['mode'] = new_mode
    system_state['checksum'] = temp_checksum
    return temp_checksum

# Unused recursive validator (distractor)
def validate_sequence(seq, index=0):
    if index >= len(seq) - 1:
        return True
    if seq[index] >= seq[index + 1]:
        return False
    return validate_sequence(seq, index + 1)

# Core analysis logic — actually used
measure_log = []
def log_measurement(value, tag='STD'):
    entry = f'{tag}:{value:.3f}'
    measure_log.append(entry)
    return len(entry)

# Main processing chain
signal_data = collect_sensor_readings()

# Dead assignment with misleading name
aggregated_profile = [x for x in signal_data if x > 18.0]

# This call looks important but feeds into unused path
update_state('analysis_enhanced')

# Real pipeline begins here
processed_segments = segment_and_filter(signal_data)

# Fake pattern matching using itertools (no effect on result)
fake_combinations = list(itertools.combinations_with_replacement([1, 2], 3))

# Another distractor: bit-twiddling on unrelated constant
debug_flag = 0b101010
mask = (debug_flag << 3) & 0xFF
inverted = (~mask) & 0xFF

# Logging irrelevant intermediate
log_measurement(sum(itertools.chain(*processed_segments)), 'BASE')

# Key computation block
summary_metrics = []
for i, seg in enumerate(processed_segments):
    avg = sum(seg) / len(seg)
    peak = max(seg)
    weight_factor = (i + 1) * 0.5
    # Only this component contributes to final answer
    diagnostic_score = (avg * 0.7) + (peak * 0.3)
    summary_metrics.append(diagnostic_score)

# Final aggregation with one legitimate path
final_diagnostic = 0
for score in summary_metrics:
    final_diagnostic += score * 100  # Scale up for precision

# Red herring: string-based checksum that isn't used
identifier_str = 'DIAG-' + ''.join(str(int(s))[-1] for s in summary_metrics)

# This print is required — must output Result: <value>
final_diagnostic = int(final_diagnostic)  # Ensure integer
print(f'Result: {final_diagnostic}')