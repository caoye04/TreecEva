import itertools

# System telemetry constants
technical_baseline = 42.5
signal_attenuation = 0.87
threshold_envelope = 987
sync_grace_period = 12

# Irrelevant telemetry (distractor variables)
unused_buffer = [0] * 100
placeholder_metric = sum(range(10))
legacy_flag = False
dummy_counter = 0
for i in range(50):
    dummy_counter += i % 3

# Core signal sequence generation
quantum_sequence = []
for n in range(1, 8):
    value = (n ** 3) - (2 * n ** 2) + (7 * n)
    if value % 2 == 0:
        quantum_sequence.append(int(value * signal_attenuation))
    else:
        quantum_sequence.append(int(value + technical_baseline))

# System event log with mixed real and decoy entries
system_log = {
    'events': [
        {'type': 'SYNC', 'id': 1, 'timestamp': 100},
        {'type': 'DATA', 'id': 2, 'timestamp': 115},
        {'type': 'ERROR', 'id': 999, 'timestamp': 118},  # red herring
        {'type': 'SYNC', 'id': 3, 'timestamp': 130}
    ],
    'status': 'nominal',
    'checksum': 0xDEADBEEF,  # irrelevant
    'version': '2.1.9-alpha'  # distractor
}

# Auxiliary function - looks important but partially unused
def compute_entropy(data_list):
    entropy = 0.0
    for x in data_list:
        if x > 0:
            entropy -= (x / sum(data_list)) * (x / sum(data_list))
    return round(entropy, 6)

# Decoy analysis function (never called)
def deprecated_analysis(seq):
    accumulator = 0
    for i, val in enumerate(seq):
        accumulator += val % (i + 1) if i != 0 else val % 7
    return accumulator * 2

# Real processing function
def analyze_sync_intervals(log):
    timestamps = [e['timestamp'] for e in log['events'] if e['type'] == 'SYNC']
    intervals = [t2 - t1 for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
    return sum(intervals) if intervals else 0

# Critical diagnostic function
def analyze_system_state(sequence, log):
    # Step 1: Filter sequence using threshold
    filtered = [x for x in sequence if x < threshold_envelope]
    
    # Step 2: Transform via cumulative pattern
    cumulative = []
    total = 0
    for val in filtered:
        total += val
        cumulative.append(total)
    
    # Step 3: Extract alternating indices
    extracted = [cumulative[i] for i in range(0, len(cumulative), 2)]
    
    # Step 4: Apply set deduplication logic (some duplicates introduced)
    temp_set = set(extracted)
    unique_extracted = sorted(list(temp_set), reverse=True)
    
    # Step 5: Cross-reference with sync intervals
    interval_score = analyze_sync_intervals(log)
    
    # Step 6: Use itertools to create rolling window sum
    window_sums = []
    for window in itertools.zip_longest(unique_extracted, unique_extracted[1:], fillvalue=0):
        window_sums.append(sum(window))
    
    # Step 7: Final transformation chain
    aggregate = sum(window_sums) + interval_score
    scaling_factor = len(extracted) + (log['events'][0]['id'] if log['status'] == 'nominal' else 0)
    intermediate_result = aggregate // scaling_factor if scaling_factor != 0 else 0
    
    # Step 8: Final adjustment based on legacy rule (simulated)
    final_adjustment = 5 if len(sequence) > 5 else 0
    final_diagnostic = intermediate_result + final_adjustment
    
    # Dead code path - never reached (misleading)
    if 'ERROR' in [e['type'] for e in log['events']]:
        final_diagnostic = -999  # decoy result
    
    return final_diagnostic

# Execute main logic
interval_diagnostic = analyze_sync_intervals(system_log)
system_snapshot = {k: v for k, v in system_log.items() if k != 'checksum'}  # distractor

# Key execution point
final_diagnostic = analyze_system_state(quantum_sequence, system_log)

# Output result
print(f"Target result: {final_diagnostic}")