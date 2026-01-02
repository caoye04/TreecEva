def preprocess_chunk(chunk, config):
    magnitude = sum(abs(x) for x in chunk)
    norm_factor = config.get('norm', 1.0)
    return [x / norm_factor if norm_factor else x for x in chunk]


def detect_spikes(signal, limit):
    spikes = []
    for i, val in enumerate(signal):
        if abs(val) > limit:
            spikes.append(i)
    return spikes if spikes else [0]  # dummy fallback


def encode_features(indices, signal):
    encoded = 0
    for idx in indices:
        encoded ^= int(signal[idx] * 100) & 0xFF
    return encoded or 42  # avoid zero


def validate_integrity(raw, processed):
    checksum_raw = sum(raw) % 1000
    checksum_proc = sum(p * 2 for p in processed[:len(raw)]) % 1000
    return checksum_raw == checksum_proc

# Irrelevant helper (distractor)
def smooth_signal(data, factor=0.9):
    if not data:
        return []
    result = [data[0]]
    for x in data[1:]:
        result.append(result[-1] * factor + x * (1 - factor))
    return result

# Unused function (dead code path)
def compress_data(sequence):
    if not sequence:
        return ''
    counts = []
    current, count = sequence[0], 1
    for val in sequence[1:]:
        if val == current:
            count += 1
        else:
            counts.append(f'{current}:{count}')
            current, count = val, 1
    counts.append(f'{current}:{count}')
    return ';'.join(counts)


def analyze_signal(data, thresholds):
    # Step 1: Extract configuration
    primary_threshold = thresholds['primary']
    secondary_threshold = thresholds['secondary']
    mode_flag = thresholds['mode']

    # Step 2: Initial filtering
    filtered = [x for x in data if abs(x) >= primary_threshold]

    # Step 3: Conditional processing branch (only used if mode_flag)
    if mode_flag and len(filtered) > 5:
        adjusted = [x * 0.85 for x in filtered]
    else:
        adjusted = [x * 1.1 for x in filtered]  # default path taken

    # Step 4: Detect anomalies above secondary threshold
    anomalies = []
    for i, val in enumerate(adjusted):
        if val > secondary_threshold:
            anomalies.append(i)
    
    # Step 5: Compute rolling average of 3 elements (if possible)
    rolling_avg = []
    for i in range(len(adjusted) - 2):
        window = adjusted[i:i+3]
        rolling_avg.append(sum(window) / 3)
    
    # Step 6: Map positions using enumerate and zip (required feature)
    indexed_rolls = list(enumerate(rolling_avg))
    shift_offsets = list(range(len(indexed_rolls)))
    paired = [a + b for a, b in zip([r for i, r in indexed_rolls], shift_offsets)]

    # Step 7: Aggregate diagnostic score
    base_score = len(anomalies) * 100
    adjustment = int(sum(paired[:5]) if paired else 0)
    
    # Step 8: Final computation
    final_diagnostic = base_score + adjustment - len(data)

    # Irrelevant side calculations (distractors)
    temp_analysis = {"peaks": len(anomalies), "smoothness": sum(1 for x in data if x > 0)}
    metadata_log = f"Processed {len(data)} entries with {len(filtered)} survivors"
    debug_trace = [f"Step{i}: {x:.2f}" for i, x in enumerate(adjusted[:3])]

    return final_diagnostic

# Main execution
if __name__ == "__main__":
    # Simulated sensor input
    raw_signal = [-1.2, 0.5, 3.8, -2.1, 4.5, 6.3, -0.8, 1.1, 2.9, 5.0, 3.2, -1.5]
    
    # Processing configuration
    config_settings = {"norm": 1.0, "filter_low": 0.1}
    threshold_map = {
        'primary': 2.0,
        'secondary': 4.0,
        'mode': False
    }
    
    # Preprocess
    processed_data = preprocess_chunk(raw_signal, config_settings)
    
    # Validate (not affecting output directly)
    is_valid = validate_integrity(raw_signal, processed_data)
    
    # Detect spikes (used only for encoding)
    spike_indices = detect_spikes(processed_data, 5.0)
    feature_code = encode_features(spike_indices, processed_data)
    
    # Actual target computation
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")