def main():
    # Sensor data processing simulation with health metrics
    raw_readings = [105, 210, 150, 180, 95, 240]
    baseline = 150
    adjustment_factor = 0.85

    # Irrelevant transformation (distractor)
    adjusted_readings = list(map(lambda x: (x - baseline) * adjustment_factor + baseline, raw_readings))

    # Key data for analysis
    filtered_readings = [val for val in raw_readings if val > 100]

    # Auxiliary calculations (some used, some not)
    sum_high = sum(filtered_readings)
    count_high = len(filtered_readings)
    average_high = sum_high / count_high if count_high else 0

    # Dead code path (distractor)
    temp_offsets = []
    for reading in raw_readings:
        if reading > 200:
            temp_offsets.append(reading * 0.05)

    # Simulate time decay on irrelevant metric
    decay_rate = 0.9
    cumulative_drift = 0
    for i in range(3):
        cumulative_drift += adjustment_factor * (decay_rate ** i)

    # Core logic variables
    metrics = {
        'peak': max(raw_readings),
        'avg': average_high,
        'stability': sum(1 for x in raw_readings if abs(x - baseline) < 50)
    }

    threshold = 120

    def calculate_performance(data, limit):
        # Performance model using lambda and conditional logic
        penalty_fn = lambda x: 0.9 if x < limit else 1.0
        base_score = data['avg'] * penalty_fn(data['avg'])
        peak_bonus = 10 if data['peak'] > 200 else 0
        stability_weight = 1.2 if data['stability'] >= 4 else 0.8

        # Final computation
        efficiency_score = (base_score + peak_bonus) * stability_weight

        # Red herring calculation
        dummy_score = (data['peak'] - base_score) * 0.5
        return efficiency_score  # Only efficiency_score matters

    final_output = calculate_performance(metrics, threshold)

    # Output requirement
    print(f"Result: {final_output}")

if __name__ == "__main__":
    main()