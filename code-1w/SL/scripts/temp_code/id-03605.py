import itertools

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_cluster(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings if x > 0]
    outliers = [val for val in normalized if val < 0.1 or val > 0.9]
    filtered = [val for val in normalized if 0.1 <= val <= 0.9]

    # Irrelevant transformation: frequency domain mock (dead path)
    spectral_peak = sum(normalized[::2]) * 0.5  # Distractor

    # Health metric based on distribution entropy approximation
    entropy_approx = 0
    for i in range(1, len(filtered)):
        diff = abs(filtered[i] - filtered[i-1])
        entropy_approx += diff * (1 + i % 3)

    consistency_score = 1 / (1 + entropy_approx) if entropy_approx else 1.0

    # Secondary irrelevant score: variance-based (not used in final logic)
    mean_filtered = sum(filtered) / len(filtered) if filtered else 0
    variance_proxy = sum((x - mean_filtered)**2 for x in filtered) / len(filtered) if filtered else 0
    stability_index = 1 / (1 + variance_proxy)  # Red herring

    return consistency_score, len(outliers)


def evaluate_node_health(node_id, sensors_data):
    # Misleading pre-checks
    if not sensors_data:
        return 0.0

    # Composite metrics across sensor groups
    group_scores = []
    total_outliers = 0

    for idx, readings in enumerate(sensors_data):
        # Decoy logic: skip every third group (never actually affects final path)
        if idx % 3 == 0:
            dummy_score = sum(readings) % 7  # Unused
            continue  # Actually skipped, but distracts from real flow

        score, outliers = analyze_sensor_cluster(readings)
        group_scores.append(score * (0.8 + idx * 0.05))  # Weighted contribution
        total_outliers += outliers

    # Real path resumes: only even-indexed groups contribute (after skip)
    actual_groups = [g for i, g in enumerate(sensors_data) if i % 2 == 0 and i % 3 != 0]
    if not actual_groups:
        fallback = sum(len(r) for r in sensors_data) / 7.0
        return fallback

    base_composite = sum(group_scores)

    # Complex conditional override (short-circuit red herring)
    adjustment_factor = (len(actual_groups) > 3) and (total_outliers < 5) or (base_composite > 2.0)
    multiplier = 1.25 if adjustment_factor else 0.88

    # Bit manipulation decoy: node id scrambling
    scrambled = (node_id ^ 0xABC) & 0xFFFF
    checksum = (scrambled >> 8) ^ (scrambled & 0xFF)
    # Checksum never used — pure distraction

    return base_composite * multiplier


def aggregate_metrics(network_topology, diagnostic_mode=True):
    if diagnostic_mode:
        mode_offset = 0.17
    else:
        mode_offset = 0

    # Simulated multi-node deployment
    nodes_data = [
        [12.1, 14.3, 13.9, 15.2, 13.0, 14.1],
        [11.8, 12.0, 9.1, 13.4, 12.7],
        [16.5, 15.9, 16.7, 16.3, 15.8, 16.0, 16.2],
        [10.2, 8.9, 11.3, 10.7, 11.1, 10.5, 9.8, 10.0],
        [14.4, 14.6, 14.3, 14.5]
    ]

    # Irrelevant topology processing
    flat_topology = list(itertools.chain.from_iterable(
        [(a, b) for b in neighbors] for a, neighbors in network_topology.items()
    ))
    connection_count = len(flat_topology)
    density_score = connection_count / (len(network_topology) ** 2)  # Unused

    # Primary evaluation
    node_results = [
        evaluate_node_health(i + 1000, data) for i, data in enumerate(nodes_data)
    ]

    # Conditional expression with misleading default
    primary_diagnostic = (
        sum(node_results) / len(node_results)
        if all(nr > 0.5 for nr in node_results)
        else max(node_results) * 0.5
    )

    # Final computation chain
    adjustment_term = (primary_diagnostic ** 0.5) * 0.3
    intermediate = primary_diagnostic + adjustment_term + mode_offset

    # Key line: what is the value of final_diagnostic here?
    final_diagnostic = int(intermediate * 1000) / 1000.0  # Rounded to 3 decimals

    # Dead code branches below
    if final_diagnostic < 0:
        final_diagnostic = 0.0
    elif final_diagnostic > 100:
        scale_backup = sum(sum(row) for row in nodes_data) / 1000
        final_diagnostic = scale_backup  # Never reached

    return final_diagnostic

# Execution entry point
network_map = {
    101: [102, 103],
    102: [101, 104],
    103: [101, 104, 105],
    104: [102, 103, 105],
    105: [103, 104]
}

result = aggregate_metrics(network_map, diagnostic_mode=True)
print(f"Target result: {result}")