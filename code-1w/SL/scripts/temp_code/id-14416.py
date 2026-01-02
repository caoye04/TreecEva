import itertools

# Simulated sensor array diagnostics with noise filtering and mode analysis
def analyze_sensor_modes(raw_readings):
    base_modes = {}
    for idx, val in enumerate(raw_readings):
        mode_key = f'mode_{idx % 7}'
        if mode_key not in base_modes:
            base_modes[mode_key] = 0
        base_modes[mode_key] ^= val & 0xF

    # Irrelevant transformation: frequency shadow mapping (dead logic)
    shadow_map = {k: ((v << 2) | (v >> 2)) & 0xF for k, v in base_modes.items()}
    unused_normalization = [sum(shadow_map.values()) / len(shadow_map)] * 3

    return base_modes


def extract_primary_signatures(raw_readings):
    # Slice-based window extraction
    window_size = 4
    sliding_windows = [raw_readings[i:i+window_size] for i in range(0, len(raw_readings)-window_size+1, 2)]
    
    # Compute XOR fingerprints of windows
    fingerprints = []
    for window in sliding_windows:
        xor_fingerprint = 0
        for w_val in window:
            xor_fingerprint ^= (w_val * 3) & 0xFF
        fingerprints.append(xor_fingerprint)
    
    # Dead path: statistical dispersion (not used later)
    if fingerprints:
        mean_fp = sum(fingerprints) / len(fingerprints)
        variance = sum((x - mean_fp) ** 2 for x in fingerprints) / len(fingerprints)
        dispersion_flag = variance > 5000

    return fingerprints

# Main processing pipeline
def filter_noise(readings, level=3):
    # Apply bit-masking noise reduction
    cleaned = [(r >> level) << level for r in readings]
    return [c for c in cleaned if c != 0]


def build_threshold_map(modes):
    # Create adaptive thresholds based on mode characteristics
    t_map = {}
    for k, v in modes.items():
        t_map[k] = (v * 17) % 97
    
    # Decoy structure: latency simulation map (unused)
    latency_sim = {f'{key}_L': (val * 11) % 101 for key, val in t_map.items()}
    
    return t_map


def process_readings(data, thresholds):
    # Core diagnostic calculation
    accumulator = 0
    
    # Real usage of dictionary and slicing
    keys = list(thresholds.keys())
    key_slice = keys[1:-1]  # Middle keys only
    
    for item in data:
        for k in key_slice:
            # Nonlinear interaction
            temp = (item ^ thresholds[k]) * (item & 0x1F)
            accumulator += temp % 89
    
    # Misleading intermediate: peak normalization (not affecting result)
    if accumulator > 1000:
        normalized_peak = accumulator / max(data)
        scaling_hint = int(normalized_peak) & 0xFFFF
    
    # Final transformation using itertools.cycle to simulate phase alignment
    phase_cycle = itertools.cycle([3, 1, 4, 1, 5])
    final_shift = 0
    for _ in range(len(data) % 7):
        final_shift += next(phase_cycle)
    
    # Actual answer computation
    raw_final = accumulator + (final_shift * 13)
    
    # Diagnostic checksum (red herring - looks important but unused)
    checksum = sum(raw_final.to_bytes(4, 'little')) ^ 0xAA
    
    return raw_final

# Execution sequence
if __name__ == '__main__':
    sensor_log = [
        243, 176, 92, 201, 134, 88, 195, 110, 209, 172,
        94, 217, 131, 85, 199, 107, 225, 168, 97, 212
    ]
    
    # Step 1: Analyze operational modes (used)
    operational_modes = analyze_sensor_modes(sensor_log)
    
    # Step 2: Extract signature patterns (partially used heuristic)
    signatures = extract_primary_signatures(sensor_log)
    
    # Step 3: Filter out electronic noise (critical)
    filtered_data = filter_noise(sensor_log, level=3)
    
    # Step 4: Build dynamic threshold map (used)
    threshold_map = build_threshold_map(operational_modes)
    
    # Step 5: Process final diagnostic (ANSWER GENERATED HERE)
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")