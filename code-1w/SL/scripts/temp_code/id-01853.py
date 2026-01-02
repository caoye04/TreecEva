def analyze_data_stream(raw_signal, threshold):
    # Simulate preprocessing steps with some irrelevant transformations
    normalized = [round(x * 0.98 + 0.5, 2) for x in raw_signal]
    shifted = [x - 32 for x in normalized if x > 20]  # Partial filtering

    # Irrelevant transformation chain (distractor)
    inverted = [abs(100 - x) for x in normalized]
    mapped_chars = [chr(int(x % 26 + 65)) for x in inverted if 65 <= int(x % 26 + 65) <= 90]
    keyword = ''.join(mapped_chars).lower()

    # Core logic: extract and process relevant frequency peaks
    raw_peaks = [x for x in raw_signal if x > threshold]
    squared_peaks = [x ** 2 for x in raw_peaks]
    root_mean = sum(squared_peaks) ** 0.5 / len(squared_peaks) if squared_peaks else 0

    # Apply dynamic window slicing based on energy level
    energy_level = int(root_mean // 10)
    window_start = max(1, energy_level)
    window_end = max(5, energy_level + 3)

    # Slice the squared_peaks to get significant entries
    sliced_peaks = squared_peaks[window_start:window_end]

    # Further filter only odd-valued peaks (arbitrary criterion)
    valid_entries = [x for x in sliced_peaks if x % 2 == 1]

    # Critical statement
    filtered_sum = sum(valid_entries)

    # Additional red herring computations
    checksum = sum([i * val for i, val in enumerate(valid_entries)])
    scale_factor = 1.0 if not checksum else (filtered_sum / checksum)

    # Output target result
    print(f"Result: {filtered_sum}")

    return filtered_sum

# Input data
signal_input = [12, 45, 23, 67, 34, 89, 14, 76]
threshold_input = 30

result = analyze_data_stream(signal_input, threshold_input)