from collections import defaultdict, Counter

# Simulated sensor data aggregation (distractor: some values are irrelevant)
def collect_telemetry():
    raw_readings = [15, 18, 23, 25, 30, 35, 40, 42, 45, 50]
    adjusted = [x * 1.05 for x in raw_readings if x > 20]
    return {f'sensor_{i}': v for i, v in enumerate(adjusted)}

def analyze_pattern(sequence):
    # Irrelevant pattern analysis (dead path)
    freq = Counter(sequence)
    mode = freq.most_common(1)[0][1]
    return [k for k, v in freq.items() if v == mode]

def generate_baseline(offset=10):
    # Unused baseline generator (red herring)
    return [i * 2 + offset for i in range(5)]

def filter_outliers(data_dict, limit=40.0):
    # Filters but also logs irrelevant stats
    clean = {}
    stats = defaultdict(int)
    for k, v in data_dict.items():
        if v < limit:
            clean[k] = round(v, 2)
        else:
            stats['discarded'] += 1
            stats['high_count'] += 1  # misleading stat
    temp_log = [v for v in data_dict.values() if v > 45]  # unused
    return clean

def compute_stability_index(values):
    # Complex but partially irrelevant computation
    diffs = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    variance = sum((d - avg_diff) ** 2 for d in diffs) / len(diffs) if diffs else 0
    fluctuation_penalty = 0
    for d in diffs:
        if d > avg_diff * 1.5:
            fluctuation_penalty += 0.5
    index = 100 - (avg_diff * 2) - fluctuation_penalty
    return max(index, 0)

def evaluate_consistency(records):
    # Another decoy function that computes but isn't used in final result
    total = 0
    count = 0
    for val in records.values():
        if val > 25:
            total += val ** 0.5
            count += 1
    return round(total / count, 2) if count else 0

def build_threshold_map(config_level=2):
    # Generates mapping used in real logic
    base = {'critical': 40.0, 'warning': 30.0}
    if config_level == 1:
        base['critical'] -= 5
    elif config_level == 2:
        base['critical'] += 2
        base['elevated'] = 36.0  # added for complexity
    return base

def extract_relevant_set(data, keys_hint=['sensor_2', 'sensor_3']):
    # Extracts subset — this is actually used
    return {k: v for k, v in data.items() if k in keys_hint or int(k.split('_')[1]) % 2 == 0}

def process_metrics(dataset, thresholds):
    # Core logic with distractions
    subset = extract_relevant_set(dataset)
    high_alerts = 0
    mid_alerts = 0
    for key, value in subset.items():
        idx = int(key.split('_')[1])
        if value > thresholds['critical']:
            high_alerts += 1
        elif value > thresholds.get('elevated', 34):  # uses optional level
            mid_alerts += 1
    # Real contribution to answer
    adjustment_factor = (high_alerts * 7) + (mid_alerts * 3)
    base_score = 50
    if high_alerts > 0:
        base_score -= adjustment_factor * 1.5
    else:
        base_score += 10 - mid_alerts
    # Distracting transformations
    temp_arr = [adjustment_factor * 2, base_score + 5]
    temp_sum = sum(temp_arr) / 2
    final_value = int(round(base_score))
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect telemetry
    telemetry_data = collect_telemetry()
    
    # Step 2: Generate unused pattern analysis (distraction)
    keys_list = list(telemetry_data.keys())
    patterns = analyze_pattern([int(k.split('_')[1]) for k in keys_list])
    
    # Step 3: Build actual threshold map
    threshold_map = build_threshold_map(config_level=2)
    
    # Step 4: Filter data (partially relevant)
    filtered_data = filter_outliers(telemetry_data, limit=42.0)
    
    # Step 5: Compute stability (unused but looks important)
    stability = compute_stability_index(list(filtered_data.values()))
    
    # Step 6: Evaluate consistency (dead end)
    consistency = evaluate_consistency(filtered_data)
    
    # Step 7: Process metrics using filtered and mapped data
    final_diagnostic = process_metrics(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")