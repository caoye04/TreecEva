def main():
    # Simulate sensor readings and baseline calibration
    readings = [102, 98, 100, 105, 95]
    baseline = 100
    tolerance = 3

    # Compute deviations from baseline
    deviation_map = {}
    for val in readings:
        diff = abs(val - baseline)
        if diff > tolerance:
            deviation_map[val] = diff

    # Penalty function for significant deviations
    penalty_func = lambda x: x * 1.5 if x > 4 else x * 0.8

    # Accumulate total penalty score
    def calculate_total(deviations, func):
        total = 0.0
        for raw_val, dev in deviations.items():
            if raw_val > baseline:
                total += func(dev)
            else:
                total += dev  # No amplification for below-baseline
        return total

    final_score = calculate_total(deviation_map, penalty_func)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()