import math

# Simulated sensor signal processing with diagnostic analysis
def generate_wave_components(frequency, phase, length):
    return [math.sin(2 * math.pi * (i * frequency + phase)) for i in range(length)]

# Irrelevant helper: generates harmonic noise (not used in final result)
def generate_harmonic_noise(intensity, size):
    return [(i % 7) * intensity / 100 for i in range(size)]

# Signal smoothing using moving average (used)
def smooth_signal(data, window_size=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window = data[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Outlier detection (distractor - not used)
def detect_outliers(values, std_factor=2.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [abs(x - mean_val) > std_factor * std_dev for x in values]

# Frequency domain transformation attempt (dead path)
def apply_dft(signal):
    N = len(signal)
    dft_result = []
    for k in range(N):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = -sum(signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        dft_result.append(complex(real, imag))
    return dft_result

# Main pattern analyzer (critical function)
def analyze_pattern(sequence, threshold_filter):
    # Step 1: Smooth the input sequence
    processed = smooth_signal(sequence)
    
    # Step 2: Apply threshold filter to highlight significant peaks
    filtered = [x if abs(x) > threshold_filter else 0 for x in processed]
    
    # Step 3: Find zero-crossing rate as stability indicator
    zero_crossings = 0
    for i in range(1, len(filtered)):
        if filtered[i-1] * filtered[i] < 0:
            zero_crossings += 1
    
    # Step 4: Compute energy of filtered signal
    energy = sum(x * x for x in filtered)
    
    # Step 5: Count sustained activity periods (consecutive non-zero)
    active_periods = 0
    current_streak = 0
    for val in filtered:
        if val != 0:
            current_streak += 1
        else:
            if current_streak >= 3:
                active_periods += 1
            current_streak = 0
    if current_streak >= 3:
        active_periods += 1
    
    # Step 6: Apply weighting formula for diagnostic score
    stability_index = (len(processed) - zero_crossings) / len(processed)
    diagnostic_score = energy * stability_index * (1 + active_periods)
    
    # Step 7: Apply nonlinear compression via lambda
    compress = lambda x: math.log(1 + x) if x > 0 else 0
    compressed_diagnostic = compress(diagnostic_score)
    
    # Step 8: Final adjustment using modular arithmetic
    seed_offset = 17
    final_value = (int(compressed_diagnostic * 1000) + seed_offset) % 98765
    
    return final_value

# Generate primary signal components
base_signal = generate_wave_components(0.08, 0.25, 128)
noise_component = [0.1 * ((i % 11) - 5) / 10 for i in range(128)]  # Minor noise
signal_sequence = [base_signal[i] + noise_component[i] for i in range(128)]

# Unused transformations (distractors)
dft_view = apply_dft(signal_sequence)
outlier_flags = detect_outliers(signal_sequence)
harmonics = generate_harmonic_noise(5.0, 64)

# Critical filtering threshold
threshold_filter = 0.45

# Perform analysis
final_diagnostic = analyze_pattern(signal_sequence, threshold_filter)

# Additional red herring computations
snapshot = signal_sequence[::8]  # Slicing operation (irrelevant)
summary_stats = list(map(lambda x: round(x, 2), [sum(signal_sequence), min(signal_sequence), max(signal_sequence)]))
entropy_proxy = -sum(x*x for x in summary_stats) % 1000

# Print final result
print(f"Result: {final_diagnostic}")