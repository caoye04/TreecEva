import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 64, 192, 32, 180, 95]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant helper - distractor
def format_timestamps(count):
    stamps = []
    for i in range(count):
        sec = i % 60
        minu = (i // 60) % 60
        stamps.append(f'{minu:02d}:{sec:02d}')
    return [s.upper() for s in stamps if '3' not in s]  # unused result

# Noise filtering with red herring logic
def apply_filter(data):
    filtered = []
    noise_floor = 45.0
    spike_threshold = 150.0
    temp_log = []  # dead variable

    for val in data:
        if val < noise_floor:
            continue
        elif val > spike_threshold:
            corrected = val * 0.85
            temp_log.append(f'High spike corrected: {corrected}')
            filtered.append(corrected)
        else:
            filtered.append(val)
    
    # Decoy transformation
    decoy_avg = sum([math.log(x + 1) for x in filtered if x > 100]) / len(filtered) if filtered else 0
    return filtered

# Signal envelope detection - relevant
def detect_envelope(signal):
    if not signal:
        return 0.0
    peak = max(signal)
    avg = sum(signal) / len(signal)
    envelope_score = (peak * 0.6) + (avg * 0.4)
    return round(envelope_score, 3)

# Checksum verification - irrelevant path
def validate_checksum(data_str):
    checksum = 0
    for ch in data_str:
        if ch.isalpha():
            checksum += ord(ch.lower()) - ord('a') + 1
    return checksum % 17 == 0

# Data smoothing using moving average - relevant
def smooth_signal(signal):
    if len(signal) < 3:
        return signal[:]
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        window_avg = (signal[i-1] + signal[i] + signal[i+1]) / 3
        smoothed.append(round(window_avg, 3))
    smoothed.append(signal[-1])
    return smoothed

# Complex analysis with multiple stages and distractions
def analyze_signal(data_list):
    # Dead code block - misleading
    if any(x < 0 for x in data_list):
        raise ValueError("Negative values not allowed")  # never triggered

    # Real processing begins
    baseline_ref = 80.5
    adjustment_steps = 0
    total_offset = 0.0

    for idx, val in enumerate(data_list):
        if val > baseline_ref:
            offset = (val - baseline_ref) * 0.1
            total_offset += offset
            adjustment_steps += 1

    # Distractor: string-based metadata (unused)
    metadata_tag = "SIGMON-2024-X9"
    tag_parts = metadata_tag.split('-')
    version_code = tag_parts[1] if len(tag_parts) > 1 else "0"
    is_active = metadata_tag.endswith('X9') and 'M' in metadata_tag

    # Real calculation path
    envelope = detect_envelope(data_list)
    smoothed = smooth_signal(data_list)
    stability_index = abs(smoothed[-1] - smoothed[0]) if len(smoothed) > 1 else 0

    # Final diagnostic computation
    adjustment_ratio = total_offset / adjustment_steps if adjustment_steps > 0 else 0
    final_diagnostic = (envelope * 1.2) - (stability_index * 0.8) + (adjustment_ratio * 2.0)
    
    # Red herring print (not part of output)
    debug_info = f'Diagnostic trace: {final_diagnostic:.4f}'
    log_entry = debug_info.replace('trace', 'snapshot').upper()

    return round(final_diagnostic, 6)

# Main execution flow
if __name__ == '__main__':
    # Collect and process sensor data
    raw_data = collect_readings()
    processed_data = apply_filter(raw_data)
    
    # Irrelevant formatting call
    _ = format_timestamps(len(raw_data) * 2)
    
    # Validate dummy tag (no effect)
    _ = validate_checksum('DiagnosticSignalX9')
    
    # Core analysis
    final_diagnostic = analyze_signal(processed_data)
    
    # Output the required result
    print(f'Result: {final_diagnostic}')