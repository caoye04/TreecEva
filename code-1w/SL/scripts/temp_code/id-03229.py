import math

# Simulated sensor fusion module for aerospace telemetry

def analyze_phase_stability(readings, threshold=0.05):
    variance = sum([(x - sum(readings)/len(readings))**2 for x in readings]) / len(readings)
    return variance < threshold

def compute_harmonic_balance(phases):
    if not phases:
        return 0.0
    total = sum([math.cos(p) + math.sin(p) for p in phases])
    return total / len(phases)

def detect_anomaly_sequence(events):
    # Irrelevant dead function - red herring
    count = 0
    for e in events:
        if e == 'ERR':
            count += 1
            if count > 2:
                return True
    return False

def extract_timing_envelope(signal_stream):
    # Unused complex transformation - distractor
    envelope = []
    for i, s in enumerate(signal_stream):
        if i % 3 == 0:
            envelope.append(s * math.tan(i + 1e-5))
    return [abs(e) for e in envelope if e != 0]

def flag_transient_spikes(powers, window=5):
    spikes = []
    for i in range(len(powers) - window + 1):
        window_avg = sum(powers[i:i+window]) / window
        if powers[i] > 2 * window_avg and powers[i] > 0.1:
            spikes.append(i)
    return len(spikes) > 0

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def bitwise_diagnostic(code_seq):
    # Bit manipulation with misleading purpose
    accumulator = 0
    for val in code_seq:
        accumulator ^= int(val * 100) & 0xFF
    return accumulator | 0x5F

def validate_phase_coherence(timestamps, signals):
    paired = [(t, s) for t, s in zip(timestamps, signals) if s > 0.2]
    if len(paired) < 2:
        return False
    diffs = [paired[i+1][0] - paired[i][0] for i in range(len(paired)-1)]
    return all(d < 0.05 for d in diffs)

def aggregate_metrics(log, flags):
    base_score = 0
    timing_data = [entry['delta'] for entry in log if entry['type'] == 'SYNC']
    
    # Real computation path
    if len(timing_data) > 3:
        avg_delta = sum(timing_data) / len(timing_data)
        base_score += int(1000 * avg_delta)
    
    phase_readings = [entry['phase'] for entry in log if 'phase' in entry]
    if analyze_phase_stability(phase_readings):
        base_score += 250
    
    if flag_transient_spikes([entry.get('power', 0) for entry in log]):
        base_score -= 100
    
    entropy_value = calculate_entropy([int(10*x['signal']) for x in log if 'signal' in x])
    base_score += int(entropy_value * 20)
    
    # Distractor: irrelevant bit operation on unrelated data
    codes = [1.76, 2.11, 1.89, 2.05, 1.94]
    decoy_result = bitwise_diagnostic(codes)
    decoy_result += 50  # More distraction
    
    # Meaningless nested structure
    temp_flags = {}
    for k, v in flags.items():
        if isinstance(v, bool):
            temp_flags[k] = not v  # Flip but unused
    
    # Key logic using dictionary operations
    critical_keys = ['calib_done', 'sync_acquired', 'voltage_stable']
    if all(flags.get(k, False) for k in critical_keys):
        base_score += 500
    
    # List comprehension with filtering (actual use)
    valid_phases = [p for p in phase_readings if 0.1 < p < 0.9]
    if len(valid_phases) > 4:
        harmonic = compute_harmonic_balance(valid_phases)
        base_score += int(harmonic * 150)
    
    final_diagnostic = base_score
    return final_diagnostic

# Simulated telemetry input
timing_log = [
    {'type': 'SYNC', 'delta': 0.023, 'phase': 0.15, 'signal': 0.88, 'power': 0.05},
    {'type': 'DATA', 'delta': 0.019, 'phase': 0.17, 'signal': 0.91},
    {'type': 'SYNC', 'delta': 0.021, 'phase': 0.16, 'signal': 0.85, 'power': 0.04},
    {'type': 'SYNC', 'delta': 0.022, 'phase': 0.18, 'signal': 0.89, 'power': 0.03},
    {'type': 'SYNC', 'delta': 0.020, 'phase': 0.15, 'signal': 0.87, 'power': 0.06},
    {'type': 'HEARTBEAT', 'timestamp': 1245},
    {'type': 'SYNC', 'delta': 0.023, 'phase': 0.17, 'signal': 0.90, 'power': 0.07},
    {'type': 'SYNC', 'delta': 0.021, 'phase': 0.16, 'signal': 0.86, 'power': 0.02}
]

system_flags = {
    'calib_done': True,
    'sync_acquired': True,
    'voltage_stable': True,
    'overheat_alert': False,
    'redundancy_active': True,
    'manual_override': False
}

# Dead variable assignments - red herrings
baseline_reference = extract_timing_envelope([0.1, 0.3, 0.2, 0.4, 0.35])
event_sequence = ['OK', 'OK', 'WARN', 'OK']
anomaly_detected = detect_anomaly_sequence(event_sequence)

# Main execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Target result: {final_diagnostic}")