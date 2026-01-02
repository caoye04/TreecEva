import math

def generate_wave_sequence(length, frequency, phase=0):
    """Generate a sine wave sequence with given parameters."""
    return [math.sin(2 * math.pi * frequency * (i / length) + phase) for i in range(length)]

def calculate_amplitude_envelope(signal):
    """Calculate the moving average envelope of a signal."""
    window_size = 3
    padded_signal = [0] * (window_size // 2) + signal + [0] * (window_size // 2)
    envelope = []
    for i in range(len(signal)):
        segment = padded_signal[i:i + window_size]
        avg = sum(abs(x) for x in segment) / window_size
        envelope.append(avg)
    return envelope

def detect_peaks(signal, threshold=0.5):
    """Simple peak detection above threshold."""
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def calculate_interference(seq1, seq2):
    """Calculate net phase shift from interference of two wave patterns."""
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have same length")
    
    # Element-wise interference
    interference = [a * b for a, b in zip(seq1, seq2)]
    
    # Normalize by RMS to get coherent measure
    rms = math.sqrt(sum(x*x for x in interference) / len(interference))
    normalized_interference = [x / (rms + 1e-9) for x in interference]
    
    # Calculate cumulative phase drift
    cumulative_drift = 0
    for i, val in enumerate(normalized_interference):
        weight = (i + 1) / len(normalized_interference)
        cumulative_drift += val * weight * math.cos(val)
    
    # Secondary validation: check symmetry
    reversed_interference = normalized_interference[::-1]
    symmetry_score = sum(min(a, b) for a, b in zip(normalized_interference, reversed_interference))
    
    # Final phase calculation
    raw_sum = sum(normalized_interference)
    adjustment = math.log(abs(raw_sum) + 1) * 0.1
    net_phase = raw_sum + adjustment
    
    # Unused but plausible distractor variables
    peak_positions = detect_peaks(normalized_interference, threshold=0.3)
    amplitude_profile = calculate_amplitude_envelope(seq1)
    baseline_offset = sum(seq1[:10]) / 10
    
    return net_phase

# Main execution
pattern_a = generate_wave_sequence(64, frequency=0.4, phase=0.1)
pattern_b = generate_wave_sequence(64, frequency=0.35, phase=0.25)

# Distractor computations
snapshot = [round(x, 3) for x in pattern_a[::8]]
duplicate_check = any(a == b for a, b in zip(pattern_a, pattern_b))
summary_stats = {
    'max_a': max(pattern_a),
    'min_b': min(pattern_b),
    'len_a': len(pattern_a),
    'product_length': len(pattern_a) * len(pattern_b)
}

# Key statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Additional irrelevant transformation
transformed = [math.tanh(x * 2) for x in pattern_b]
entropy_approx = -sum(x * math.log(abs(x) + 1e-9) for x in transformed)

# Final output
print(f"Result: {net_phase_shift}")