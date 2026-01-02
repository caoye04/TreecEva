from collections import defaultdict, Counter

# Simulated sensor data ingestion and diagnostic pipeline
def main():
    raw_readings = [
        (1001, 23.5), (1002, 45.0), (1003, 12.8), (1004, 67.3),
        (1005, 23.5), (1006, 89.1), (1007, 45.0), (1008, 23.5),
        (1009, 12.8), (1010, 67.3)
    ]

    # Irrelevant mapping - decoy for device calibration (not used in logic)
    calibration_map = {i: (i * 0.95 + 3) for i in range(1000, 1020)}

    # Thresholds for anomaly detection (used later)
    threshold_map = defaultdict(lambda: 50.0)
    for k, v in [(1001, 25.0), (1004, 70.0), (1006, 90.0), (1008, 30.0)]:
        threshold_map[k] = v

    # Extract values and count frequency (used in filtering)
    values_only = [r[1] for r in raw_readings]
    freq_count = Counter(values_only)

    # Filtering: only keep readings where value appears more than once OR device ID is odd
    filtered_data = []
    for device_id, value in raw_readings:
        if freq_count[value] > 1 or device_id % 2 == 1:
            filtered_data.append((device_id, value))

    # Decoy transformation - unused but looks important
    transformed = [round(v ** 0.5 * 1.1, 2) for v in values_only if v > 20]
    normalized = [((v - min(values_only)) / (max(values_only) - min(values_only))) for v in values_only]

    # Auxiliary function that appears relevant but is not called
    def legacy_filter(data, limit=20):
        return [x for x in data if x[1] < limit]

    # Another red herring: historical baseline comparison
    historical_avg = sum([22.1, 23.5, 24.0, 23.8, 25.2]) / 5
    deviation_score = abs(historical_avg - values_only[0])

    # Key processing function
    def process_readings(data, thresholds):
        aggregate = 0
        status_flags = []

        for dev_id, val in data:
            # Bit manipulation as part of diagnostic hash
            meta_tag = dev_id ^ int(val)  # XOR operation
            meta_tag = (meta_tag << 2) & 0xFF  # Shift and mask

            # Conditional expression for flag assignment
            flag = 1 if (meta_tag % 3 == 0) else (-1 if meta_tag > 100 else 0)
            status_flags.append(flag)

            # Actual accumulation logic
            threshold = thresholds[dev_id]
            if val > threshold:
                aggregate += int(val) % 7  # modular arithmetic
            elif val < threshold:
                aggregate -= int(dev_id) % 5
            else:
                aggregate += 1

        # Final adjustment based on flag pattern
        flag_counter = Counter(status_flags)
        net_effect = flag_counter[1] * 2 - flag_counter[-1] * 3

        result = aggregate + net_effect

        # Dead code branch - never executed due to logic above
        if False and len(data) > 100:
            backup = sum([d[1] for d in data]) // len(data)
            result = backup

        return result

    # Unused recursive helper - looks important but irrelevant
    def recursive_sum(n):
        return n + recursive_sum(n - 1) if n > 0 else 0

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Misleading secondary calculation
    phantom_index = sum([int(d[1]) for d in raw_readings if d[0] % 3 == 0]) // 3

    # Output required value
    print(f"Result: {final_diagnostic}")

    # Return for clarity (though print is the required output)
    return final_diagnostic

if __name__ == "__main__":
    main()