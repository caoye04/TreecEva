import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_samples = [i * 0.1 for i in range(100)]
    noise_floor = 0.05
    return [math.sin(x) + noise_floor * (x % 2) for x in raw_samples]

# Irrelevant helper: computes statistical dispersion (not used in final result)
def compute_dispersion(data):
    mean_val = sum(data) / len(data)
    return math.sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))

# Distraction function: processes metadata only
def process_metadata(raw_data):
    meta = {
        'length': len(raw_data),
        'max_val': max(raw_data),
        'min_val': min(raw_data),
        'checksum': sum(int(x * 100) for x in raw_data[:10])
    }
    # Dead code path
    if meta['length'] > 1000:
        meta['flag'] = True
    else:
        meta['flag'] = False
    return meta

# Preprocess signal with filtering and normalization
def preprocess_signal(signal):
    # Apply high-pass filter simulation
    filtered = [signal[i] - signal[i-1] for i in range(1, len(signal))]
    # Normalize to zero mean
    mean_filtered = sum(filtered) / len(filtered)
    normalized = [x - mean_filtered for x in filtered]
    # Truncate negative values (rectification)
    rectified = [max(0, x) for x in normalized]
    return rectified

# Secondary distraction: spectral estimation (unused)
def estimate_spectrum(signal):
    spectrum = []
    for k in range(10):
        real_part = sum(signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        imag_part = sum(signal[n] * math.sin(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        magnitude = math.sqrt(real_part**2 + imag_part**2)
        spectrum.append(magnitude)
    peak_freq = spectrum.index(max(spectrum))
    return {'peak_frequency': peak_freq, 'spectrum': spectrum}

# Core analysis logic (depends on preprocessing)
def analyze_waveform(chars):
    count_dict = {}
    for c in chars:
        count_dict[c] = count_dict.get(c, 0) + 1
    sorted_chars = sorted(count_dict.keys())
    return ''.join(sorted_chars)

# Main processing chain
def analyze_signal(data):
    # Misleading intermediate steps
    temp_stats = {
        'sum': sum(data),
        'count_above': len([x for x in data if x > 0.1]),
        'ratio': 0
    }
    if temp_stats['sum'] != 0:
        temp_stats['ratio'] = temp_stats['count_above'] / temp_stats['sum']

    # Actual key computation
    threshold = 0.05
    crossings = 0
    for i in range(1, len(data)):
        if data[i-1] < threshold <= data[i]:
            crossings += 1

    # Complex transformation using string operations
    binary_pattern = ''.join(['1' if x > threshold else '0' for x in data[:32]])
    grouped = [binary_pattern[i:i+4] for i in range(0, len(binary_pattern), 4)]
    hex_segments = [hex(int(segment, 2))[2:] for segment in grouped]
    
    # Decoy dictionary manipulation
    decoy_map = {h: i for i, h in enumerate(hex_segments)}
    for k in decoy_map:
        decoy_map[k] = (decoy_map[k] ** 2) + 1

    # Critical calculation
    base_value = crossings * 1000
    adjustment = len([h for h in hex_segments if 'a' in h or 'f' in h]) * 17
    final_score = base_value + adjustment

    # String-based secondary check (actually affects result)
    control_string = "diagnostic_sync_894"
    char_frequency = {c: control_string.count(c) for c in set(control_string)}
    sync_marker = sum(char_frequency[c] for c in "sync")

    # Final result influenced by both signal and string logic
    final_diagnostic = final_score + (sync_marker * 10)

    # Dead assignment - misleading
    final_diagnostic = final_diagnostic if final_diagnostic > 0 else -1

    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    signal_data = acquire_signal()
    metadata = process_metadata(signal_data)  # Unused but looks important
    processed_data = preprocess_signal(signal_data)
    spectral_analysis = estimate_spectrum(processed_data)  # Computed but unused
    waveform_signature = analyze_waveform("abccba")  # Red herring call
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")