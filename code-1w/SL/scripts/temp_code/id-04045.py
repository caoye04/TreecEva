import math

# Simulated sensor data preprocessing with interference
def analyze_signal_integrity(raw_samples):
    if len(raw_samples) < 10:
        return 0

    # Irrelevant normalization branch (dead path due to input size)
    normalized = [x / max(raw_samples) for x in raw_samples] if max(raw_samples) != 0 else raw_samples

    # Distractor: unused frequency analysis
    fft_magnitude = []
    for i in range(len(raw_samples)):
        real = sum(raw_samples[j] * math.cos(2 * math.pi * i * j / len(raw_samples)) for j in range(len(raw_samples)))
        imag = sum(-raw_samples[j] * math.sin(2 * math.pi * i * j / len(raw_samples)) for j in range(len(raw_samples)))
        fft_magnitude.append(math.sqrt(real**2 + imag**2))

    # Actual relevant transformation chain
    filtered = [x for x in raw_samples if x > 1.5]  # Filter noise floor
    if len(filtered) == 0:
        filtered = [0]

    # Introduce decoy statistical measures
    mean_val = sum(filtered) / len(filtered)
    variance = sum((x - mean_val)**2 for x in filtered) / len(filtered)
    skewness_estimate = sum((x - mean_val)**3 for x in filtered) / (len(filtered) * variance**1.5) if variance > 0 else 0

    # Red herring: unused peak detection
    peaks = []
    for i in range(1, len(filtered)-1):
        if filtered[i-1] < filtered[i] > filtered[i+1]:
            peaks.append(i)

    # Critical data slicing and transformation
    mid_segment = filtered[len(filtered)//4 : len(filtered)*3//4]
    if not mid_segment:
        mid_segment = [1]

    # Decoy entropy calculation
    probability_dist = [mid_segment.count(x)/len(mid_segment) for x in set(mid_segment)]
    shannon_entropy = -sum(p * math.log2(p) for p in probability_dist if p > 0)

    # Key transformation sequence begins
    accumulated = 1.0
    for val in mid_segment:
        accumulated *= (val + 0.5)
        accumulated = math.fmod(accumulated, 100000.0)

    # Another distraction: unused pattern matcher
    pattern_found = False
    for i in range(len(mid_segment) - 2):
        if mid_segment[i] < mid_segment[i+1] > mid_segment[i+2]:
            if abs(mid_segment[i] - mid_segment[i+2]) < 0.1:
                pattern_found = True
                break

    # Core processing function defined inside (closure)
    def process_chunk(data_slice, width):
        if width <= 0:
            width = 1
        # Slice with dynamic bounds
        effective = data_slice[:len(data_slice)//width + 1] if width > 1 else data_slice
        result = 0
        for idx, item in enumerate(effective):
            # Interleaved arithmetic and bit manipulation
            temp = (idx + 1) * item
            temp = int(temp) ^ int(item * 10)  # XOR operation
            result += abs(temp)
        return result + len(effective)

    base_shift = 3
    transformed_data = [math.floor(x * base_shift) for x in mid_segment]
    window_size = len(transformed_data) // 5 or 2

    # Apply slicing with step (python-specific feature)
    transformed_data = transformed_data[::-2] if len(transformed_data) > 4 else transformed_data

    # Critical execution point
    phase_output = process_chunk(transformed_data, window_size)

    # Final irrelevant aggregation
    final_diagnostic = 0
    for i in range(len(transformed_data)):
        final_diagnostic += math.sin(transformed_data[i]) * math.cos(i)

    print(f"Result: {phase_output}")
    return phase_output

# Generate deterministic input
input_signal = [1.2, 2.7, 3.1, 4.9, 2.3, 5.0, 6.8, 4.2, 3.9, 5.5, 6.1, 7.2]
analyze_signal_integrity(input_signal)