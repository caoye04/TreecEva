def process_data(signal, threshold=3.5):
    # Simulate preprocessing steps with distractions
    normalized = [x / max(signal) for x in signal]
    scaled = [int(x * 100) for x in normalized]

    # Irrelevant transformation (dead-end path)
    inverted = list(map(lambda y: 1/(y+1e-5), normalized))
    avg_inverted = sum(inverted) / len(inverted)

    # Core logic begins: identify peaks above threshold in original scale
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])

    # Distractor: secondary unused peak detection
    troughs = []
    for i in range(1, len(signal) - 1):
        if signal[i] < threshold and signal[i] < signal[i-1] and signal[i] < signal[i+1]:
            troughs.append(signal[i])

    # Apply filtering using set operations to remove duplicates and outliers
    unique_peaks = list(set(peaks))
    clipped_peaks = [min(p, 8.0) for p in unique_peaks]  # artificial ceiling

    # Transform via lambda-based mapping (some values pushed below threshold)
    enhanced = list(map(lambda z: z * 0.9 + 0.5, clipped_peaks))

    # Only keep values that remain above threshold after enhancement
    valid_results = [val for val in enhanced if val > threshold]

    # Compute final result
    filtered_sum = sum(valid_results)

    # Unrelated tracking variable (distractor)
    cumulative_effect = 0
    for v in valid_results:
        cumulative_effect += v * 0.1

    return filtered_sum

# Input data - synthetic sensor readings
data_stream = [2.1, 3.8, 4.5, 3.9, 2.7, 5.2, 6.1, 5.8, 3.0, 4.0, 2.5]

# Call function and extract target variable
result = process_data(data_stream)
filtered_sum = result
print(f"Target result: {filtered_sum}")