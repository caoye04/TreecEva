from collections import defaultdict, Counter

# Simulate sensor data aggregation in an industrial pipeline
def main():
    raw_readings = [105, 210, 150, 300, 90, 240, 180, 120, 30, 60]
    threshold = 100
    high_load = []
    low_load = []
    temp_accumulator = 0

    # Misleading pre-processing: categorizing but not used later
    for val in raw_readings:
        if val > threshold:
            high_load.append(val * 0.95)  # Simulated loss adjustment
        else:
            low_load.append(val * 1.05)  # Simulated gain adjustment

    # Actual processing path
    processed_data = defaultdict(int)
    for idx, reading in enumerate(raw_readings):
        category = 'critical' if reading > 200 else 'normal'
        processed_data[category] += reading
        temp_accumulator += idx  # Distractor: accumulates index sum (unused)

    # Additional irrelevant transformation
    mirrored_data = [raw_readings[-i-1] for i in range(len(raw_readings))]
    avg_mirror = sum(mirrored_data[:3]) / 3  # Only computes average of first three reversed

    # Conditional expression affecting state
    adjustment_factor = 1.1 if len(high_load) > 4 else 0.9

    # Core calculation function
    def calculate_efficiency(data):
        critical_total = data['critical']
        normal_total = data['normal']
        total = critical_total + normal_total
        ratio = critical_total / total if total != 0 else 0
        return round(ratio * adjustment_factor, 4)

    efficiency_ratio = calculate_efficiency(processed_data)

    # Dead code branch - never executed
    if False:
        fallback = sum(low_load) / len(low_load)
        efficiency_ratio = max(efficiency_ratio, fallback)

    # Output result
    print(f"Result: {efficiency_ratio}")

    return efficiency_ratio

if __name__ == "__main__":
    main()