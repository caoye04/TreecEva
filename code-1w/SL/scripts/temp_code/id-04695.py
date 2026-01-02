import math

# Simulated sensor data processing with embedded diagnostics
def collect_sensor_data():
    raw_signals = [i * 0.5 + math.sin(i / 3) for i in range(20)]
    noise_floor = sum([abs(x) for x in raw_signals]) / len(raw_signals)
    filtered = [x for x in raw_signals if abs(x) > 0.8]
    baseline_shift = math.cos(len(filtered))
    return filtered, noise_floor, baseline_shift

# Irrelevant auxiliary function (distractor)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 3)

# Signal preprocessing with red herring operations
def preprocess_signal(signal_list):
    temp_log = []
    adjusted = []
    magnitude_peak = max([abs(x) for x in signal_list], default=0)
    
    for idx, val in enumerate(signal_list):
        if idx % 3 == 0:
            transformed = val ** 2 if val >= 0 else -1 * (val ** 2)
        else:
            transformed = val * 1.1
        
        # Decoy transformation
        decoy_val = transformed + math.tan(idx + 0.1) if idx % 4 == 2 else transformed
        adjusted.append(transformed)  # Only 'transformed' is used
        temp_log.append(f'Step {idx}: {decoy_val:.3f}')
    
    # Dead code path (never executed due to constant condition)
    debug_mode = False
    if debug_mode and len(adjusted) > 10:
        print('Debug: High volume adjustment')
        adjusted = [x * 2 for x in adjusted]
    
    # Real processing branch
    normalized = [x / magnitude_peak if magnitude_peak != 0 else 0 for x in adjusted]
    return normalized

# Frame segmentation with dummy counters
def segment_frames(clean_signal):
    frames = []
    frame_size = 4
    dummy_counter = 0
    
    for i in range(0, len(clean_signal), frame_size):
        chunk = clean_signal[i:i + frame_size]
        if len(chunk) == frame_size:
            # Bit manipulation red herring
            checksum = 0
            for x in chunk:
                truncated = int(abs(x * 100))
                checksum ^= (truncated << 1) | (truncated >> 7)  # Bit fiddling
            frames.append({'data': chunk, 'chk': checksum})
        else:
            dummy_counter += 1  # Unused counter
    
    # Dummy structure with no downstream use
    stats_summary = {
        'frame_count': len(frames),
        'dummy_total': dummy_counter,
        'placeholder_flag': True
    }
    
    return frames

# Core analysis logic buried in distractions
def analyze_signal(frame_packets):
    diagnostic_score = 0.0
    fluctuation_index = 0
    threshold_reference = 0.75
    
    for packet in frame_packets:
        data = packet['data']
        
        # Logical operation chain with conditional expression
        peak = max(data, key=abs)
        polarity_switch = sum(
            1 for a, b in zip(data, data[1:]) if (a < 0) != (b < 0)
        )
        
        # Conditional expression (python idiom)
        severity = 1.5 if abs(peak) > threshold_reference else 0.8
        stability = 'stable' if polarity_switch <= 1 else 'unstable'
        
        # Accumulate real score
        diagnostic_score += severity * (2 if stability == 'stable' else 0.5)
        
        # Distractor: Set-based anomaly detection (unused)
        unique_signs = set(1 if x >= 0 else -1 for x in data)
        anomaly_flag = len(unique_signs) > 1 and polarity_switch > 2
        if anomaly_flag:
            diagnostic_score -= 0.1  # Never triggered in this case
        
        fluctuation_index += polarity_switch
    
    # Final computation using correct path
    adjustment_factor = 1 + (fluctuation_index / 100)
    final_diagnostic = int(diagnostic_score * adjustment_factor * 100)  # Key assignment
    
    # Dead code: unused alternative result
    if fluctuation_index == 0:
        alt_result = diagnostic_score * 2
    else:
        alt_result = None
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    signals, floor, shift = collect_sensor_data()
    processed = preprocess_signal(signals)
    segmented = segment_frames(processed)
    final_diagnostic = analyze_signal(segmented)
    print(f'Result: {final_diagnostic}')