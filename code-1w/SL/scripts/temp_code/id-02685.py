import itertools

def analyze_phase_coherence(samples):
    # Irrelevant signal processing function (dead code path)
    filtered = [x for x in samples if abs(x) > 0.1]
    spectrum = [abs(sample)**2 for sample in filtered]
    return sum(spectrum) / len(spectrum) if spectrum else 0.0

def validate_handshake(protocol_layers):
    # Misleading validation logic with decoy purpose
    checksum = 0
    for layer in protocol_layers:
        for byte in layer:
            checksum ^= byte
    return checksum == 0x5A

def evaluate_latency_burst(latency_data):
    # Unused performance analysis
    bursts = []
    current_burst = []
    threshold = sum(latency_data) / len(latency_data) * 1.5
    
    for t in latency_data:
        if t > threshold:
            current_burst.append(t)
        elif current_burst:
            bursts.append(current_burst)
            current_burst = []
    if current_burst:
        bursts.append(current_burst)
    
    return len(bursts), sum(len(b) for b in bursts)

def extract_signal_envelope(waveform, rate=44100):
    # Distractor: advanced math not used in final result
    import math
    envelope = []
    window_size = int(rate * 0.01)  # 10ms windows
    for i in range(0, len(waveform), window_size):
        chunk = waveform[i:i+window_size]
        rms = math.sqrt(sum(x*x for x in chunk) / len(chunk)) if chunk else 0
        envelope.append(rms)
    return envelope

def aggregate_metrics(log_entries, flags):
    # Core relevant logic buried among distractions
    status_map = {0: 'idle', 1: 'active', 2: 'standby', 3: 'error'}
    critical_events = 0
    timing_sum = 0.0
    
    # Real data processing
    for entry in log_entries:
        phase_id = entry['phase']
        duration = entry['duration_sec']
        timing_sum += duration
        
        if flags['debug_mode'] and phase_id == 3:
            critical_events += 1
        
        # Nested conditional red herring
        if flags['legacy_compat']:
            temp_adj = entry.get('temp', 25) - 20
            if temp_adj > 5:
                pass  # Dead logic

    # Complex counting using enumerate and zip
    indices = list(range(len(log_entries)))
    paired = list(zip(indices, [e['duration_sec'] for e in log_entries]))
    weighted_index_sum = sum(i * dur for i, dur in paired)

    # Bit manipulation distractor
    flag_state = 0
    for f in flags.values():
        if isinstance(f, bool) and f:
            flag_state |= 1
        flag_state = (flag_state << 1) & 0xF

    # Actual answer computation hidden here
    base_score = timing_sum * 100
    adjustment = critical_events * 50
    raw_metric = base_score - adjustment  # This determines final_diagnostic

    # Decoy transformation
    transformed = [math.sin(x['duration_sec']) for x in log_entries] if log_entries else []
    entropy = 0.0
    for t in transformed:
        if t != 0:
            entropy -= t * math.log(abs(t))

    return int(raw_metric)  # Final result extraction

# Simulated input data
system_flags = {
    'debug_mode': True,
    'safe_mode': False,
    'legacy_compat': True,
    'verbose_logging': True,
    'enable_tracing': False
}

timing_log = [
    {'phase': 0, 'duration_sec': 0.12, 'temp': 22},
    {'phase': 1, 'duration_sec': 0.34, 'temp': 27},
    {'phase': 2, 'duration_sec': 0.21, 'temp': 30},
    {'phase': 3, 'duration_sec': 0.58, 'temp': 35},
    {'phase': 3, 'duration_sec': 0.19, 'temp': 33}
]

# Unused signal data (distractor)
signal_samples = [0.15, -0.03, 0.42, 0.08, -0.21, 0.67, 0.11]
protocol_stack = [
    [0x10, 0x2F, 0x55],
    [0x3C, 0x4A, 0x01],
    [0x5A, 0x5A, 0x5A]
]

# Real execution begins here
baseline_coherence = analyze_phase_coherence(signal_samples)
handshake_valid = validate_handshake(protocol_stack)
latency_bursts, total_spike_count = evaluate_latency_burst([x['duration_sec'] for x in timing_log])
envelope = extract_signal_envelope(signal_samples)

# Key computation - target of the question
final_diagnostic = aggregate_metrics(timing_log, system_flags)

print(f"Result: {final_diagnostic}")