import math

# Simulated sensor data processing system for aerospace telemetry
def acquire_signal(raw=False):
    base_readings = [0.1, 0.3, 0.4, 0.8, 1.2, 1.5, 1.6, 1.4, 1.1, 0.7, 0.5]
    noise_floor = [0.01 * math.sin(i) for i in range(len(base_readings))]
    return [b + n for b, n in zip(base_readings, noise_floor)]


def filter_outliers(data, threshold=1.0):
    filtered = []
    for x in data:
        if abs(x) > threshold:
            filtered.append(x)
    return filtered


def integrate_signal(data):
    total = 0.0
    for i in range(1, len(data)):
        total += (data[i] + data[i-1]) * 0.05 / 2  # trapezoidal rule
    return total


def segment_signal(data, window_size=3):
    segments = []
    for i in range(0, len(data) - window_size + 1):
        segments.append(data[i:i+window_size])
    return segments


def compress_data(segments):
    # Irrelevant compression function (dead path)
    compressed = []
    for seg in segments:
        val = 0
        for i, x in enumerate(seg):
            val += int(x * 10) << (i * 3)
        compressed.append(hex(val))
    return compressed


def shift_reference_frame(segments, offset=1):
    # Misleading transformation - not used in final result
    shifted = []
    for seg in segments:
        shifted.append([x - offset for x in seg])
    return shifted


def compute_coherence_metric(segments):
    # Distractor: complex but unused metric
    coherence = 0.0
    for seg in segments:
        mean_val = sum(seg) / len(seg)
        variance = sum((x - mean_val) ** 2 for x in seg) / len(seg)
        if variance > 0:
            coherence += mean_val / math.sqrt(variance)
    return coherence


def extract_peak_features(segments):
    peaks = []
    for seg in segments:
        peaks.append(max(seg) - min(seg))
    return peaks


def normalize_features(features):
    if not features:
        return []
    max_feat = max(features)
    if max_feat == 0:
        return features
    return [f / max_feat for f in features]


def apply_calibration_curve(features):
    calibrated = []
    for f in features:
        # Complex non-linear mapping (some distraction)
        if f < 0.3:
            calibrated.append(f * 1.2)
        elif f < 0.7:
            calibrated.append(f * 0.95)
        else:
            calibrated.append(f * 0.8 + 0.1)
    return calibrated


def analyze_signal(segments):
    # Core logic begins here
    features = extract_peak_features(segments)
    normalized = normalize_features(features)
    calibrated = apply_calibration_curve(normalized)
    
    # Key computation path
    signal_energy = 0.0
    for c in calibrated:
        signal_energy += c ** 2
    
    # Final diagnostic score based on energy and segment count
    adjustment_factor = len(segments) % 7
    raw_diagnostic = int(signal_energy * 1000) + adjustment_factor
    
    # Red herring: unused branching
    if raw_diagnostic > 1000:
        final = raw_diagnostic // 3
    elif raw_diagnostic > 500:
        final = raw_diagnostic // 2
    else:
        final = raw_diagnostic  # This will be the case
    
    # Additional distraction: spurious bit manipulation
    decoy_value = (final ^ 0xAA) & 0xFF
    decoy_value = (decoy_value >> 4) | ((decoy_value & 0xF) << 4)
    
    return final

# Main execution flow
if __name__ == "__main__":
    # Step 1: Acquire raw telemetry signal
    raw_signal = acquire_signal(raw=True)
    
    # Step 2: Filter out high-amplitude outliers (no effect in this case)
    cleaned_signal = filter_outliers(raw_signal, threshold=2.0)
    
    # Step 3: Integrate signal for total energy (distractor - not used later)
    integrated_energy = integrate_signal(raw_signal)
    
    # Step 4: Segment the signal into overlapping windows
    signal_segments = segment_signal(raw_signal, window_size=3)
    
    # Step 5: Compress segments (irrelevant operation)
    compressed_repr = compress_data(signal_segments)
    
    # Step 6: Shift reference frame (misleading transformation)
    shifted_segments = shift_reference_frame(signal_segments, offset=0.5)
    
    # Step 7: Compute coherence (unused metric - red herring)
    coherence_score = compute_coherence_metric(signal_segments)
    
    # Step 8: Process only original segments (correct path)
    processed_segments = signal_segments  # No actual processing needed
    
    # Step 9: Analyze signal using peak-based diagnostics
    final_diagnostic = analyze_signal(processed_segments)
    
    # Output result
    print(f"Result: {final_diagnostic}")