import math

# Simulated sensor data processing system
def collect_samples(duration_ms, sample_rate):
    samples = []
    for i in range(int(duration_ms * sample_rate / 1000)):
        samples.append((i * 0.1) % 2.5)
    return samples

# Irrelevant helper: converts numeric level to status string (unused path)
def level_to_status(level):
    if level < 0.5:
        return "CRITICAL"
    elif level < 1.0:
        return "WARNING"
    else:
        return "NORMAL"

# Signal conditioning: applies gain and offset correction
def apply_calibration(raw_signal, gain=1.2, offset=-0.3):
    calibrated = []
    for val in raw_signal:
        corrected = val * gain + offset
        calibrated.append(round(corrected, 6))
    return calibrated

# Frequency domain approximation via simple spectral binning
def estimate_dominant_frequency(signal_chunk):
    total = 0.0
    for i in range(1, len(signal_chunk)):
        total += abs(signal_chunk[i] - signal_chunk[i-1])
    return round(total * 100 / len(signal_chunk), 3)

# Data segmentation into analysis windows
def segment_signal(calibrated_data, window_size=8):
    segments = []
    for i in range(0, len(calibrated_data) - window_size + 1, window_size):
        segments.append(calibrated_data[i:i+window_size])
    # Truncate last incomplete segment
    return segments

# Character frequency analysis in hex representation (distractor)
def count_hex_digits(segments):
    hex_string = ''.join([format(int(abs(s[0]*100)), 'x') for s in segments if s])
    counts = {}
    for c in hex_string:
        counts[c] = counts.get(c, 0) + 1
    return counts  # Dead end: never used

# Threshold mapping based on dynamic baseline (core logic component)
def generate_threshold_map(segmented, base_freq):
    map_dict = {}
    for idx, seg in enumerate(segmented):
        key = f"S{idx}"
        variation = sum(abs(x) for x in seg) / len(seg)
        map_dict[key] = {
            'dynamic': variation * base_freq / (idx + 1),
            'static': 0.85,
            'gain_comp': math.cos(idx * 0.1)
        }
    return map_dict

# Core diagnostic analyzer combining multiple metrics
def analyze_signal(buffer, thresholds):
    if not buffer or not thresholds:
        return -1
    
    # Extract key statistical features from signal buffer
    all_vals = [val for segment in buffer for val in segment]
    mean_val = sum(all_vals) / len(all_vals)
    variance = sum((x - mean_val) ** 2 for x in all_vals) / len(all_vals)
    peak = max(abs(x) for x in all_vals)
    
    # Compute entropy-like measure using value distribution
    rounded_vals = [round(x, 1) for x in all_vals]
    freq_map = {}
    for v in rounded_vals:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / len(rounded_vals)
        entropy -= p * math.log(p) if p > 0 else 0
    
    # Apply complex threshold logic across segments
    score = 0
    for seg_idx, segment in enumerate(buffer):
        seg_key = f"S{seg_idx}"
        if seg_key in thresholds:
            t = thresholds[seg_key]
            seg_mean = sum(segment) / len(segment)
            if seg_mean > t['dynamic'] and abs(t['gain_comp']) > 0.5:
                score += int(abs(seg_mean) * 100)
            elif seg_mean < -t['static']:
                score -= 50
    
    # Final computation with slicing-based correction factor
    history_window = all_vals[-7:] if len(all_vals) >= 7 else all_vals
    correction_factor = sum(history_window[::2]) - sum(history_window[1::2])  # Slicing operation
    final_score = score * (1 + correction_factor) + (entropy * 100)
    
    return int(round(final_score))

# --- Main Execution ---
raw_input_signal = collect_samples(250, 32)  # 250ms at 32Hz
processed_signal = apply_calibration(raw_input_signal)

# Generate time segments for analysis
pattern_buffer = segment_signal(processed_signal, window_size=8)

# Independent frequency estimation for calibration (used in threshold)
dominant_freq = estimate_dominant_frequency(processed_signal)

# Build adaptive threshold structure
threshold_map = generate_threshold_map(pattern_buffer, dominant_freq)

# Perform deep character analysis on metadata (red herring)
hex_counts = count_hex_digits(pattern_buffer)  # Computed but irrelevant

# Introduce decoy variables with plausible names
data_integrity = True
validation_cycle = 0
while validation_cycle < 3:
    data_integrity = not data_integrity
    validation_cycle += 1

# Primary diagnostic assessment
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Output target result
print(f"Target result: {final_diagnostic}")