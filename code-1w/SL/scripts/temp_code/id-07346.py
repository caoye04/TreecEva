def analyze_signal_integrity(raw_samples, threshold=1024):
    sample_size = len(raw_samples)
    baseline = sum(raw_samples) / sample_size if sample_size else 0
    
    # Irrelevant signal preprocessing (distractor)
    normalized_buffer = [((x - baseline) * 1.05) for x in raw_samples]
    outlier_mask = [abs(x) > threshold for x in normalized_buffer]
    masked_count = sum(outlier_mask)

    # Red herring: FFT-like transformation (unused)
    fft_magnitude = [abs(normalized_buffer[i] * (-1)**i) for i in range(len(normalized_buffer))]
    spectral_entropy = sum([x * x for x in fft_magnitude]) / len(fft_magnitude) if fft_magnitude else 0

    # Core logic disguised among distractions
    valid_indices = [i for i in range(sample_size) if i % 3 != 2 and raw_samples[i] > 0]
    filtered_peaks = []
    for idx in valid_indices:
        if idx + 1 < sample_size and raw_samples[idx] < raw_samples[idx + 1]:
            filtered_peaks.append(raw_samples[idx + 1])
        elif idx > 0:
            filtered_peaks.append(raw_samples[idx] // 2)

    # Decoy accumulation path (dead code)
    temp_accumulator = 0
    for peak in filtered_peaks:
        temp_accumulator += peak ^ 255
        if temp_accumulator > 10000:
            temp_accumulator //= 3

    # Actual computation chain (buried)
    shift_offset = len(filtered_peaks) & 7
    rolled_values = [raw_samples[(i - shift_offset) % sample_size] for i in range(sample_size)]
    rolled_avg = sum(rolled_values) / sample_size

    # Conditional expression used per requirement
    normalization_factor = rolled_avg if rolled_avg > 1e-5 else 1
    aggregate_metric = sum([v ** 2 for v in rolled_values if v % 2 == 1])

    # Key statement
    filtration_score = aggregate_metric // (normalization_factor or 1)

    # More red herrings below
    diagnostic_checksum = 0
    for i, v in enumerate(rolled_values):
        diagnostic_checksum ^= (i + v) & 0xFF
    # Unused nested structure
    if diagnostic_checksum > 200:
        for _ in range(3):
            diagnostic_checksum >>= 1

    return filtration_score

# Simulated sensor data (fixed seed equivalent)
input_stream = [128, 255, 192, 64, 320, 768, 512, 896, 1023, 110]
result = analyze_signal_integrity(input_stream)
print(f"Result: {result}")