import itertools

def collect_sensor_metrics(raw_streams):
    aggregated = []
    for stream in raw_streams:
        temp_series = [x * 0.85 + 12.7 for x in stream if x > 0]
        if len(temp_series) > 5:
            aggregated.extend(temp_series[::2])
    return aggregated

def validate_checksum(data):
    # Irrelevant validation function (dead code path)
    checksum = sum(d % 11 for d in data if d > 0) * 3
    return checksum < 1000

def analyze_trend(sequence):
    if len(sequence) < 3:
        return 0
    trend_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_score += 1
        elif sequence[i] < sequence[i-1]:
            trend_score -= 1
    return trend_score

def filter_anomalies(dataset, lower_bound=-50, upper_bound=200):
    cleaned = [x for x in dataset if lower_bound <= x <= upper_bound]
    outlier_count = len(dataset) - len(cleaned)
    # Misleading intermediate: looks important but unused later
    stability_flag = outlier_count < 5
    return cleaned

def generate_reference_grid():
    # Distractor function: creates a grid but it's not used
    return [[i*j for j in range(5)] for i in range(5)]

def build_threshold_map(tags):
    base_levels = {'core': 65.0, 'aux': 45.0, 'edge': 30.0}
    dynamic_offsets = {t: len(t) * 0.5 for t in tags}
    return {k: base_levels[k] + dynamic_offsets.get(k, 0) for k in base_levels}

def compute_entropy(values):
    # Dead computation with no impact on result
    if not values:
        return 0.0
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    from math import log2
    total = len(values)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 3)

def process_readings(readings, config_map):
    segment_a = readings[:len(readings)//2]
    segment_b = readings[len(readings)//2:]
    
    # Use of enumerate and zip
    indexed_b = list(enumerate(segment_b, start=len(segment_a)))
    paired = list(zip(segment_a, segment_b[:len(segment_a)]))
    
    # Set operation to remove duplicates in a non-trivial way
    unique_pairs = set(paired)
    flattened_unique = [val for pair in unique_pairs for val in pair]
    
    # Real computation path
    baseline = config_map['core']
    deviation_scores = [abs(x - baseline) for x in flattened_unique]
    
    # Use of itertools: group consecutive similar deviations
    grouped = []
    for key, group in itertools.groupby(deviation_scores, key=lambda x: x > baseline * 0.4):
        grouped.append((key, len(list(group))))
    
    adjustment_factor = sum(score * 0.1 for score in deviation_scores if score > 10)
    
    # Final diagnostic logic
    trend = analyze_trend(flattened_unique)
    adjustment_factor *= (trend + 5)
    final_value = int(baseline + adjustment_factor)
    
    # Irrelevant variables (red herrings)
    debug_snapshot = {
        'size': len(flattened_unique),
        'max_dev': max(deviation_scores, default=0),
        'groups': len(grouped)
    }
    
    # This is the actual answer variable
    final_diagnostic = final_value
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Simulated sensor input streams
    raw_input_data = [
        [105, -5, 80, 120, 110, 90, 200, 150],
        [70, 85, 95, 100, 102, 101, 99],
        [-10, -20, 60, 75, 85, 90, 95, 100, 110, 120]
    ]

    # Step 1: Collect metrics
    all_readings = collect_sensor_metrics(raw_input_data)
    
    # Step 2: Filter anomalies
    filtered_data = filter_anomalies(all_readings, lower_bound=0, upper_bound=130)
    
    # Step 3: Build configuration map
    sensor_tags = ['core', 'auxiliary', 'edge_node']
    threshold_map = build_threshold_map(sensor_tags)
    
    # Step 4: Validate (unused result)
    is_valid = validate_checksum([int(x) for x in filtered_data])
    
    # Step 5: Compute entropy (distraction)
    entropy_metric = compute_entropy(filtered_data)
    
    # Step 6: Generate unused grid
    reference_grid = generate_reference_grid()
    
    # Key statement: process readings to get final diagnostic
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")