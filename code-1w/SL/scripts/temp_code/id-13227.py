from itertools import compress, cycle

def analyze_sensor_network():
    # Simulated sensor IDs and raw voltage readings
    sensor_ids = [f'SEN{str(i).zfill(3)}' for i in range(1, 18)]
    raw_readings = [4.21, 3.98, 5.01, 4.44, 3.87, 5.12, 4.65, 4.33, 4.77, 4.05, 4.91, 4.22, 4.66, 4.39, 4.82, 4.15, 4.53]

    # Irrelevant calibration coefficients (distractor)
    calib_factors = [1.02, 0.99, 1.05, 1.01, 0.97, 1.03, 1.00, 0.98, 1.04, 1.02, 0.99, 1.06, 1.00, 0.98, 1.03, 1.01, 1.02]
    calibrated_values = [raw_readings[i] * calib_factors[i] for i in range(len(raw_readings))]  # Unused downstream

    # Threshold policies per sensor class (A: critical, B: standard, C: auxiliary)
    sensor_classes = ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'A']
    threshold_map = {'A': 4.75, 'B': 4.40, 'C': 4.20}

    # Flag sensors above class-specific thresholds
    above_threshold = [raw_readings[i] > threshold_map[sensor_classes[i]] for i in range(len(sensor_ids))]

    # Extract only sensors that are both active and above threshold
    active_mask = [i % 3 != 0 for i in range(len(sensor_ids))]  # Every 3rd sensor inactive
    filtered_data = list(compress(raw_readings, (a and b for a, b in zip(above_threshold, active_mask))))

    # Decoy transformation: normalize all readings (unused)
    max_reading = max(raw_readings)
    normalized = [x / max_reading for x in raw_readings]

    # Simulate packet loss pattern with cycle (irrelevant)
    transmission_cycle = list(cycle([True, True, False]))[:len(sensor_ids)]
    valid_transmission = [active_mask[i] and transmission_cycle[i] for i in range(len(sensor_ids))]

    # Debug: count how many sensors are in each class (red herring)
    class_count = {}
    for cls in sensor_classes:
        class_count[cls] = class_count.get(cls, 0) + 1

    # Begin processing relevant data
    def process_readings(data, thresholds):
        base_score = sum(int(x * 100) for x in data)
        penalty = 0

        # Artificial complexity: apply dynamic penalty based on digit patterns
        for val in data:
            cents = int(round(val * 100)) % 100
            if cents % 11 == 0:  # divisible by 11 in cents
                penalty += 5
            if cents > 50:
                penalty += 2

        # Additional decoy logic: analyze digit frequency (never used)
        digit_freq = {str(i): 0 for i in range(10)}
        for val in data:
            for char in f'{val:.2f}':
                if char.isdigit():
                    digit_freq[char] += 1
        rare_digits = sum(1 for v in digit_freq.values() if v < 3)  # unused

        # Real computation path
        adjustment = len(data) * 3
        return base_score - penalty + adjustment

    # Misleading early assignment (overwritten later)
    final_diagnostic = -999

    # Key statement
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Dead code path: simulation of rollback (never executed)
    try:
        raise ValueError('Simulated fault')
    except ValueError:
        if len(filtered_data) > 10:
            final_diagnostic = sum(filtered_data)  # unreachable due to condition

    # Final red herring: string-based checksum (unrelated)
    label_stream = ''.join(sensor_ids)
    checksum = sum(ord(c) for c in label_stream if c in 'AEIOU') % 100

    print(f'Result: {final_diagnostic}')

analyze_sensor_network()