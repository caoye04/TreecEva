from collections import defaultdict, Counter
import itertools

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_data():
    raw_readings = [
        (101, [23.4, 24.1, 22.9, 25.0, 23.6]),
        (102, [19.5, 20.1, 18.9, 20.5, 19.8]),
        (103, [31.2, 32.0, 30.8, 33.1, 31.5]),
        (104, [17.6, 18.3, 17.9, 18.0, 18.5])
    ]
    return raw_readings

def filter_outliers(readings, low=15.0, high=35.0):
    filtered = []
    for node_id, values in readings:
        valid = [v for v in values if low <= v <= high]
        filtered.append((node_id, valid))
    return filtered

def compute_rolling_avg(values, window=3):
    if len(values) < window:
        return [sum(values)/len(values)] if values else [0]
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def derive_trend_indicator(averages):
    if len(averages) < 2:
        return 0
    diffs = [averages[i+1] - averages[i] for i in range(len(averages)-1)]
    positive = sum(1 for d in diffs if d > 0)
    negative = sum(1 for d in diffs if d < 0)
    return 1 if positive > negative else (-1 if negative > positive else 0)

def generate_combinations(items):
    # Irrelevant distractor function: generates unused combinations
    combs = []
    for r in range(2, len(items)+1):
        combs.extend(itertools.combinations(items, r))
    return combs  # Never used in main logic

def count_frequency_patterns(seq):
    # Another red herring: analyzes patterns not used in final result
    freq = Counter()
    for i in range(len(seq)-1):
        pair = (seq[i], seq[i+1])
        freq[pair] += 1
    return freq  # Computed but irrelevant

def build_lookup_structure(data_list):
    # Creates a complex nested structure with decoy entries
    lookup = defaultdict(lambda: defaultdict(dict))
    for idx, (node_id, values) in enumerate(data_list):
        stats = {
            'raw_count': len(values),
            'valid_range': len([v for v in values if 18.0 <= v <= 32.0]),
            'extreme': len([v for v in values if v > 30.0])
        }
        lookup[node_id]['meta']['index'] = idx
        lookup[node_id]['meta']['source'] = 'sensor_net_v2'
        lookup[node_id]['diagnostics'].update(stats)
        # Decoy computations
        temp_set = set(f'{v:.1f}' for v in values)
        case_variants = [s.upper() for s in temp_set] + [s.lower() for s in temp_set]
        lookup[node_id]['flags']['cases'] = case_variants  # Unused
    return lookup  # Only partially used

def calculate_baseline_adjustment(nodes_data):
    all_vals = []
    for _, vals in nodes_data:
        all_vals.extend(vals)
    mean_val = sum(all_vals) / len(all_vals)
    adjustment = 0.0
    if mean_val > 25.0:
        adjustment = -1.5
    elif mean_val < 20.0:
        adjustment = 2.0
    return mean_val, adjustment

def analyze_readings(processed, thresholds):
    results = []
    trend_scores = []
    for node_id, data in processed:
        rolling = compute_rolling_avg(data)
        trend = derive_trend_indicator(rolling)
        trend_scores.append(trend)
        
        # Real computation path
        base = sum(data) / len(data)
        if base > thresholds.get(node_id, 0):
            status = 2
        elif base < thresholds.get(node_id, 0) * 0.9:
            status = -1
        else:
            status = 1
        results.append(status)
    
    # Final aggregation logic
    net_status = sum(results)
    trend_bias = sum(trend_scores)
    final_score = net_status * 3 + trend_bias * 2
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    raw_data = collect_sensor_data()
    
    # Step 2: Filter outliers (distractor: low/high bounds appear adjustable but are fixed)
    cleaned_data = filter_outliers(raw_data)
    
    # Step 3: Compute baseline adjustment (partially relevant)
    avg_temp, correction = calculate_baseline_adjustment(cleaned_data)
    
    # Step 4: Build complex lookup (mostly irrelevant, only node_ids matter)
    lookup_table = build_lookup_structure(cleaned_data)
    
    # Step 5: Extract and transform data for analysis
    processed_nodes = []
    for node_id, values in cleaned_data:
        adjusted = [v + correction for v in values]  # Apply real correction
        processed_nodes.append((node_id, adjusted))
    
    # Step 6: Generate unused combinatorial patterns (pure distraction)
    node_ids = [nid for nid, _ in cleaned_data]
    combinations = generate_combinations(node_ids)  # Dead code path
    pattern_freq = count_frequency_patterns(node_ids)  # More dead code
    
    # Step 7: Define actual threshold map (critical for final logic)
    threshold_config = {
        101: 23.5,
        102: 19.0,
        103: 31.0,
        104: 18.0
    }
    
    # Step 8: Execute key analysis (target statement)
    final_diagnostic = analyze_readings(processed_nodes, threshold_config)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")