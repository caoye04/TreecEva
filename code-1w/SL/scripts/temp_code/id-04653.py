import math

# Simulated sensor fusion system for environmental monitoring
def collect_samples(count, noise_factor=0.05):
    """Generate synthetic sensor readings with controlled noise."""
    samples = []
    for i in range(count):
        clean_signal = 20 * math.sin(i * 0.3) + 15 * math.cos(i * 0.7)
        noisy_reading = clean_signal + noise_factor * math.sin(i * 5)
        samples.append(round(noisy_reading, 3))
    return samples

# Irrelevant utility function (red herring)
def calculate_efficiency_score(metrics):
    total = sum(metrics)
    penalty = len([m for m in metrics if m < 0]) * 0.1
    return round((total / len(metrics)) ** 2 - penalty, 4) if metrics else 0

def filter_outliers(data, threshold=2.5):
    """Remove values beyond threshold standard deviations from mean."""
    if not data:
        return []
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered or [mean_val]  # Prevent empty result

def apply_window_correction(signal_chunk):
    """Apply Hanning window to reduce spectral leakage."""
    corrected = []
    n = len(signal_chunk)
    for i in range(n):
        window_weight = 0.5 - 0.5 * math.cos(2 * math.pi * i / max(n-1, 1))
        corrected.append(signal_chunk[i] * window_weight)
    return corrected

def integrate_segments(segments):
    """Combine multiple signal segments using energy-weighted averaging."""
    weights = []
    outputs = []n    for seg in segments:
        energy = sum(x**2 for x in seg)
        weights.append(energy)
        outputs.append(sum(seg) / len(seg) if seg else 0)
    total_weight = sum(weights)
    if total_weight == 0:
        return 0
    return sum(outputs[i] * weights[i] for i in range(len(outputs))) / total_weight

# Unused decoy function (dead code path)
def legacy_compatibility_mode(inputs):
    buffer = [0] * 8
    for x in inputs:
        idx = int(abs(x)) % 8
        buffer[idx] ^= int(x) & 0xF
    return sum(buffer[i] << i for i in range(8))

def preprocess_signal(raw_data):
    """Main preprocessing pipeline with distractions."""
    # Step 1: Initial filtering
    stage_a = filter_outliers(raw_data, threshold=2.0)
    
    # Distraction: Efficiency metric calculation (irrelevant)
    dummy_metrics = [len(raw_data), len(stage_a), sum(1 for x in raw_data if x > 0)]
    efficiency_diagnostic = calculate_efficiency_score(dummy_metrics)  # unused later
    
    # Step 2: Normalize range
    min_val, max_val = min(stage_a), max(stage_a)
    dynamic_range = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / dynamic_range for x in stage_a]
    
    # Step 3: Window correction
    window_applied = apply_window_correction(normalized)
    
    # Red herring: Bit manipulation on float magnitudes (unused)
    bit_trail = 0
    for val in window_applied[:5]:
        int_part = int(abs(val) * 1000)
        bit_trail ^= (int_part & 0xFF) >> 2
    
    # Step 4: Segment and prepare
    mid_point = len(window_applied) // 2
    segment_1 = window_applied[:mid_point]
    segment_2 = window_applied[mid_point:]
    segmented_data = [segment_1, segment_2]
    
    # Final integration
    integrated_value = integrate_segments(segmented_data)
    return round(integrated_value, 5)

def analyze_readings(signals):
    """Final diagnostic analysis with set-based validation."""
    # Transform into categorical bands
    bands = []
    for s in signals:
        if s < -0.5:
            bands.append('critical')
        elif s < 0:
            bands.append('low')
        elif s < 0.5:
            bands.append('normal')
        else:
            bands.append('high')
    
    # Real processing: compute entropy-like score
    unique_classes = set(bands)
    class_counts = {cls: bands.count(cls) for cls in unique_classes}
    total = len(bands)
    shannon_index = -sum((count/total) * math.log(count/total) for count in class_counts.values())
    
    # Set operations as required feature
    expected_set = {'normal', 'high', 'low', 'critical'}
    missing_categories = expected_set - set(bands)
    completeness_bonus = 1.25 if not missing_categories else 0.8
    
    # Secondary distraction: combinatorics calculation (misleading)
    possible_pairs = 0
    if len(signals) >= 2:
        n = len(signals)
        possible_pairs = n * (n - 1) // 2  # C(n,2)
    diversity_proxy = len(unique_classes) / possible_pairs if possible_pairs else 0  # artificial metric
    
    # Final deterministic computation (this is the real answer path)
    base_score = shannon_index * 100
    final_adjustment = completeness_bonus * 0.75
    final_diagnostic = int(round(base_score * final_adjustment))
    
    # Additional red herring: unused recursive function
    def trace_anomaly_path(depth, acc=0):
        if depth <= 0:
            return acc
        return trace_anomaly_path(depth - 1, acc ^ (depth * 3))
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate raw input
    raw_sensor_data = collect_samples(36, noise_factor=0.08)
    
    # Preprocess the signal (key transformation)
    processed_signals = preprocess_signal(raw_sensor_data)
    
    # Final analysis step (target execution point)
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")