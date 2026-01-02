def analyze_signal_data(raw_samples, threshold, window_size):
    # Simulate preprocessing steps with red herrings
    normalized = [x / max(raw_samples) for x in raw_samples]
    smoothed = []
    for i in range(len(normalized)):
        start = max(0, i - window_size // 2)
        end = min(len(normalized), i + window_size // 2 + 1)
        window_avg = sum(normalized[start:end]) / (end - start)
        smoothed.append(window_avg)

    # Irrelevant transformation: frequency domain mock-up
    spectral_magnitude = []
    for i in range(len(smoothed)):
        component = 0
        for j in range(len(smoothed)):
            from math import cos
            component += smoothed[j] * cos(2 * 3.14159 * i * j / len(smoothed))
        spectral_magnitude.append(abs(component))

    # Decoy statistical analysis
    mean_val = sum(smoothed) / len(smoothed)
    variance = sum((x - mean_val) ** 2 for x in smoothed) / len(smoothed)
    stdev = variance ** 0.5
    z_scores = [(x - mean_val) / stdev for x in smoothed]

    # Actual relevant logic buried among distractions
    binary_flags = [1 if x > threshold else 0 for x in raw_samples]
    runs = []
    current_run = 0
    for flag in binary_flags:
        if flag == 1:
            current_run += 1
        else:
            if current_run > 0:
                runs.append(current_run)
                current_run = 0
    if current_run > 0:
        runs.append(current_run)

    # Key data extraction: find longest run and extract subsequence
    max_run_length = max(runs) if runs else 0
    critical_indices = []
    temp_start = 0
    for i, flag in enumerate(binary_flags):
        if flag == 1:
            if current_run == 0:
                temp_start = i
            current_run += 1
            if current_run == max_run_length:
                critical_indices = list(range(temp_start, i + 1))
        else:
            current_run = 0

    # Slice the original data using critical indices
    if critical_indices:
        relevant_subsequence = [raw_samples[i] for i in critical_indices]
    else:
        relevant_subsequence = []

    # Secondary irrelevant filter based on smoothed data
    high_activity_regions = [i for i, x in enumerate(smoothed) if x > 0.75]
    decoy_subsequence = [raw_samples[i] for i in high_activity_regions if i < len(raw_samples)]

    # Another distraction: attempt to correlate with spectral data
    peak_frequency_index = spectral_magnitude.index(max(spectral_magnitude)) if spectral_magnitude else 0
    modulation_factor = spectral_magnitude[peak_frequency_index] if spectral_magnitude else 1.0

    # Final computation path — only this matters
    filtered_sum = sum(relevant_subsequence)

    # Print result as required
    print(f"Result: {filtered_sum}")

    # Dead code paths and unused variables below
    final_output = None
    if modulation_factor > 1.5:
        final_output = [x * modulation_factor for x in decoy_subsequence]
    else:
        final_output = [x for x in raw_samples if x in relevant_subsequence]

    return final_output

# Input data
input_samples = [12, 15, 3, 8, 23, 25, 27, 14, 6, 33, 9, 40, 42, 41, 29, 11, 2]

# Call function
result = analyze_signal_data(input_samples, threshold=20, window_size=5)