def analyze_component_health(sensor_readings, thresholds):
    # Irrelevant function – dead code path
    health_status = {}
    for comp, value in sensor_readings.items():
        health_status[comp] = value < thresholds.get(comp, 100)
    return health_status


def transform_case(strings, mode='upper'):
    # Distractor: string manipulation with no impact on final result
    if mode == 'upper':
        return [s.upper() for s in strings]
    else:
        return [s.lower() for s in strings]


def compute_checksum(data_stream):
    # Red herring: bit manipulation that looks important but is unused
    checksum = 0
    for val in data_stream:
        checksum ^= val << 1
        checksum &= 0xFFFF
    return checksum


def filter_outliers(values, margin=1.5):
    # Seemingly relevant data processing, but not used in main logic
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - margin * iqr
    upper_bound = q3 + margin * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]


def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    base_scores = {}
    adjustment_factor = 0.85

    # Simulate multi-step scoring with conditional weighting
    for idx, (metric, value) in enumerate(zip(metrics, [x * 1.1 for x in metrics])):
        temp_key = f'metric_{idx}'
        if temp_key not in ['metric_99']:  # Fake conditional guard
            scaled = value * weights[idx]
            if scaled > 50:
                scaled = scaled * adjustment_factor  # First adjustment
            base_scores[temp_key] = round(scaled, 4)

    # Aggregate using dictionary and list together
    score_list = [v for k, v in base_scores.items()]
    
    # Real computation buried here
    aggregate = sum(score_list)
    penalty = 0
    for i, val in enumerate(score_list):
        if i % 2 == 1:
            penalty += val * 0.02  # Small penalty on odd indices

    final = aggregate - penalty

    # Decoy intermediate print
    debug_value = int(final ^ 0xABCD) & 0xFFFF  # Bitwise decoy

    # Actual answer computed here
    return int(final)

# Main execution block
if __name__ == '__main__':
    # Irrelevant data structures
    system_log = ['init', 'ready', 'active', 'idle']
    transformed_log = transform_case(system_log, 'lower')

    # Fake sensor data (distractor)
    readings = {'cpu': 65, 'gpu': 70, 'ram': 80}
    limits = {'cpu': 90, 'gpu': 85, 'ram': 85}
    health = analyze_component_health(readings, limits)

    # Unused outlier filtering
    raw_metrics = [88, 92, 76, 95, 83, 105, 89, 94, 77]
    filtered_metrics = filter_outliers(raw_metrics, 2.0)

    # Checksum red herring
    stream = [23, 45, 67, 89, 12]
    chksum = compute_checksum(stream)

    # Core input data
    metrics = [85, 90, 78, 93, 88, 91, 84, 87, 79, 92]
    benchmark_weights = [0.1, 0.15, 0.1, 0.2, 0.05, 0.15, 0.1, 0.05, 0.03, 0.02]

    # Key statement
    final_score = evaluate_performance(metrics, benchmark_weights)

    # Output target result
    print(f"Target result: {final_score}")