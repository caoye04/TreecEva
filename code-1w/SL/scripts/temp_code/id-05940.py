import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(12):
        phase = (i * 7) % 16
        amplitude = (i ** 2) % 9 + 3
        signals.append({
            'id': f'SIG{i:02d}',
            'raw_value': (amplitude * math.sin(math.pi * phase / 8)) + i % 4,
            'timestamp': 1623456000 + i * 30,
            'status': 'active' if i % 3 != 2 else 'standby'
        })
    return signals

# Legacy function - not used but looks relevant
def legacy_calibrate(data):
    adjusted = []
    for entry in data:
        adj_val = entry['raw_value'] * 0.95 + 2.1
        adjusted.append({**entry, 'raw_value': adj_val})
    return adjusted

# Diagnostic pattern analyzer
def count_transitions(signal_list):
    transitions = 0
    prev_status = ''
    for item in signal_list:
        if prev_status and prev_status != item['status']:
            transitions += 1
        prev_status = item['status']
    return transitions

# Signal compressor - irrelevant to final result
def compress_signal(signal_list):
    compressed = {}
    for s in signal_list:
        key = s['id'][:-1]
        if key not in compressed:
            compressed[key] = []
        compressed[key].append(s['raw_value'])
    return {k: sum(v)/len(v) for k, v in compressed.items()}

# Flag aggregator with red herring computation
def aggregate_flags(metadata_map):
    flag_summary = {key: False for key in ['F1', 'F2', 'F3', 'F4', 'F5']}
    entropy = 0.0
    for k, v in metadata_map.items():
        if isinstance(v, bool):
            flag_summary[k[-2:]] = v
        # Distracting entropy calculation
        if isinstance(v, int) and v > 0:
            p = v / 100.0
            entropy -= p * math.log(p) if p > 0 else 0
    # Fake checksum
    fake_checksum = sum(1 for x in flag_summary.values() if x) * 17
    return flag_summary

# Main analysis function
def analyze_pattern(entries, flags):
    # Step 1: Extract numeric sequence
    values = [e['raw_value'] for e in entries]
    
    # Step 2: Compute moving average over 3 elements
    moving_avg = []
    for i in range(len(values) - 2):
        avg = (values[i] + values[i+1] + values[i+2]) / 3
        moving_avg.append(round(avg, 2))
    
    # Step 3: Detect upward trends
    trend_count = 0
    for i in range(len(moving_avg) - 1):
        if moving_avg[i] < moving_avg[i+1]:
            trend_count += 1
    
    # Step 4: Apply modular filter based on timestamps
    valid_times = [e['timestamp'] % 100 for e in entries]
    mod_sum = sum(t % 7 for t in valid_times if t % 2 == 1)
    
    # Step 5: Character frequency in IDs (red herring)
    id_chars = ''.join(e['id'] for e in entries)
    char_freq = {}
    for c in id_chars:
        char_freq[c] = char_freq.get(c, 0) + 1
    # Use only digit '1' count meaningfully
    auxiliary = char_freq.get('1', 0) * 5
    
    # Step 6: Status transition count (actually used)
    status_transitions = count_transitions(entries)
    
    # Step 7: Dictionary-based mapping of transitions
    transition_map = {
        0: 100, 1: 205, 2: 198, 3: 212, 4: 187, 5: 201,
        6: 194, 7: 209, 8: 196, 9: 203, 10: 199, 11: 207
    }
    base_score = transition_map.get(status_transitions, 0)
    
    # Step 8: Final composition (only some components are used)
    # Despite many variables, only these contribute:
    # - base_score from transition map
    # - mod_sum from timestamp mod arithmetic
    # - auxiliary from character count
    final_diagnostic = base_score + mod_sum - auxiliary
    
    # Many other computations above are distractions
    return final_diagnostic

# Irrelevant utility function (decoy)
def validate_checksum(data):
    total = sum(d['raw_value'] for d in data)
    return int(total) % 11 == 0

# Main execution flow
if __name__ == '__main__':
    # Generate real data
    log_entries = generate_telemetry()
    
    # Create system flags (some look important)
    system_flags = {
        'F1': True, 'F2': False, 'F3': True,
        'config_priority': 78,
        'timeout_cycles': 4,
        'F4': True, 'F5': False
    }
    
    # Perform aggregation (result unused)
    aggregated = aggregate_flags(system_flags)
    
    # Compress signals (unused)
    compressed_signals = compress_signal(log_entries)
    
    # Analyze pattern - this produces the answer
    final_diagnostic = analyze_pattern(log_entries, system_flags)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")