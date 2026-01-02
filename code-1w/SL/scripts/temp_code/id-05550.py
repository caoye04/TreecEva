def main():
    # Sensor calibration data simulation
    raw_readings = [104, 211, 156, 93, 187]
    baseline = 100
    adjusted = [x - baseline for x in raw_readings]

    # Irrelevant auxiliary variable (mild distraction)
    sample_ids = ['S1', 'S2', 'S3', 'S4', 'S5']

    threshold_filter = lambda x: x > 50
    processed = list(filter(threshold_filter, adjusted))

    # Rule-based transformation using dictionary mapping
    rules = {56: 3, 87: 5, 11: 1}
    default_rule = 2

    # Complex transformation function involving slicing and conditional logic
    def transform_data(data, rule_map):
        if not data:
            return 0
        # Use of slicing to take only first two valid elements
        subset = data[:2]
        total = 0
        for val in subset:
            # Map values using dictionary with fallback
            multiplier = rule_map.get(val, default_rule)
            total += val // 10 * multiplier  # Integer division and scaling
        return total if total != 0 else -1

    result = transform_data(processed, rules)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()