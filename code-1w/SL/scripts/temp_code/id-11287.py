from collections import defaultdict, Counter

# Simulated sensor network data processing with red herrings
def analyze_sensor_network(raw_streams, config):
    aggregate_metrics = []
    temp_cache = {}
    debug_flags = [False] * len(raw_streams)
    normalization_factor = 0.87

    for idx, stream in enumerate(raw_streams):
        if len(stream) < 5:
            continue

        # Irrelevant preprocessing branch (dead path)
        if config.get('legacy_mode', False):
            adjusted = [x * 1.05 for x in stream if x > 0]
            temp_cache[idx] = sum(adjusted) % 100

        # Real processing begins
        valid_readings = [x for x in stream if 10 <= x <= 90]
        if not valid_readings:
            debug_flags[idx] = True
            continue

        avg_reading = sum(valid_readings) / len(valid_readings)
        outlier_count = sum(1 for x in valid_readings if x > 75)

        # Distractor computation (unused later)
        entropy_proxy = 0
        freqs = Counter(valid_readings)
        for count in freqs.values():
            entropy_proxy -= (count / len(valid_readings)) * (count / len(valid_readings))

        # Meaningful metric collection
        aggregate_metrics.append({
            'node': idx,
            'avg': avg_reading,
            'outliers': outlier_count,
            'weight': len(valid_readings)
        })

    return aggregate_metrics


def calculate_thresholds(metrics_list):
    # Complex but mostly irrelevant threshold calculation
    if not metrics_list:
        return {'high_risk': 80, 'caution': 60}

    total_avg = sum(m['avg'] for m in metrics_list)
    total_weight = sum(m['weight'] for m in metrics_list)
    global_avg = total_avg / len(metrics_list)

    # Decoy statistical measures
    squared_dev = sum((m['avg'] - global_avg) ** 2 for m in metrics_list)
    variance_proxy = squared_dev / len(metrics_list) if metrics_list else 0

    # Actual thresholds used later
    return {
        'high_risk': int(global_avg + 12),
        'caution': int(global_avg + 5)
    }


def filter_critical_nodes(nodes, thresholds):
    # Another layer of filtering with distractions
    flagged_nodes = []
    audit_log = []
    cumulative_score = 0

    for node in nodes:
        score = 0
        if node['avg'] > thresholds['high_risk']:
            score += 3
        elif node['avg'] > thresholds['caution']:
            score += 1

        # Irrelevant scoring branch
        if node['outliers'] > 5:
            score += 0.5  # This does nothing due to integer conversion below

        final_score = int(score)
        cumulative_score += final_score

        if final_score > 0:
            audit_log.append(f"Node {node['node']}: {final_score}")
            flagged_nodes.append(node)

    # Unused summary statistic
    avg_cumulative = cumulative_score / len(nodes) if nodes else 0

    return flagged_nodes


def process_readings(flagged, threshold_map):
    # Core logic hidden among distractors
    readings_snapshot = []
    temp_series = []
    compression_key = 2

    for item in flagged:
        # Real transformation
        normalized_val = item['avg'] * 0.95
        adjusted_outliers = item['outliers'] + 1

        # Red herring: complex bit manipulation
        encoded = 0
        for i, b in enumerate(bin(item['node'])[-4:]) :
            encoded += int(b) << (3 - i)
        transformed = (encoded ^ 7) & 15

        # Actual accumulation
        contribution = int(normalized_val) // adjusted_outliers
        readings_snapshot.append(contribution)

        # Dead path: builds list but never used
        if transformed > 5:
            temp_series.append(normalized_val * 1.1)

    # Final computation
    base_sum = sum(readings_snapshot)
    modifier = len(temp_series) - len(readings_snapshot)  # Usually negative

    # Key result built from non-obvious components
    diagnostic_value = base_sum + modifier * 3

    # Multiple similar variables to confuse
    preliminary_diagnostic = base_sum * 0.9
    intermediate_diagnostic = base_sum + len(flagged)
    final_diagnostic = diagnostic_value  # This is the real one

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


# --- Main Execution with Distractors ---
if __name__ == "__main__":
    # Input data
    sensor_data = [
        [85, 88, 92, 103, 76, 81, 15],
        [45, 52, 58, 61, 67, 49, 55],
        [78, 83, 85, 89, 91, 77],
        [20, 25, 30, 35, 40],
        [88, 90, 92, 87, 85, 84, 86]
    ]

    system_config = {
        'sampling_rate': 100,
        'legacy_mode': True,
        'debug_trace': False
    }

    # Irrelevant precomputations
    flat_data = [x for seq in sensor_data for x in seq]
    mode_approx = max(set(flat_data), key=flat_data.count)
    data_range = max(flat_data) - min(flat_data)

    # Chain of processing steps
    processed_metrics = analyze_sensor_network(sensor_data, system_config)
    threshold_map = calculate_thresholds(processed_metrics)
    filtered_data = filter_critical_nodes(processed_metrics, threshold_map)
    
    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
