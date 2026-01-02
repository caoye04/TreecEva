from collections import defaultdict

# Simulate sensor data aggregation and anomaly-adjusted scoring
def collect_sensor_metrics(raw_readings):
    metrics = defaultdict(float)
    temp_count = 0
    total_temp = 0.0
    spike_count = 0

    for reading in raw_readings:
        sensor_id = reading['id']
        value = reading['value']
        timestamp = reading['time']

        # Track per-sensor averages
        metrics[f'{sensor_id}_sum'] += value
        metrics[f'{sensor_id}_count'] += 1

        # Accumulate global temperature stats (distractor)
        if sensor_id == 'TEMP01':
            total_temp += value
            temp_count += 1

        # Detect sudden spikes (used later)
        if value > 95:
            spike_count += 1

    # Compute average for TEMP01 (semi-relevant but not final)
    if temp_count > 0:
        metrics['temp_avg'] = total_temp / temp_count
    else:
        metrics['temp_avg'] = 0.0

    # Store spike count for adjustment
    metrics['spike_count'] = spike_count

    return metrics

def apply_calibration(baseline, adjustments):
    calibrated = {}
    noise_floor = 0.0  # Distractor variable
    drift_factor = 1.0  # Another distractor

    for key, value in baseline.items():
        if '_sum' in key:
            sensor = key.replace('_sum', '')
            count_key = f'{sensor}_count'
            if count_key in baseline:
                avg_val = value / baseline[count_key]
                calibrated[sensor] = avg_val * 0.9 + adjustments.get(sensor, 1.0) * 0.1

    # Fake noise processing (dead computation path)
    for i in range(2):
        noise_floor += 0.01 * drift_factor

    return calibrated

def calculate_final_score(metrics, weight_map):
    base_score = 0.0
    penalty = 0.0
    bonus = 0.0

    # Score contributions from calibrated sensors
    for sensor, value in metrics.items():
        contribution = value * weight_map.get(sensor, 0.5)
        if contribution > 10:
            bonus += 1.5
        elif contribution < 3:
            penalty += 0.8
        base_score += contribution

    # Adjust based on spike count (actual logic path)
    if metrics.get('spike_count', 0) > 2:
        penalty += 2.5
    else:
        bonus += 1.0

    # Final score with bonus/penalty
    final_score = base_score + bonus - penalty

    # Red herring normalization (not affecting result)
    if final_score > 0:
        normalized = final_score / (1 + 0.05)

    return int(round(final_score))

# Main execution
if __name__ == '__main__':
    # Input data
    readings = [
        {'id': 'TEMP01', 'value': 98, 'time': 100},
        {'id': 'TEMP01', 'value': 96, 'time': 101},
        {'id': 'PRESS01', 'value': 88, 'time': 100},
        {'id': 'PRESS01', 'value': 85, 'time': 101},
        {'id': 'VIBRO01', 'value': 70, 'time': 100},
        {'id': 'VIBRO01', 'value': 99, 'time': 101},  # Spike
        {'id': 'VIBRO01', 'value': 97, 'time': 102},  # Spike
        {'id': 'VIBRO01', 'value': 96, 'time': 103}   # Spike
    ]

    # Weight configuration
    weights = {
        'TEMP01': 0.8,
        'PRESS01': 0.6,
        'VIBRO01': 0.7
    }

    # Step 1: Collect raw metrics
    raw_metrics = collect_sensor_metrics(readings)

    # Step 2: Apply calibration using dummy adjustments
    adjustments = {'TEMP01': 1.1, 'PRESS01': 0.9, 'VIBRO01': 1.2}
    calibrated_metrics = apply_calibration(raw_metrics, adjustments)

    # Step 3: Calculate final score
    final_score = calculate_final_score(calibrated_metrics, weights)

    print(f"Result: {final_score}")