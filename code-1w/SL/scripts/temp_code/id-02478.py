import itertools

# Simulated system telemetry data with mixed signal types
def collect_telemetry(batches):
    readings = []
    for batch in batches:
        for val in batch:
            if val % 7 == 0:
                readings.append(val * 1.5)
            elif val > 50:
                readings.append(val - 10)
            else:
                readings.append(val + 3)
    return readings

# Legacy function - unused but looks relevant
def deprecated_normalizer(x):
    return (x >> 1) ^ 0xAA

# Signal filter that masks noise using bitwise logic
def filter_noise(signal_stream):
    mask = 0xFF
    filtered = []
    for i, x in enumerate(signal_stream):
        masked_val = int(x) & mask
        if masked_val % 5 == 0 and i % 2 == 0:
            filtered.append(masked_val)
    return filtered

# Redundant transformation - only used to distract
def transform_legacy(data):
    return [d ** 0.5 for d in data if d > 10]

# Core diagnostic processor
def analyze_phase_shift(readings):
    shifted = []
    for r in readings:
        temp = (r * 2) + 5
        shifted.append(temp)
    return shifted

# Aggregates metrics using dictionary operations and slicing
def extract_signatures(filtered_data):
    sig_dict = {}
    for i, val in enumerate(filtered_data):
        key = f'group_{i // 3}'
        if key not in sig_dict:
            sig_dict[key] = []
        sig_dict[key].append(val)
    
    # Apply slicing to extract mid-patterns
    for k in sig_dict:
        if len(sig_dict[k]) > 2:
            sig_dict[k] = sig_dict[k][1:-1]
    
    # Flatten using itertools
    flat_sigs = list(itertools.chain.from_iterable(sig_dict.values()))
    
    # Decoy reduction (not actually used in final path)
    fake_reduction = sum(flat_sigs) // 2 if flat_sigs else 0
    
    return flat_sigs

# Main metric processor combining multiple concepts
def process_metrics(log_entries, system_flags):
    # Step 1: Collect raw telemetry
    raw_telemetry = collect_telemetry(log_entries)
    
    # Step 2: Apply noise filtering (critical path)
    clean_signal = filter_noise(raw_telemetry)
    
    # Step 3: Phase shift analysis (relevant)
    phase_data = analyze_phase_shift(clean_signal)
    
    # Step 4: Extract structural signatures (used)
    signatures = extract_signatures(phase_data)
    
    # Irrelevant computations below (distractors)
    anomaly_score = 0
    for s in signatures:
        if s & 0x1:
            anomaly_score += 1
    anomaly_score *= 17
    
    # Fake control flow with dead branch
    debug_mode = False
    extra_offset = 0
    if debug_mode:  # Never taken
        extra_offset = sum(transform_legacy(phase_data))
    
    # Simulated flag interactions (misleading intermediate)
    flag_weights = {k: v * 0.1 for k, v in system_flags.items()}
    weighted_total = sum(flag_weights.values()) * 100
    
    # Critical final computation
    base_result = sum(signatures) // len(signatures) if signatures else 0
    adjustment = system_flags.get('overclock', 0) - system_flags.get('throttle', 0)
    final_diagnostic = base_result + adjustment * 5
    
    # Unused but plausible-looking output
    diagnostic_log = {
        'raw_count': len(raw_telemetry),
        'filtered_peak': max(clean_signal) if clean_signal else 0,
        'phase_avg': sum(phase_data) // len(phase_data) if phase_data else 0,
        'anomaly_score': anomaly_score,
        'computed_result': final_diagnostic
    }
    
    return final_diagnostic

# Input data setup
log_input = [
    [14, 8, 63, 41],
    [70, 55, 3, 28],
    [84, 105, 9, 77]
]

system_diagnostics = {
    'overclock': 6,
    'throttle': 2,
    'legacy_mode': 1,
    'debug_trace': 5
}

# Execution point of interest
final_diagnostic = process_metrics(log_input, system_diagnostics)
print(f"Result: {final_diagnostic}")