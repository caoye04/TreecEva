def main():
    # Simulate sensor readings and calibration adjustments
    base_readings = [3.2, 4.1, 2.8, 5.6, 3.9]
    threshold = 3.5
    scaling_factor = 1.75

    # Identify deviations above threshold
    significant_dev = list(filter(lambda x: x > threshold, base_readings))

    # Calculate mean deviation for adjustment
    if len(significant_dev) > 0:
        mean_dev = sum(significant_dev) / len(significant_dev)
    else:
        mean_dev = 0.0

    # Create mapping of individual deviations from mean
    deviation_map = list(map(lambda x: round(x - mean_dev, 2), significant_dev))

    # Secondary processing: count how many are above median
    sorted_dev = sorted(deviation_map)
    mid = len(sorted_dev) // 2
    median_dev = (sorted_dev[mid] + sorted_dev[~mid]) / 2 if len(sorted_dev) % 2 == 0 else sorted_dev[mid]

    # Irrelevant tracking variable (minor distraction)
    update_counter = 0
    for _ in sorted_dev:
        update_counter += 1

    # Core calculation function
    def calculate_total(devs, scale):
        total = 0
        for val in devs:
            if val > median_dev:
                total += val * scale
            else:
                total += val + scale
        return round(total, 3)

    final_score = calculate_total(deviation_map, scaling_factor)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()