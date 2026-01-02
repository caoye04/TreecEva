from collections import defaultdict, Counter

# Simulated sensor network data with noise and redundant metrics
def collect_diagnostics():
    raw_readings = [
        (100, 'temp', 'node_A'), (205, 'voltage', 'node_B'), (300, 'temp', 'node_C'),
        (150, 'current', 'node_A'), (400, 'temp', 'node_B'), (99, 'temp', 'node_A'),
        (210, 'voltage', 'node_B'), (160, 'current', 'node_C'), (310, 'temp', 'node_C')
    ]

    # Irrelevant aggregation: counts per node (not used in final logic)
    node_counts = defaultdict(int)
    for _, metric, node in raw_readings:
        node_counts[node] += 1

    # Distractor: mapping unrelated to actual processing
    metric_scales = {'temp': 1.0, 'voltage': 0.5, 'current': 0.8}
    scaled = [val * metric_scales[typ] for val, typ, _ in raw_readings]

    # Actual relevant filtering: extract only 'temp' readings above 100
    temp_readings = [(val, node) for val, typ, node in raw_readings if typ == 'temp' and val > 100]

    # Dead code path: never called function
    def calibrate(x):
        return x * 1.05 + 10  # Misleading adjustment

    # Redundant transformation
    temp_dict = defaultdict(list)
    for val, node in temp_readings:
        temp_dict[node].append(val)

    # Further distractor: statistical overkill
    stats_summary = {}
    for node, vals in temp_dict.items():
        mean_val = sum(vals) / len(vals)
        variance = sum((x - mean_val) ** 2 for x in vals) / len(vals)
        stats_summary[node] = (mean_val, variance)

    # Key filtering step: only nodes with more than one reading
    filtered_nodes = {k for k, v in temp_dict.items() if len(v) > 1}
    filtered_data = [(v, n) for v, n in temp_readings if n in filtered_nodes]

    # Decoy structure
    baseline_shifts = {'node_A': -5, 'node_B': 3, 'node_C': 0}  # Unused

    # Threshold map actually used in processing
    threshold_map = {'node_A': 95, 'node_B': 390, 'node_C': 305}

    # Fake normalization
    normalized_log = [round((x - 100) / 10) for x in scaled]  # Irrelevant

    # Core logic hidden among distractions
    def process_readings(data, thresholds):
        alert_count = 0
        for value, node in data:
            # Only this condition matters
            if value > thresholds.get(node, 0):
                alert_count += 1
        # Another red herring
        if alert_count == 0:
            return sum(len(s) for s in temp_dict.keys())  # unreachable due to data
        # Real answer path
        checksum = 0
        for value, node in data:
            if node == 'node_B':
                checksum ^= value  # XOR into checksum
            else:
                checksum += value
        return checksum + alert_count

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Unrelated visualization prep
    frequency = Counter(normalized_log)
    distribution = sorted(frequency.items())

    # Output required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute
collect_diagnostics()