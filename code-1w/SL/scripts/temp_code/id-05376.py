from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def collect_diagnostics():
    raw_readings = [
        (102, 'A', 'active'), (205, 'B', 'idle'), (180, 'A', 'active'),
        (97, 'C', 'active'), (300, 'B', 'fault'), (150, 'A', 'active'),
        (400, 'D', 'unknown'), (110, 'C', 'active'), (220, 'B', 'active'),
        (95, 'A', 'fault'), (160, 'C', 'active')
    ]

    # Irrelevant transformation: count status labels (decoy)
    status_count = defaultdict(int)
    for _, _, status in raw_readings:
        status_count[status] += 1

    # Misleading intermediate: normalize readings above 100 (not used later)
    normalized = [max(0, x - 100) for x, _, _ in raw_readings]

    # Decoy function: calculates average but not used
    def calculate_average(data):
        return sum(data) / len(data) if data else 0
    avg_normalized = calculate_average(normalized)  # Dead assignment

    # Key processing path begins here
    readings_by_node = defaultdict(list)
    for value, node, status in raw_readings:
        if status != 'fault':  # Filter out faulty status
            readings_by_node[node].append(value)

    # Compute baseline thresholds per node (mean of valid readings)
    threshold_map = {}
    for node, values in readings_by_node.items():
        if values:
            threshold_map[node] = sum(values) / len(values)

    # Introduce red herring: bit manipulation on node IDs (unused)
    magic_offsets = {}
    for node in readings_by_node:
        char_val = ord(node)
        magic_offsets[node] = (char_val << 2) ^ 15 & char_val  # Complex but irrelevant

    # Filter data: only high-variance nodes (variance > 1500)
    variance_filter = {}
    for node, values in readings_by_node.items():
        mean_val = threshold_map[node]
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)
        variance_filter[node] = variance > 1500

    # Only include nodes with high variance
    target_nodes = {k for k, v in variance_filter.items() if v}

    # Apply node filter to get filtered_data
    filtered_data = []
    for entry in raw_readings:
        value, node, status = entry
        if status != 'fault' and node in target_nodes:
            filtered_data.append((value, node))

    # Another distraction: build frequency map of first digits (unused)
    digit_counter = Counter()
    for val, _ in filtered_data:
        digit_counter[int(str(val)[0])] += 1
    dominant_digit = max(digit_counter, key=digit_counter.get)  # Not used

    # Core logic: process the filtered dataset
    def process_readings(data, thresholds):
        if not data:
            return 0
        # Extract values above their node's threshold
        boosted = []
        for value, node in data:
            if value > thresholds.get(node, 0):
                boosted.append(value)
        # Apply exponential weighting (key transformation)
        weighted = sum(v * 0.1 for v in boosted)
        # Secondary adjustment: add number of unique nodes in filtered data
        nodes_in_use = set(node for _, node in data)
        adjustment = len(nodes_in_use) * 5
        return int(weighted + adjustment)  # Final integer result

    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")

    # Dead code paths below
    def legacy_calibrate(x):
        return (x >> 1) | 25
    unused_signal = legacy_calibrate(200)

    temp_snapshot = [x for x, _ in raw_readings if x > 200]
    snapshot_mean = sum(temp_snapshot) / len(temp_snapshot) if temp_snapshot else 0

    return final_diagnostic

# Execute and output
collect_diagnostics()