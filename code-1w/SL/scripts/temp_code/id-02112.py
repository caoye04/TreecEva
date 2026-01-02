def main():
    # Environmental monitoring simulation with data transformation
    raw_readings = [12, 15, 18, 22, 14, 25, 30, 28, 20, 16]
    baseline = 18
    adjustment_factor = 1.25

    # Irrelevant intermediate calculation (distractor)
    avg_reading = sum(raw_readings) / len(raw_readings)
    deviation = [abs(x - avg_reading) for x in raw_readings]
    max_dev = max(deviation)

    # Normalize and scale relevant data
    normalized = [(x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) for x in raw_readings]
    scaled_values = [round(x * adjustment_factor * 100) for x in normalized]

    # Threshold logic with helper tracking
    threshold_map = {}
    for i, val in enumerate(scaled_values):
        category = 'low'
        if val > 60:
            category = 'high'
        elif val > 40:
            category = 'moderate'
        threshold_map[i] = {'value': val, 'level': category}

    # Dead code path (misleading control flow)
    temp_stats = {}
    if False:  # Simulated condition that never triggers
        temp_stats = {
            'count_high': len([v for v in scaled_values if v > 70]),
            'sum_extreme': sum(v for v in scaled_values if v > 80)
        }

    # Actual threshold bounds for aggregation
    thresholds = {'min_qualifying': 50, 'boost_trigger': 75}

    def compute_aggregate(values, config):
        total = 0
        bonus_applied = False
        for idx, v in enumerate(values):
            if v >= config['min_qualifying']:
                total += v
                # Boost logic
                if not bonus_applied and v >= config['boost_trigger']:
                    total += 10  # Bonus point for first high-tier value
                    bonus_applied = True
        return total

    # Key computation step
    final_score = compute_aggregate(scaled_values, thresholds)

    # Auxiliary diagnostic output (irrelevant to result)
    outlier_count = len([v for v in deviation if v > 2 * (sum(deviation)/len(deviation))])
    consistency_check = all(scaled_values[i] <= scaled_values[i+1] for i in range(len(scaled_values)-1))

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()