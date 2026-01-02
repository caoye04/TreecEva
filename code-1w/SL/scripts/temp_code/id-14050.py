from collections import defaultdict, Counter

# Simulated sensor data aggregation for a distributed system health monitor
def collect_diagnostics(nodes):
    raw_readings = defaultdict(list)
    temp_aggregates = []
    checksum = 0

    for node_id, readings in nodes.items():
        if len(readings) < 3:
            continue
        avg_temp = sum(readings) / len(readings)
        temp_aggregates.append(avg_temp)
        
        # Irrelevant checksum distraction
        for val in readings:
            checksum ^= int(val * 10) % 256

        raw_readings['temperature'].extend(readings)
        raw_readings['processed'].append(avg_temp > 75.0)

    return raw_readings, temp_aggregates, checksum

# Misleading auxiliary function (dead path)
def compute_stability_index(logs):
    if not logs:
        return 0.0
    total_variance = 0.0
    for entry in logs:
        total_variance += (entry.get('cpu', 0) - entry.get('mem', 0)) ** 2
    return total_variance / len(logs)

# Core processing with red herrings
def analyze_pattern(sequence):
    freq_map = Counter(sequence)
    pattern_score = 0
    noise_floor = 0.0

    for k, v in freq_map.items():
        if v > 2:
            pattern_score += k * v
        else:
            noise_floor += k / (v + 1)
    
    # Decoy calculation
    if pattern_score > 100:
        adjusted = pattern_score * 0.9
    else:
        adjusted = pattern_score * 1.1

    # Actual relevant output
    return pattern_score

# Main metric processor
def process_metrics(summary, threshold):
    base_value = 0
    adjustment_factor = 1.0

    # Real logic branch
    if 'temperature' in summary:
        high_temp_nodes = len([t for t in summary['temperature'] if t > threshold])
        if high_temp_nodes > 0:
            base_value += 42 * high_temp_nodes

    # Distractor: complex but unused logic
    safety_margin = 0
    for temp in summary.get('temperature', []):
        if temp < 50:
            safety_margin += 5
        elif temp < 70:
            safety_margin += 3
        else:
            safety_margin -= 2

    # Another irrelevant transformation
    temp_str = ''.join(map(str, map(int, summary.get('temperature', [])[:3])))
    split_parts = temp_str.split('5')
    combined = ''.join([p[::-1] for p in split_parts])

    # Real contribution to answer
    if len(combined) > 5:
        base_value += len(combined)

    # Final computation using correct path
    if base_value > 50:
        adjustment_factor = 0.85
    
    result = int(base_value * adjustment_factor)
    return result

# Orchestration with decoy data
if __name__ == '__main__':
    cluster_data = {
        'node_a': [68.5, 72.1, 76.3, 80.0],
        'node_b': [70.2, 71.8, 69.9],
        'node_c': [85.0, 87.3, 88.1, 90.2],
        'node_d': [45.0, 47.1],  # Skipped due to length < 3
    }

    # Unused log data (red herring)
    system_logs = [
        {'cpu': 80, 'mem': 60, 'disk': 30},
        {'cpu': 75, 'mem': 70, 'disk': 25},
        {'cpu': 90, 'mem': 85, 'disk': 40}
    ]

    readings, aggregates, chk = collect_diagnostics(cluster_data)
    
    # Irrelevant pattern analysis on meaningless data
    dummy_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    score = analyze_pattern(dummy_sequence)
    
    # This stability index is never used
    stability = compute_stability_index(system_logs)

    # Key data structure for final computation
    data_summary = readings
    activation_threshold = 75.0

    # Critical statement
    final_diagnostic = process_metrics(data_summary, activation_threshold)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")