def process_signal_chain(raw_samples, threshold=0.75):
    filtered = [x for x in raw_samples if abs(x) > threshold]
    normalized = [round(x * 1.414213, 4) for x in filtered]
    return normalized

# Irrelevant signal processing stub (distractor)
def enhance_resolution(data):
    return [x * 2 for x in data if x > 1]  # Unused path

# Misleading fault simulation (dead code)
def simulate_failure_modes(mode_ids):
    severity_map = {}
    for m in mode_ids:
        if m % 3 == 0:
            severity_map[m] = 'CRITICAL'
        elif m % 2 == 0:
            severity_map[m] = 'WARNING'
    return severity_map  # Never called

# Core diagnostic logic
def evaluate_phase_shift(samples):
    total_shift = 0
    for i in range(len(samples)):
        if i % 3 == 0 and samples[i] > 0:
            total_shift += int(samples[i]) % 7
        elif i % 4 == 0:
            total_shift -= (samples[i] ** 2) // 10
    return total_shift

# Data transformation with list comprehension and filtering
def generate_diagnostic_codes(events):
    codes = []
    for e in events:
        if e < 0:
            codes.append(f"ERR_{abs(e)}")
        else:
            codes.append(f"OK_{e}")
    return [c for c in codes if '_1' not in c]  # Extra filter step (partially relevant)

# Main analysis function
def analyze_fault_sequence(log_entry):
    phase_result = evaluate_phase_shift(log_entry['readings'])
    
    # Distractor: unused intermediate calculation
    baseline_offset = sum([x // 2 for x in log_entry['readings'] if x > 5])
    temporal_weight = len([t for t in log_entry['timestamps'] if t % 2 == 1])
    
    # Red herring: complex but irrelevant mapping
    status_lookup = {i: chr(65 + (i * 3) % 26) for i in range(15)}
    for k in list(status_lookup.keys()):
        if k % 4 == 0:
            status_lookup[k] = 'X'  # Obfuscation

    # Critical path: compute checksum from event codes
    event_codes = generate_diagnostic_codes(log_entry['events'])
    error_count = len([ec for ec in event_codes if ec.startswith('ERR')])
    
    # Final computation combining multiple concepts
    checksum = (phase_result * 3) - (error_count * 12) + (temporal_weight * 2)
    
    # Dead code block (misleading)
    if checksum < 0:
        adjustment = 0
        for _ in range(abs(checksum)):
            adjustment += 1  # Simulates compensation (never used)
    
    # Final result
    final_diagnostic = abs(checksum) + 100
    return final_diagnostic

# Simulated input data
sensor_readings = [8.2, -3.1, 6.7, 9.0, -1.5, 4.3, 7.8]
timestamps = [101, 102, 103, 104, 105, 106, 107]
events = [2, -3, 1, -1, 4]

# Processed data (only some used)
processed = process_signal_chain(sensor_readings)

# Input structure (real data)
diagnostic_log = {
    'readings': [int(x) for x in sensor_readings],  # Converted to integers
    'timestamps': timestamps,
    'events': events,
    'metadata': {'version': '2.1', 'node': 'A7'}  # Unused
}

# Execution point
final_diagnostic = analyze_fault_sequence(diagnostic_log)
print(f"Result: {final_diagnostic}")