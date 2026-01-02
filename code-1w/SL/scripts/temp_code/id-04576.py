from collections import defaultdict, Counter

# Simulated health monitoring system with signal processing and noise filtering
def analyze_readings(readings):
    filtered = [x for x in readings if 50 < x < 200]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    
    # Irrelevant statistical distractions
    variance = sum((x - baseline) ** 2 for x in filtered) / len(filtered) if filtered else 0
    peak_noise_ratio = max(filtered) / (min(filtered) + 1) if filtered else 0
    
    # Distractor: unused transformation
    normalized = [round((x - baseline) / (variance ** 0.5 + 1), 3) for x in filtered]
    
    return baseline

# Signal decoder with bit manipulation red herrings
def decode_signal(patterns):
    accumulated = 0
    for p in patterns:
        # Bit manipulation that looks important but is irrelevant
        shifted = (p << 3) & 0xFF
        toggled = shifted ^ 0b10101010
        accumulated += toggled % 17
    # This function ultimately returns a constant for decoy purposes
    return 42  # red herring value

# Core data processor with conditional logic and slicing
def extract_segments(data_stream):
    segment_key = data_stream[10:15]  # critical slice
    offset = sum(segment_key) % 7
    
    # Multiple distractor slices
    decoy_a = data_stream[::3]
    decoy_b = data_stream[-5::-2]
    decoy_c = data_stream[7:20:2]
    
    # Real computation hidden among distractions
    if offset > 3:
        return segment_key[1] * 2
    else:
        return segment_key[2] * 3

# Main metric processor combining multiple concepts
def process_metrics(data, config):
    # Dictionary-based threshold routing
    action_map = defaultdict(lambda: 'monitor')
    action_map.update({
        'critical': 'isolate',
        'elevated': 'warn',
        'normal': 'continue'
    })
    
    # Count occurrences (used later)
    status_counts = Counter([entry['status'] for entry in data])
    
    # Slicing distraction on structured data
    recent_entries = data[-8:]
    sample_slice = [e['value'] for e in recent_entries[::2]]
    
    # Real logic path
    base_score = 0
    for entry in data:
        val = entry['value']
        stat = entry['status']
        if stat == 'critical' and val > config['critical_floor']:
            base_score += val // 10
        elif stat == 'elevated':
            base_score += val % 9
    
    # Decoy branching with misleading intermediate
    diagnostic_code = 0
    if status_counts['critical'] > 2:
        diagnostic_code = 999
    elif len(sample_slice) > 5:
        diagnostic_code = 888  # looks important
    else:
        diagnostic_code = 777
    
    # Final computation uses extract_segments in non-obvious way
    signal_probe = [len(str(entry['value'])) for entry in data]
    segment_value = extract_segments(signal_probe)
    
    # Actual answer derivation
    final_diagnostic = base_score * segment_value - status_counts['normal']
    
    # Dead code path - never reached due to above logic
    if diagnostic_code == 42:
        finalize_system_state()
    
    return final_diagnostic

# Unused helper to increase interference
def finalize_system_state():
    raise RuntimeError("This should not be called")

# Global configuration with plausible decoys
thresholds = {
    'critical_floor': 85,
    'warning_ceil': 150,
    'sample_rate': 0.25,
    'timeout': 300
}

# Input data constructed to trigger specific logic paths
health_data = [
    {'value': 92, 'status': 'critical'},
    {'value': 45, 'status': 'normal'},
    {'value': 87, 'status': 'critical'},
    {'value': 76, 'status': 'elevated'},
    {'value': 95, 'status': 'critical'},
    {'value': 34, 'status': 'normal'},
    {'value': 89, 'status': 'critical'},
    {'value': 68, 'status': 'elevated'},
    {'value': 40, 'status': 'normal'},
    {'value': 105, 'status': 'critical'},
    {'value': 72, 'status': 'elevated'}
]

# Execution chain with hidden dependencies
baseline_metric = analyze_readings([entry['value'] for entry in health_data])
signal_patterns = [len(entry['status']) for entry in health_data]
decoded = decode_signal(signal_patterns)  # calls red herring function

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")