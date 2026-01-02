from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation
def analyze_sensor_network(raw_streams, config_params):
    aggregate_metrics = []
    temp_registry = defaultdict(float)
    event_counter = Counter()

    for stream_name, readings in raw_streams.items():
        if not readings or len(readings) < 3:
            continue

        # Irrelevant preprocessing: normalizing timestamps (unused later)
        normalized_times = [t % 3600 for t in range(len(readings))]
        weight_mask = [0.8, 1.0, 0.9][:len(readings)]

        weighted_sum = sum(readings[i] * weight_mask[i % len(weight_mask)] for i in range(len(readings)))
        base_average = weighted_sum / len(readings)

        # Real logic: detect anomalies above dynamic threshold
        threshold_factor = config_params.get('sensitivity', 1.5)
        deviation = abs(max(readings) - min(readings))

        if deviation > threshold_factor * 15:
            event_counter['anomaly'] += 1
            adjustment = (base_average * 0.1) if deviation > 25 else (base_average * 0.05)
            temp_registry[stream_name] = base_average - adjustment
        else:
            event_counter['stable'] += 1
            temp_registry[stream_name] = base_average + 0.02

    # DEAD CODE PATH: Unused transformation branch
    def transform_legacy(data):
        return [x * 1.05 for x in data if x > 0]

    scaling_buffer = [temp_registry[k] * 1.1 for k in temp_registry if 'calib' in k]

    # Distractor: complex but irrelevant entropy calculation
    flat_values = [v for v in temp_registry.values()]
    entropy = 0.0
    total = sum(flat_values)
    if total > 0:
        from math import log
        entropy = -sum((v / total) * log(v / total) for v in flat_values if v > 0)

    # Real filtering logic disguised among noise
    filtered_registry = {k: v for k, v in temp_registry.items() if 'faulty' not in k and v > 0.5}

    return filtered_registry, dict(event_counter), entropy


def process_readings(data_map, thresholds):
    result_stack = []
    status_flags = set()
    rolling_cache = []

    # Nested control flow with mixed operations
    for key, val in data_map.items():
        key_prefix = key[:3]
        key_suffix = key[-1]

        # Bit manipulation red herring
        masked_key = sum(ord(c) << (i % 4) for i, c in enumerate(key)) & 0xFF

        if key_prefix in ['sen', 'dev']:
            # Real computation path
            base_score = val * 100
            
            # Conditional modification using slicing
            history_snippet = rolling_cache[-2:] if len(rolling_cache) >= 2 else [0, 0]
            
            if base_score > thresholds.get('critical', 75):
                adjusted_score = base_score * 0.85
                status_flags.add('high_load')
            elif base_score > thresholds.get('warning', 50):
                adjusted_score = base_score * 0.95 + history_snippet[-1] * 0.1
                status_flags.add('moderate')
            else:
                adjusted_score = base_score * 1.05
                status_flags.add('optimal')

            result_stack.append(adjusted_score)
            
            # Decoy: character counting in key (irrelevant)
            vowel_count = sum(1 for c in key if c.lower() in 'aeiou')
            case_ratio = sum(1 for c in key if c.isupper()) / len(key)

        # DEAD BRANCH: never executed due to prefix constraints
        if key_prefix == 'dbg':
            result_stack.append(-999)

    # Final aggregation with set operation distraction
    unique_floor = {int(x) for x in result_stack}
    overlap_check = unique_floor & {1, 2, 3, 4, 5}

    final_value = sum(result_stack) / len(result_stack) if result_stack else 0
    
    # Critical distractor: unused recursive function
    def recurse_diagnostics(level, acc):
        if level <= 0:
            return acc
        return recurse_diagnostics(level - 1, acc + [level * 2])

    return round(final_value, 4)

# Main execution flow
if __name__ == '__main__':
    # Input data setup
    sensor_inputs = {
        'sensor_a1': [23.5, 24.1, 22.9, 25.3],
        'sensor_b2': [45.6, 46.2, 44.8, 47.1, 46.5],
        'dev_unit_x': [30.1, 31.3, 29.9],
        'calib_ref_3': [10.0, 10.2],  # will be excluded due to length
        'faulty_node': [50.0, 52.0, 49.0]  # will be filtered later
    }

    config_settings = {
        'sensitivity': 1.8,
        'sample_rate': 1000,
        'timeout': 30
    }

    threshold_levels = {
        'warning': 50,
        'critical': 75
    }

    # Execute analysis pipeline
    cleaned_data, events, info_entropy = analyze_sensor_network(sensor_inputs, config_settings)
    
    # Key statement containing target variable
    final_diagnostic = process_readings(cleaned_data, threshold_levels)
    
    print(f"Result: {final_diagnostic}")