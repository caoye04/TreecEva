import math

def generate_wave_sequence(length, frequency, phase=0):
    """Generate a sinusoidal wave sequence (real-world signal simulation)."""
    return [math.sin(2 * math.pi * frequency * t / length + phase) for t in range(length)]

def extract_peaks(signal):
    """Extract indices where signal crosses positive threshold."""
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > 0.5 and signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def calculate_symmetry_score(peaks):
    """Calculate symmetry score of peak distribution (unused distractor)."""
    if len(peaks) < 2:
        return 0.0
    diffs = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    mean_diff = sum(diffs) / len(diffs)
    variance = sum((d - mean_diff) ** 2 for d in diffs) / len(diffs)
    return round(variance, 4)

def slice_and_normalize(segment):
    """Normalize a slice of signal to [-1, 1]."""
    max_val = max(abs(x) for x in segment) if segment else 1
    return [x / max_val for x in segment] if max_val != 0 else segment

def calculate_interference(pat1, pat2):
    """Compute net phase shift from interference of two patterns."""
    # Use only first 8 elements for alignment analysis
    window_a = pat1[:8]
    window_b = pat2[:8]

    # Compute element-wise product (interference pattern)
    interference = [a * b for a, b in zip(window_a, window_b)]

    # Calculate cumulative phase-like offset
    total_offset = 0.0
    for i, val in enumerate(interference):
        if val < 0:
            total_offset -= 0.25  # quarter-cycle shift per negative interference
        elif val > 0:
            total_offset += 0.125  # eighth-cycle reinforcement

    # Apply artificial damping factor (not affecting final answer directly)
    damping_factor = len([x for x in interference if abs(x) > 0.3])
    effective_shift = total_offset / (damping_factor if damping_factor else 1)

    # Final transformation: convert to discrete phase state
    quantized_shift = int(round(effective_shift * 8))  # eighths of cycle
    return quantized_shift

# Main simulation setup
sequence_length = 16
base_freq_a = 2
base_freq_b = 3

# Generate two wave patterns with different frequencies
pattern_a = generate_wave_sequence(sequence_length, base_freq_a, phase=math.pi/4)
pattern_b = generate_wave_sequence(sequence_length, base_freq_b, phase=math.pi/2)

# Extract structural features (distractor - not used in final calculation)
peaks_a = extract_peaks(pattern_a)
symmetry_a = calculate_symmetry_score(peaks_a)

peaks_b = extract_peaks(pattern_b)
symmetry_b = calculate_symmetry_score(peaks_b)

# Normalize central segments (semi-relevant but not used in core logic)
mid_slice_a = slice_and_normalize(pattern_a[4:12])
mid_slice_b = slice_and_normalize(pattern_b[4:12])

# Core computation: interference-based phase analysis
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Irrelevant secondary processing (dead-end path)
combined_peaks = sorted(set(peaks_a + peaks_b))
peak_gaps = [combined_peaks[i+1] - combined_peaks[i] for i in range(len(combined_peaks)-1)] if combined_peaks else []

# Output result
Result: {net_phase_shift}