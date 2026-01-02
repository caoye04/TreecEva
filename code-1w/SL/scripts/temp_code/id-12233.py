def analyze_sensor_readings(readings):
    # Irrelevant transformation: normalize readings (not used in final result)
    normalized = [round((r - min(readings)) / (max(readings) - min(readings)) * 100) for r in readings]

    # Decoy statistical computation
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_deviation = variance ** 0.5

    # Simulated timestamp alignment (dead code path)
    timestamps = list(range(len(readings)))
    aligned_pairs = [(ts, val) for ts, val in zip(timestamps, readings) if val > mean_val]

    # Actual processing begins here
    outlier_threshold = 2 * std_deviation
    cleaned_data = [x for x in readings if abs(x - mean_val) < outlier_threshold]

    # Bit manipulation red herring
    bit_analysis = []
    for val in cleaned_data:
        flipped = val ^ 255  # XOR with 255 (irrelevant)
        rotated = ((flipped << 1) & 255) | (flipped >> 7)  # Circular shift
        bit_analysis.append(rotated)

    # Conditional data slicing based on index parity
    even_indexed = cleaned_data[::2]
    odd_indexed = cleaned_data[1::2]

    # Set operations to filter duplicates and apply constraints
    unique_evens = set(even_indexed)
    unique_odds = set(odd_indexed)
    common_elements = unique_evens & unique_odds  # Intersection (mostly empty, distraction)

    # Real logic: filter values above dynamic threshold
    dynamic_floor = len(cleaned_data) // 3
    if dynamic_floor > 5:
        threshold = mean_val + std_deviation
    else:
        threshold = mean_val

    # Key filtering operation
    filtered_data = [x for x in even_indexed if x > threshold]

    # Add dummy transformations on filtered data
    transformed = [x * 2 + 1 for x in filtered_data if x % 2 == 0]  # Only evens processed

    # Final summation
    filtered_sum = sum(filtered_data)

    # Dead print statements (distractors)
    # print(f"Normalized: {normalized}")
    # print(f"Bit analysis peak: {max(bit_analysis)}")
    # print(f"Common elements: {common_elements}")

    return filtered_sum

# Input data with subtle skew
sensor_inputs = [12, 45, 67, 34, 23, 89, 23, 56, 78, 12, 45, 67, 91, 15, 14]
result = analyze_sensor_readings(sensor_inputs)
print(f"Target result: {result}")