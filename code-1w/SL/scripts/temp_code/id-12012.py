def main():
    # System performance monitoring with data transformation
    raw_metrics = [120, 85, 90, 110, 95]
    calibration_factor = 0.98
    adjustment_log = []

    # Irrelevant preprocessing: historical baseline (not used in final calculation)
    baseline_history = [88, 92, 87, 93]
    avg_baseline = sum(baseline_history) / len(baseline_history)

    # Relevant data processing
    adjusted_metrics = []
    for val in raw_metrics:
        adjusted = val * calibration_factor
        if adjusted > 90:
            adjusted_metrics.append(adjusted)
        else:
            adjustment_log.append(f'Low value adjusted: {adjusted}')

    # Simulate secondary validation pass (some values rechecked)
    validated_metrics = list(filter(lambda x: x >= 95, adjusted_metrics))

    # Overhead computation from auxiliary sensors (distractor with partial relevance)
    sensor_readings = {'s1': 12, 's2': 8, 's3': 10}
    total_sensors = sum(sensor_readings.values())
    overhead = max(sensor_readings.values()) * 1.5 if total_sensors > 20 else 0

    # Data transformation map for efficiency tiers (dictionary usage)
    efficiency_map = {0: 1.0, 1: 0.95, 2: 0.9, 3: 0.85}
    tier_index = min(len(validated_metrics), 3)
    tier_multiplier = efficiency_map.get(tier_index, 0.8)

    # Final processing pipeline
    processed_data = sum(validated_metrics) * tier_multiplier

    # Critical statement containing the target variable
    efficiency_score = calculate_efficiency(processed_data, overhead)

    # Print result for evaluation
    print(f'Result: {efficiency_score}')


# Helper function for efficiency modeling
def calculate_efficiency(data, overhead):
    base_efficiency = data * 0.75
    penalty = overhead * 2.5
    return int(base_efficiency - penalty)  # Deterministic integer output

if __name__ == '__main__':
    main()