import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_health(raw_readings, calibration_factor):
    # Irrelevant helper function (dead code path)
    def apply_fourier_transform(signal):
        return [math.sin(x / 3.14159) for x in signal]

    # Another decoy transformation
    transformed = [x * 0.9 + 2 for x in raw_readings]

    # Real processing begins: remove outliers beyond 3σ (but calculated simply here)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)
    filtered_data = [x for x in raw_readings if abs(x - mean_val) <= 2 * std_dev]

    # Decoy statistical analysis
    skewness = sum((x - mean_val) ** 3 for x in raw_readings) / (len(raw_readings) * std_dev ** 3)
    kurtosis = sum((x - mean_val) ** 4 for x in raw_readings) / (len(raw_readings) * std_dev ** 4) - 3

    # Unused intermediate scores
    stability_score = 100 - (std_dev * 10)
    linearity_index = abs(skewness) + 0.1 * kurtosis

    # Actual key threshold map construction (relevant)
    threshold_map = {
        'low': mean_val - std_dev,
        'high': mean_val + std_dev,
        'critical': mean_val + 2 * std_dev
    }

    # Red herring: unused data structure
    diagnostic_log = {
        'timestamp': 1678886400,
        'nodes': [f'N{i}' for i in range(len(raw_readings))],
        'checksum': sum(int(x) for x in raw_readings) % 1000
    }

    # Misleading early aggregation
    aggregated_diagnostics = [
        {'node': i, 'status': 'OK' if val > mean_val else 'LOW', 'raw': val}
        for i, val in enumerate(transformed)
    ]

    # This function is never called but looks important
    generate_report = lambda log, score: f"Report: {score:.2f} ({log['checksum']})"

    # Key call buried in logic
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Dead branch (never reached due to return above)
    if False:
        backup_diagnostic = 0
        for val in transformed:
            if val > threshold_map['critical']:
                backup_diagnostic += 1
        final_diagnostic = max(final_diagnostic, backup_diagnostic)

    return final_diagnostic


def process_readings(data, thresholds):
    # Count how many readings exceed high threshold but are below critical
    valid_range_count = 0
    penalty_factor = 0.0

    # Complex conditional counting with string-based flags (distractor)
    status_flags = []
    for d in data:
        if d < thresholds['low']:
            flag = 'L'
            penalty_factor += 0.1
        elif d > thresholds['high']:
            flag = 'H'
            if d < thresholds['critical']:
                valid_range_count += 1  # Only count those in 'warning but okay' zone
        else:
            flag = 'M'
        status_flags.append(flag)

    # Irrelevant string manipulation
    flag_string = ''.join(status_flags)
    runs = 1
    for i in range(1, len(flag_string)):
        if flag_string[i] != flag_string[i-1]:
            runs += 1

    # Another decoy calculation using dictionary methods
    frequency_map = {}
    for char in flag_string:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    entropy = 0.0
    total = len(flag_string)
    for count in frequency_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0

    # Core logic hidden among distractions: apply combinatoric adjustment
    n = valid_range_count
    adjustment = math.factorial(n) // (math.factorial(max(n-2, 1)) * 2) if n >= 2 else n

    # Final result computation
    result = int((adjustment * 17) - (penalty_factor * 100))

    # Additional red herring: unused complex expression
    aux_score = entropy * runs * (frequency_map.get('H', 0) + 1)

    return result

# Entry point
if __name__ == '__main__':
    sensor_inputs = [12.1, 15.3, 9.8, 18.7, 14.2, 22.5, 13.9, 16.1, 8.4, 17.3]
    scaling_factor = 1.05

    # Unused alternate dataset
    dummy_sensors = [x * 0.5 + 3 for x in reversed(sensor_inputs)]

    # Trigger main logic
    final_diagnostic = analyze_sensor_health(sensor_inputs, scaling_factor)

    # Output target variable
    print(f"Target result: {final_diagnostic}")