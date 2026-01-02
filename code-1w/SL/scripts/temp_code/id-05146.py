import math

def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    energy = sum([x**2 for x in filtered])
    normalized = [x / (energy + 1e-9) for x in filtered]
    return energy, normalized

def compute_entropy(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    probabilities = [freq / len(data) for freq in freq_map.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def validate_checksum(sequence):
    # Irrelevant checksum validation (dead-end logic)
    chk = 0
    for val in sequence:
        chk ^= int(val * 100) & 0xFF
    return chk == 0x5A

def process_telemetry(stream_data):
    raw_timestamps = [entry[0] for entry in stream_data]
    signals = [entry[1] for entry in stream_data]
    
    # Distractor: complex but unused signal transformation
    transformed = []
    for i, sig in enumerate(signals):
        phase = (i % 4) * 0.5 * math.pi
        modulated = sig * math.sin(phase) + math.cos(sig)
        transformed.append(round(modulated, 4))
    
    # Real processing path begins
    timing_log = []
    for ts in raw_timestamps:
        sec = int(ts % 60)
        nsec = int((ts * 1e9) % 1e9)
        timing_log.append((sec, nsec))
    
    # Misleading intermediate diagnostic flags
    diag_flags = {}
    for idx, (s, ns) in enumerate(timing_log):
        flag_key = f"F{idx}"
        if s % 7 == 0:
            diag_flags[flag_key] = "ERR_SYNC"
        elif ns % 1000 == 0:
            diag_flags[flag_key] = "WARN_CLOCK"
        else:
            diag_flags[flag_key] = "OK"
    
    # Key computation: extract intervals and analyze periodicity
    intervals = []
    for i in range(1, len(raw_timestamps)):
        delta = raw_timestamps[i] - raw_timestamps[i-1]
        if delta > 0:
            intervals.append(delta)
    
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    stability_score = compute_entropy([round(iv * 10) for iv in intervals])
    
    # Simulate hardware register readouts (irrelevant)
    registers = {f"R{i}": (hash(f"reg{i}") % 256) for i in range(8)}
    calibration_offset = sum(registers.values()) % 17
    
    # Unused function call with side effects avoided
    _ = analyze_signal(signals, threshold=0.5)
    
    # Critical diagnostic logic buried in noise
    diagnostics = {
        'stability': stability_score,
        'count': len(signals),
        'interval_avg': avg_interval,
        'flags_present': sum(1 for f in diag_flags.values() if f != "OK")
    }
    
    # Final aggregation — this is where answer is determined
    final_diagnostic = aggregate_metrics(timing_log, diagnostics)
    
    # Dead code path — never executed
    if calibration_offset < 0:
        fallback = 0
        for k, v in registers.items():
            fallback += hash(k) ^ v
        final_diagnostic -= fallback
    
    return final_diagnostic

def aggregate_metrics(timing_log, diagnostics):
    base = len(timing_log)
    penalty = 0
    
    # Analyze timestamp patterns using zip and enumerate
    for i, (sec, nsec) in enumerate(timing_log):
        if i > 0 and sec % 2 == 0:
            penalty += nsec % 100
    
    # Use of zip to pair adjacent entries
    paired_gaps = [
        curr_sec - prev_sec 
        for (prev_sec, _), (curr_sec, _) in zip(timing_log[:-1], timing_log[1:])
        if curr_sec > prev_sec
    ]
    
    avg_gap = sum(paired_gaps) / len(paired_gaps) if paired_gaps else 1
n    
    # String-based control flow (red herring)
    status_str = "HEALTHY SYSTEM OPERATIONAL"
    if "ERROR" in status_str:
        base *= 2
    
    # Real contribution: combination of count, stability, and gap
    result = int(
        base 
        + diagnostics['stability'] * 100 
        + diagnostics['interval_avg'] * 10 
        - diagnostics['flags_present'] * 5
        - penalty // 1000
    )
    
    return result

def main():
    # Simulated telemetry stream: (timestamp, signal_value)
    telemetry_data = [
        (163784.123, 0.15), (163784.223, 0.82), (163784.323, 0.91),
        (163784.423, 0.03), (163784.523, 0.77), (163784.623, 0.88),
        (163784.723, 0.12), (163784.823, 0.95), (163784.923, 0.64),
        (163785.023, 0.21), (163785.123, 0.89), (163785.223, 0.93)
    ]
    
    # Irrelevant preprocessing
    sorted_data = sorted(telemetry_data, key=lambda x: x[1], reverse=True)
    top_signals = [entry for entry in sorted_data[:5]]
    
    # Trigger main logic
    result = process_telemetry(telemetry_data)
    
    # Output target variable
    print(f"Target result: {result}")

# Execute
main()
