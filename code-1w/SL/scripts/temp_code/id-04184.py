import math

# Simulated sensor data processing system for autonomous drone navigation
def collect_sensor_data():
    raw_readings = [i * 0.7 + (i % 3) for i in range(25)]
    timestamps = [t * 100 + 5 for t in range(25)]
    metadata_log = {'version': '2.1.5', 'source': 'drone_7', 'calibrated': True}
    return list(zip(timestamps, raw_readings))


def filter_noise(data, threshold=4.5):
    cleaned = []
    noise_floor = []
    for ts, val in data:
        if abs(val) > threshold:
            cleaned.append((ts, val))
        else:
            noise_floor.append(val)  # Distractor: collected but unused later
    scaling_factor = 1.0 + len(noise_floor) / 100.0  # Distractor: calculated but not impactful
    return cleaned


def extract_peaks(signal_series):
    peaks = []
    for i in range(1, len(signal_series) - 1):
        if signal_series[i] > signal_series[i-1] and signal_series[i] > signal_series[i+1]:
            peaks.append(i)
    return peaks


def generate_frequency_map(peaks):
    freq_map = {}
    for p in peaks:
        bin_index = p % 7
        freq_map[bin_index] = freq_map.get(bin_index, 0) + 1
    # Irrelevant transformation
    normalized = {k: v * 0.95 for k, v in freq_map.items()}
    return freq_map  # Return original, not normalized


def compute_coherence_metric(freq_dict, size_hint):
    total = 0
    for k, v in freq_dict.items():
        total += (k + 1) * v
    dummy_adjustment = math.sin(len(freq_dict)) * 0.1  # Red herring
    adjusted_total = total + dummy_adjustment
    return int(adjusted_total)


def reconstruct_waveform(indices, raw_magnitude):
    waveform = []
    for idx in indices:
        contribution = (raw_magnitude[idx] ** 0.5) * 2.5
        waveform.append(contribution)
    # Dead code path - never used
    if len(waveform) > 10:
        smoothed = [sum(waveform[i:i+3]) / 3 for i in range(len(waveform)-2)]
    return waveform


def slice_critical_band(data, start=5, end=15):
    # Slicing operation (required feature)
    return data[start:end]


def calculate_entropy(values):
    from collections import Counter
    counts = Counter(values)
    entropy = 0.0
    n = len(values)
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)
    return round(entropy, 6)


def temporal_align(frames):
    aligned = []
    shift = len(frames) // 4
    for i in range(len(frames)):
        aligned.append(frames[(i + shift) % len(frames)])
    return aligned


def analyze_signal(frames):
    # Dictionary operation (required feature)
    stats = {
        'count': len(frames),
        'sum': sum(frames),
        'max': max(frames),
        'min': min(frames)
    }
    
    # Complex multi-step logic with decoys
    if stats['count'] > 10:
        pivot = stats['sum'] // stats['count']
        high_freq_components = [f for f in frames if f > pivot]
        low_freq_components = [f for f in frames if f <= pivot]
        
        # Nested conditional red herring
        if len(high_freq_components) > len(low_freq_components):
            adjustment = calculate_entropy(high_freq_components)
        else:
            adjustment = calculate_entropy(low_freq_components) * 0.8
        
        # Core computation disguised among distractions
        base_score = 0
        for i, f in enumerate(frames):
            if i % 3 == 0:
                base_score += int(f) % 7
            elif i % 4 == 0:
                base_score -= int(f) % 5
        
        # Decoy transformation
        temp_result = base_score * adjustment
        secondary_check = sum(1 for x in frames if x > 5) * 17
        
        # Final logic step
        final_score = base_score + secondary_check
        
        # Misleading intermediate
        diagnostic_flag = 'STABLE' if final_score > 100 else 'FLUCTUATING'
        
        # Actual answer carrier
        return final_score * 2  # Critical multiplier
    
    return -1

# Main execution flow
sensor_data = collect_sensor_data()
filtered_data = filter_noise(sensor_data)
only_values = [val for _, val in filtered_data]
peaks_in_signal = extract_peaks(only_values)
frequency_bins = generate_frequency_map(peaks_in_signal)
coherence_index = compute_coherence_metric(frequency_bins, len(only_values))

# Signal reconstruction branch (distractor)
reconstructed = reconstruct_waveform(peaks_in_signal, only_values)
entropy_measure = calculate_entropy(reconstructed)  # Computed but not used directly

# Critical processing chain
segmented = slice_critical_band(only_values, 3, 14)
rotated = temporal_align(segmented)
processed_frames = [x * 1.8 for x in rotated]  # Final input preparation

# Key statement
final_diagnostic = analyze_signal(processed_frames)

print(f"Result: {final_diagnostic}")