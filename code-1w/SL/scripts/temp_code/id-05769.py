def main():
    # Sensor data processing simulation with pattern matching
    raw_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    base_pattern = [1, 5, 9]

    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_readings) for x in raw_readings]
    scaled_sum = sum(normalized) * 100

    # Extract every third reading starting from index 1 (relevant filtering)
    filtered_data = raw_readings[1::3]  # -> [1, 9, 3, 7]

    # Misleading statistical computation (dead-end path)
    avg_val = sum(filtered_data) / len(filtered_data)
    variance_proxy = sum((x - avg_val) ** 2 for x in filtered_data)

    # Auxiliary function using lambda for sliding window (relevant)
    sliding_windows = lambda seq, n: [seq[i:i+n] for i in range(len(seq)-n+1)]

    # Compare filtered segments to base pattern (key logic)
    matches = 0
    for window in sliding_windows(filtered_data, len(base_pattern)):
        if all(a == b for a, b in zip(window, base_pattern)):
            matches += 1

    # Secondary distraction: complex but unused structure
    histogram = {x: filtered_data.count(x) for x in set(filtered_data)}
    outlier_count = len([x for x in filtered_data if x > 5])

    # Core scoring logic
    def compute_threshold(data, pattern):
        length_factor = len(data) * 0.5
        match_bonus = matches * 10
        entropy_component = 0
        for x in data:
            if x > 0:
                entropy_component += x * (-x / sum(data))
        return int(length_factor + match_bonus + 5 * abs(entropy_component))

    # Critical assignment point
    activation_score = compute_threshold(filtered_data, base_pattern)

    # Final red herring: unrelated calculation
    compression_ratio = len(raw_readings) / len(str(raw_readings))

    print(f"Result: {activation_score}")

if __name__ == "__main__":
    main()