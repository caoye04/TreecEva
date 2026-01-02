import math

# Simulate dual-wave interference with phase modulation and noise filtering
def generate_wave_pattern(base_freq, duration, sample_rate=1000):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    raw_wave = [math.sin(2 * math.pi * base_freq * t) for t in timesteps]
    return raw_wave


def apply_harmonic_distortion(signal, harmonics=3):
    # Irrelevant transformation - not used in final computation
    distorted = signal[:]
    for h in range(2, harmonics + 1):
        distorted = [distorted[i] + 0.3 * math.sin(h * i * 0.1) for i in range(len(distorted))]
    return distorted


def extract_spectral_peaks(signal_chunk):
    # Dead-end analysis function - never called in main flow
    magnitude = sum(abs(x) for x in signal_chunk)
    norm = magnitude / len(signal_chunk)
    peaks = [i for i, x in enumerate(signal_chunk) if abs(x) > 1.5 * norm]
    return len(peaks), norm


def calculate_interference(pat1, pat2):
    # Core logic: cross-correlation with phase unwrapping
    min_len = min(len(pat1), len(pat2))
    truncated_a = pat1[:min_len]
    truncated_b = pat2[:min_len]

    # Compute element-wise phase difference
    phase_diffs = []
    for i in range(min_len):
        if truncated_a[i] == 0:
            angle = math.pi / 2 if truncated_b[i] > 0 else -math.pi / 2
        elif truncated_b[i] == 0:
            angle = 0
        else:
            ratio = truncated_b[i] / truncated_a[i]
            angle = math.atan(ratio) if abs(ratio) <= 100 else math.copysign(math.pi/2, ratio)
        phase_diffs.append(angle)
    
    # Accumulate net phase shift with smoothing
    smoothed_phase = [phase_diffs[0]]
    for i in range(1, len(phase_diffs)):
        delta = phase_diffs[i] - phase_diffs[i-1]
        if delta > math.pi:
            delta -= 2 * math.pi
        elif delta < -math.pi:
            delta += 2 * math.pi
        smoothed_phase.append(smoothed_phase[-1] + delta)
    
    net_phase = sum(smoothed_phase) / len(smoothed_phase)

    # Red herring: unused high-order moment calculation
    fourth_moment = sum((x - net_phase)**4 for x in smoothed_phase) / len(smoothed_phase)
    kurtosis = fourth_moment / (sum((x - net_phase)**2 for x in smoothed_phase) / len(smoothed_phase))**2

    return net_phase

# Generate control noise profile (irrelevant to final result)
noise_floor = [0.01 * math.cos(i * 0.05) for i in range(1000)]
denoised_reference = [x if abs(x) > 0.005 else 0 for x in noise_floor]

# Primary signal generation
pattern_a = generate_wave_pattern(5.0, 0.5)   # 5Hz wave over 0.5s
pattern_b = generate_wave_pattern(7.5, 0.5)  # 7.5Hz reference

# Apply irrelevant processing to create distraction
enhanced_a = apply_harmonic_distortion(pattern_a)
enhanced_b = apply_harmonic_distortion(pattern_b)

# Slice operations on irrelevant segments
segment_offset = 150
analysis_window = 300
fragment_a = enhanced_a[segment_offset:segment_offset + analysis_window]
fragment_b = enhanced_b[segment_offset:segment_offset + analysis_window]

# Additional decoy: set-based outlier detection (unused)
signal_values = set(round(x, 3) for x in pattern_a)
outlier_threshold = 0.95
outliers = {x for x in signal_values if abs(x) > outlier_threshold}

# Critical statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print final answer
print(f"Result: {net_phase_shift}")