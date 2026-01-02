from collections import defaultdict, Counter

# Simulate sensor data aggregation across network nodes
def main():
    node_data = [
        ('A', [3, 5, 7, 2]), ('B', [8, 2, 6]), ('C', [1, 1, 1, 1]),
        ('D', [4, 4, 4, 4]), ('E', [9]), ('F', [5, 5])
    ]

    # Aggregate contributions per node
    contributions = defaultdict(float)
    raw_counts = Counter()
    temp_sums = {}
    for node, readings in node_data:
        valid_readings = [r for r in readings if r > 2]
        if len(valid_readings) == 0:
            contributions[node] = 0.5
        else:
            base_score = sum(valid_readings)
            penalty = len(readings) - len(valid_readings)
            contributions[node] = base_score - penalty * 0.5

        raw_counts[node] = len(readings)
        temp_sums[node] = sum(readings)

    # Irrelevant statistical tracking (distractor)
    avg_length = sum(len(r[1]) for r in node_data) / len(node_data)
    mode_length = max(set(len(r[1]) for r in node_data), key=lambda x: list(len(r[1]) for r in node_data).count(x))

    # Define dynamic thresholds based on node name length (semi-relevant)
    thresholds = {}
    for node in contributions:
        if len(node) == 1:
            thresholds[node] = 6.0
        else:
            thresholds[node] = 4.5

    # Misleading normalization pass (dead computation)
    normalized_contribs = {}
    total_base = sum(temp_sums.values())
    for k, v in contributions.items():
        normalized_contribs[k] = (v + 1) / (total_base + 0.1) * 100

    # Core logic: calculate net flow above threshold
    def calculate_net_flow(contribs, threshs):
        surplus = 0
        deficit = 0
        debug_stats = {'above': 0, 'below': 0}
        for node, value in contribs.items():
            if value >= threshs[node]:
                surplus += value
                debug_stats['above'] += 1
            else:
                deficit += value
                debug_stats['below'] += 1

        # Secondary adjustment based on character frequency in node IDs (irrelevant)
        all_chars = ''.join(contribs.keys())
        freq = Counter(all_chars)
        bonus = 0
        for char, cnt in freq.items():
            if cnt > 1:
                bonus += 0.1  # This doesn't affect final result

        return surplus - deficit  # Only this matters

    # Execution point of interest
    net_flow = calculate_net_flow(contributions, thresholds)

    # Extraneous post-processing (distractor)
    magnitude_class = ""    
    if abs(net_flow) < 5:
        magnitude_class = "low"
    elif abs(net_flow) < 15:
        magnitude_class = "medium"
    else:
        magnitude_class = "high"

    scaling_factor = 1.0
    for i in range(2):  # Artificial loop
        scaling_factor *= 1.0

    # Output the target result
    print(f"Result: {net_flow}")

if __name__ == '__main__':
    main()