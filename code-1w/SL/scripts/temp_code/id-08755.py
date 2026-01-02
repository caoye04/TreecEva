from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def collect_signals(timestamps):
    raw_signals = {}
    for t in timestamps:
        if t % 7 == 0:
            raw_signals[t] = (t * 3) % 19
        elif t % 5 == 0:
            raw_signals[t] = (t + 11) % 17
        else:
            raw_signals[t] = (t * 2) % 13
    return raw_signals

def filter_anomalies(signal_dict, threshold=4):
    anomalies = []
    for k, v in signal_dict.items():
        if v > threshold and k % 2 == 1:
            anomalies.append((k, v))
    # Irrelevant transformation
    reversed_pairs = [(v, k) for k, v in anomalies]
    sorted_reversed = sorted(reversed_pairs)
    return dict(anomalies)

def generate_checksum(data_dict):
    # Red herring function - never actually used in critical path
    checksum = 0
    for i, (k, v) in enumerate(data_dict.items()):
        checksum += (k % 5) * (v % 4) - i
    return abs(checksum) % 1000

def decode_segments(raw_data):
    segments = defaultdict(int)
    temp_buffer = []
    for key, val in raw_data.items():
        if val % 2 == 0:
            segments['even_keys'] += 1
        if key > 50:
            segments['late'] += val
        if key < 20 and val < 10:
            segments['early_low'] += 1
        temp_buffer.append(val * 2 - key)  # unused later
    
    # Dead logic branch - condition never met due to input constraints
    if len(temp_buffer) > 1000:
        backup = sum(temp_buffer) // len(temp_buffer)
        segments['fallback_avg'] = backup
    
    return dict(segments)

def compute_phase_shift(elements):
    total = 0
    shift = 3
    for e in elements:
        if e % 4 == 0:
            total += e >> shift  # Right bit shift by 3
        elif e % 3 == 0:
            total -= e << 1      # Left bit shift by 1
        else:
            total ^= e & 7       # Bitwise AND then XOR
    return total

def analyze_patterns(seq):
    freq = Counter(seq)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    mode_val = min(modes) if modes else 0
    
    # Distractor slicing - creates misleading intermediate
    window = seq[5:15:2]  # Non-critical slice
    window_sum = sum(window) if window else 0
    
    # Actual relevant logic
    cumulative = 0
    for i, x in enumerate(seq):
        if i % 4 == 0:
            cumulative += x * 2
        elif i % 3 == 0:
            cumulative -= x // 2
    return cumulative + mode_val

def process_metrics(entries, flags):
    # Core logic embedded within distractions
    base_values = [e['value'] for e in entries if e['active']]
    inactive_count = len([e for e in entries if not e['active']])  # red herring
    
    # Meaningful transformations
    phase_result = compute_phase_shift(base_values)
    pattern_result = analyze_patterns(base_values)
    
    # Decoy aggregation
    decoy_agg = defaultdict(list)
    for e in entries:
        decoy_agg[e['source']].append(e['value'])
    
    # Critical conditional logic with nested dependencies
    adjustment = 0
    if flags['overclock'] and not flags['safe_mode']:
        adjustment += 17
    if flags['debug_trace']:
        adjustment -= 5
    if flags['legacy_io'] or flags['overclock']:
        adjustment += 3
    
    # Key computation - depends on multiple prior results
    intermediate = (phase_result * 2) + pattern_result + adjustment
    
    # Final mapping based on modular arithmetic
    final_map = {
        i % 11: i for i in range(intermediate - 5, intermediate + 6)
    }
    mapped_value = final_map.get(7, intermediate)
    
    # Irrelevant secondary structure
    metadata_log = {"version": "2.1", "batch": 42, "size": len(entries)}
    
    # ACTUAL ANSWER COMPUTATION
    diagnostic_score = mapped_value + len(flags) - (inactive_count % 7)
    
    # FINAL TARGET VARIABLE
    final_diagnostic = diagnostic_score  # <-- This is the target variable
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # Simulated log entries (realistic domain: system telemetry)
    log_entries = [
        {'value': 12, 'active': True, 'source': 'sensor_A'},
        {'value': 15, 'active': False, 'source': 'sensor_B'},
        {'value': 8, 'active': True, 'source': 'sensor_A'},
        {'value': 9, 'active': True, 'source': 'sensor_C'},
        {'value': 16, 'active': True, 'source': 'sensor_B'},
        {'value': 6, 'active': True, 'source': 'sensor_A'},
        {'value': 21, 'active': False, 'source': 'sensor_D'},
        {'value': 14, 'active': True, 'source': 'sensor_C'}
    ]

    system_flags = {
        'overclock': True,
        'safe_mode': False,
        'debug_trace': True,
        'legacy_io': False,
        'enable_cache': True,
        'validate_input': False
    }

    # Collect signals (used to create distractor data)
    timestamps = list(range(10, 101, 10))
    signal_data = collect_signals(timestamps)
    filtered_signals = filter_anomalies(signal_data)
    segment_stats = decode_segments(signal_data)

    # Unused but plausible-looking aggregations
    total_energy = sum(v for v in signal_data.values() if v % 2 == 1)
    peak_magnitude = max(signal_data.values()) if signal_data else 0

    # MAIN CALL THAT PRODUCES THE ANSWER
    final_diagnostic = process_metrics(log_entries, system_flags)