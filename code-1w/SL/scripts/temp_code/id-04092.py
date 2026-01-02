def preprocess_signal(raw_values, filter_key):
    processed = []
    temp_offset = 0
    for val in raw_values:
        if val % 3 == 0:
            temp_offset += 2
        elif val % 5 == 0:
            temp_offset -= 1
        else:
            temp_offset += (val % 7)
        processed.append(val + temp_offset)
    return processed


def generate_lookup(base_seed):
    lookup = {}
    x = base_seed
    for i in range(1, 10):
        x = (x * i + 3) % 17
        lookup[i] = x * 2
    return lookup


def decode_sequence(seq, keymap):
    result = []
    for i, item in enumerate(seq):
        if i in keymap:
            result.append(item ^ keymap[i])
        else:
            result.append(item | 5)
    return result


def count_anomalies(data_stream):
    count = 0
    prev = data_stream[0]
    for curr in data_stream[1:]:
        if abs(curr - prev) > 15:
            count += 1
        prev = curr
    return count + len([x for x in data_stream if x < 0])


def aggregate_metrics(records):
    stats = {'total': 0, 'peaks': 0, 'baseline': 0}
    for r in records:
        stats['total'] += r
        if r > 40:
            stats['peaks'] += 1
    stats['baseline'] = stats['total'] // len(records) if records else 0
    return stats


def analyze_pattern(dataset, config):
    score = 0
    mode_flag = config.get('mode', 1)
    
    # Irrelevant helper function defined inside (dead code)
    def unused_helper(x):
        return (x ** 2 + 1) % 100
    
    # Distractor variables
    temp_cache = set()
    shadow_sum = 0
    for item in dataset:
        if item in temp_cache:
            continue
        temp_cache.add(item)
        shadow_sum += item % 11
    
    # Actual logic begins
    phase_value = 0
    for i, v in enumerate(dataset):
        if mode_flag == 1 and i % 2 == 0:
            phase_value += v // 3
        elif mode_flag == 2:
            phase_value += v % 5
    
    # More distractions
    decoy_dict = {k: v*3 for k, v in config.items()}
    decoy_dict['extra'] = sum(decoy_dict.values()) // 2
    
    # Core computation
    base_score = phase_value * config.get('multiplier', 1)
    penalty = len([x for x in dataset if x in config.get('penalty_zone', [])])
    adjustment = config.get('adjustment', 0)
    
    final_score = base_score - penalty + adjustment
    
    # Red herring: complex but unused bitwise chain
    magic_shift = 0
    for b in dataset[:3]:
        magic_shift ^= (b << 2) | (b >> 1)
    magic_shift &= 0xFFFF
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input signal data
    sensor_readings = [12, 18, 25, 7, 33, 41, 14, 8, 29]
    
    # Apply preprocessing with distraction
    filtered_data = preprocess_signal(sensor_readings, filter_key=3)
    
    # Generate irrelevant lookup (not used in critical path)
    dummy_lookup = generate_lookup(7)
    
    # Transform data using actual relevant function
    transformed_data = decode_sequence(filtered_data, {0: 6, 2: 4, 5: 9})
    
    # Count anomalies (distraction - not used later)
    anomaly_count = count_anomalies(transformed_data)
    
    # Aggregate metrics (another distraction)
    stats_summary = aggregate_metrics(transformed_data)
    
    # Build configuration map using dictionary operations
    threshold_map = {
        'mode': 1,
        'multiplier': 4,
        'adjustment': -8,
        'penalty_zone': {15, 16, 17, 38, 39, 40}
    }
    
    # Introduce distractor set operation
    unused_set_ops = set(transformed_data) - set(sensor_readings)
    extra_calc = len(unused_set_ops.intersection({x * 2 for x in range(10)}))
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")