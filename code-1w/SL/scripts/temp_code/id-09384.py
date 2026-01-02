import math

def generate_harmonic_sequence(base_freq, duration, sample_rate=1000):
    """Generate a harmonic waveform sequence with decay."""
    timesteps = int(duration * sample_rate)
    signal = []
    for t in range(timesteps):
        time_val = t / sample_rate
        # Fundamental frequency with third harmonic and exponential decay
        amplitude = 0.8 * math.exp(-0.5 * time_val)
        value = amplitude * (
            math.sin(2 * math.pi * base_freq * time_val) + 
            0.3 * math.sin(2 * math.pi * 3 * base_freq * time_val)
        )
        signal.append(value)
    return signal

def compute_envelope_integral(signal, window_size=100):
    """Compute moving RMS envelope and its integral (irrelevant to final answer)."""
    rms_values = []
    integral = 0.0
    for i in range(0, len(signal) - window_size + 1, window_size):
        window = signal[i:i + window_size]
        rms = math.sqrt(sum(x ** 2 for x in window) / len(window))
        rms_values.append(rms)
        integral += rms
    return integral

def detect_zero_crossings(signal):
    """Count zero crossings (semi-relevant distractor)."""
    count = 0
    for i in range(1, len(signal)):
        if signal[i-1] * signal[i] < 0:
            count += 1
    return count

def calculate_interference_phase(signals):
    """Calculate net phase shift from composite signal alignment."""
    total_phase = 0.0
    reference = signals[0]
    for idx, sig in enumerate(signals[1:], start=1):
        correlation_sum = 0.0
        max_correlation = -1
        best_lag = 0
        # Find phase lag via simple cross-correlation peak
        for lag in range(min(50, len(reference), len(sig))):
            corr = 0
            valid_pairs = 0
            for i in range(max(lag, len(sig) - lag)):
                if i < len(sig) and (i + lag) < len(reference):
                    corr += sig[i] * reference[i + lag]
                    valid_pairs += 1
            if valid_pairs > 0:
                corr /= valid_pairs
            if corr > max_correlation:
                max_correlation = corr
                best_lag = lag
        # Convert lag to approximate phase shift in radians
        phase_shift = (best_lag / 1000) * 2 * math.pi * 5  # Assume ~5 Hz signal
        if idx % 2 == 0:
            phase_shift = -phase_shift
        total_phase += phase_shift
    return total_phase

# Main execution block
if __name__ == "__main__":
    # Generate multiple harmonic signals with slight timing differences
    sig_a = generate_harmonic_sequence(5.0, 2.0)
    sig_b = generate_harmonic_sequence(5.1, 2.0)  # Slightly detuned
    sig_c = generate_harmonic_sequence(4.9, 2.0)  # Detuned the other way

    # Irrelevant preprocessing steps (distractors)
    envelope_integral_a = compute_envelope_integral(sig_a)
    envelope_integral_b = compute_envelope_integral(sig_b)
    zc_a = detect_zero_crossings(sig_a)
    zc_b = detect_zero_crossings(sig_b)
    zc_c = detect_zero_crossings(sig_c)

    # Normalize signals (semi-relevant but not used in phase logic directly)
    max_val_a = max(abs(x) for x in sig_a) or 1
    normalized_a = [x / max_val_a for x in sig_a]
    normalized_b = [x / (max(abs(x) for x in sig_b) or 1) for x in sig_b]
    normalized_c = [x / (max(abs(x) for x in sig_c) or 1) for x in sig_c]

    # Composite signal list
    composite_signals = [normalized_a, normalized_b, normalized_c]

    # Key computation step
    net_phase_shift = calculate_interference_phase(composite_signals)

    # Additional irrelevant aggregation
    avg_length = sum(len(s) for s in composite_signals) / len(composite_signals)
    complexity_metric = avg_length * (zc_a + zc_b + zc_c) / (envelope_integral_a + envelope_integral_b + 1)

    # Print target result
    print(f"Result: {net_phase_shift}")