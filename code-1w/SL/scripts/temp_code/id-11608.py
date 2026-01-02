from collections import defaultdict

# Simulate sensor data aggregation and anomaly detection
def collect_sensor_metrics(raw_readings):
    processed = defaultdict(float)
    anomalies = 0
    temp_buffer = []

    for reading in raw_readings:
        sensor_id = reading['sensor']
        value = reading['value']
        timestamp = reading['time']

        if value < 0:
            anomalies += 1
            continue

        processed[sensor_id] += value / 10.0

        if timestamp % 100 == 0:
            temp_buffer.append(value)

    # Irrelevant summary (distractor)
    avg_buffer = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return dict(processed), anomalies

def compute_stability_index(data, base_threshold=5.0):
    index = 1.0
    fluctuation_count = 0
    prev = 0

    for val in sorted(data.values()):
        if abs(val - prev) > base_threshold:
            fluctuation_count += 1
            index *= 0.9
        prev = val

    # Dead computation - not used later
    normalized_index = index / (fluctuation_count + 1e-5)
    return index

def apply_correction_factor(x, factor=1.1):
    # Simple helper, minor relevance
    return x * factor

def evaluate_performance(metrics, config):
    score = 0
    weighted_sum = 0.0
    penalty = 0

    for sensor, value in metrics.items():
        if sensor.startswith('A'):
            weighted_sum += apply_correction_factor(value)
        elif sensor.startswith('B'):
            weighted_sum += value * config.get('B_weight', 1.2)
        else:
            weighted_sum += value * 0.8

    stability = compute_stability_index(metrics)
    base_score = int(weighted_sum * 10)

    # Apply modular logic for bonus/penalty
    if base_score % 7 == 0:
        penalty += 5
    elif base_score % 5 == 0:
        base_score += 10  # Bonus case

    # Final adjustment
    adjusted_score = base_score - penalty
    final_score = int(adjusted_score * stability)

    # Red herring variables
    debug_info = {'base': base_score, 'penalty': penalty, 'stability': stability}
    temp_result = adjusted_score + sum(debug_info.values())  # unused

    return final_score

# Main execution
if __name__ == "__main__":
    readings = [
        {'sensor': 'A1', 'value': 25, 'time': 100},
        {'sensor': 'A2', 'value': 30, 'time': 200},
        {'sensor': 'B1', 'value': 40, 'time': 300},
        {'sensor': 'B2', 'value': 35, 'time': 400},
        {'sensor': 'C1', 'value': 50, 'time': 500},
        {'sensor': 'A3', 'value': 20, 'time': 600},
    ]

    threshold_config = {
        'B_weight': 1.2,
        'stability_floor': 0.8
    }

    # Step 1: Collect and process sensor data
    metric_data, err_count = collect_sensor_metrics(readings)

    # Step 2: Evaluate overall performance
    final_score = evaluate_performance(metric_data, threshold_config)

    print(f"Result: {final_score}")