def monitor_subsystem_integrity(base_offset, thresholds):
    status_bits = set()
    accumulator = 0
    
    for i in range(3, 10):
        if i % 2 == 0:
            accumulator += i ** 2
            status_bits.add(f'mask_{i}')
        else:
            accumulator -= i
            status_bits.discard('mask_4')  # harmless if not present
    
    calibrated = accumulator + base_offset
    return calibrated, status_bits


def compute_signal_chain(input_val, mode_flag):
    temp_buffer = []
    shift_reg = input_val
    
    for _ in range(5):
        shift_reg = (shift_reg * 3) ^ 0b1010
        temp_buffer.append(shift_reg & 0xFF)
    
    # Irrelevant aggregation
    aggregate_noise = sum(x & 0x0F for x in temp_buffer) * 0.5
    signal_peak = max(temp_buffer)
    
    # Decoy computation with no downstream use
    decoy_metric = (signal_peak << 2) | 0x0A
    normalization_factor = 1.0 if mode_flag else 0.1
    
    return signal_peak * normalization_factor

# Dead function - never called
def legacy_diagnostic_routine():
    history_log = [0] * 10
    for i in range(len(history_log)):
        history_log[i] = (i * i) % 7
    return sum(history_log)

# Simulate sensor drift compensation (distractor)
sensor_drift_compensation = 0.0
for cycle in range(1, 8):
    sensor_drift_compensation += (cycle * 0.1) ** 2

# Real data path begins
baseline, flags = monitor_subsystem_integrity(42, [0.5, 0.75])
raw_input_signal = 17
processed_signal = compute_signal_chain(raw_input_signal, True)

# Simulated diagnostic log with red herring entries
initial_diagnostics = {
    'sensor_a': True,
    'sensor_b': False,
    'calibration_lock': True,
    'voltage_spike': False
}

working_set = set(initial_diagnostics.keys())
detected_anomalies = set()
for key in initial_diagnostics:
    if not initial_diagnostics[key]:
        detected_anomalies.add(key)

# Merged state with irrelevant transformations
merged_state = working_set.symmetric_difference({'calibration_lock', 'timing_fault'})
anomaly_count = len(detected_anomalies)

# Introduce misleading intermediate
phantom_score = (anomaly_count * 1000) + 567  # looks important but unused later

# Core logic disguised among distractors
def analyze_fault_sequence(log, flags):
    severity_weight = 0
    
    # Relevant condition
    if 'sensor_b' in log and not log['sensor_b']:
        severity_weight += 30
    
    # Another relevant factor
    if len(flags) > 0:
        severity_weight += 5
    
    # Critical arithmetic path
    raw_contrib = baseline // 10
    signal_contrib = int(processed_signal)
    
    # Key calculation
    preliminary_index = raw_contrib + signal_contrib + severity_weight
    
    # Red herring: complex but irrelevant bit manipulation
    decoy_mask = 0
    for i in range(3):
        decoy_mask ^= (preliminary_index >> i) & 0b111
    final_adjustment = 2 if decoy_mask > 10 else 1
    
    # Final result built from multiple reasoning steps
    result = preliminary_index * final_adjustment
    
    # THIS IS THE TARGET VARIABLE
    final_diagnostic = result + 11
    
    return final_diagnostic

# Execute main logic
diagnostic_log = initial_diagnostics
system_flags = ['flag_1']
final_diagnostic = analyze_fault_sequence(diagnostic_log, system_flags)

print(f"Target result: {final_diagnostic}")