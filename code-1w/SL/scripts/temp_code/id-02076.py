from collections import defaultdict, Counter

# Simulated system metrics over time
timestamped_metrics = [
    {'time': 1, 'cpu': 75, 'mem': 80, 'disk': 30, 'net_in': 200, 'net_out': 180},
    {'time': 2, 'cpu': 80, 'mem': 82, 'disk': 35, 'net_in': 210, 'net_out': 190},
    {'time': 3, 'cpu': 95, 'mem': 90, 'disk': 40, 'net_in': 220, 'net_out': 200},
    {'time': 4, 'cpu': 65, 'mem': 70, 'disk': 50, 'net_in': 230, 'net_out': 210},
    {'time': 5, 'cpu': 70, 'mem': 75, 'disk': 55, 'net_in': 240, 'net_out': 220}
]

# Irrelevant auxiliary function (decoy)
def analyze_network_patterns(metrics):
    total_in = sum(m['net_in'] for m in metrics)
    total_out = sum(m['net_out'] for m in metrics)
    avg_in = total_in / len(metrics)
    avg_out = total_out / len(metrics)
    return (avg_in * avg_out) % 100

# Unused but plausible transformation
def normalize_values(data_list):
    normalized = []
    for entry in data_list:
        norm_entry = {k: v / 100.0 for k, v in entry.items() if isinstance(v, int)}
        normalized.append(norm_entry)
    return normalized

# Another red herring: detects 'spikes', not used in final calculation
def detect_spikes(metrics, threshold=85):
    spikes = defaultdict(int)
    for m in metrics:
        for k, v in m.items():
            if k in ['cpu', 'mem', 'disk'] and v > threshold:
                spikes[k] += 1
    return dict(spikes)

# Decoy metric aggregation (never called in main path)
def aggregate_by_time_window(metrics, window_size=2):
    windows = []
    for i in range(0, len(metrics), window_size):
        window = metrics[i:i+window_size]
        window_avg = {key: sum(d[key] for d in window) / len(window) 
                     for key in window[0].keys() if key != 'time'}
        windows.append(window_avg)
    return windows

# Core logic disguised among distractors
baseline_thresholds = {'cpu': 80, 'mem': 85, 'disk': 45}
penalty_weights = {'cpu': 1.5, 'mem': 2.0, 'disk': 1.2}

# Simulated benchmark reference patterns (mostly irrelevant)
benchmark_patterns = [
    [70, 80, 30], [75, 82, 35], [85, 88, 40], [60, 70, 50], [68, 74, 55]
]

# Pattern matcher that isn't actually used
def match_benchmark_fingerprint(patterns, current):
    flat_current = [current['cpu'], current['mem'], current['disk']]
    matches = 0
    for p in patterns:
        dist = sum(abs(a-b) for a,b in zip(p, flat_current))
        if dist < 5:
            matches += 1
    return matches

# Critical function buried in noise
def calculate_stability_index(metrics):
    stability = 0
    for i in range(1, len(metrics)):
        prev, curr = metrics[i-1], metrics[i]
        # Measure change in key resources
        cpu_delta = abs(curr['cpu'] - prev['cpu'])
        mem_delta = abs(curr['mem'] - prev['mem'])
        disk_delta = abs(curr['disk'] - prev['disk'])
        stability += (cpu_delta * 0.3 + mem_delta * 0.5 + disk_delta * 0.2)
    return 100 - (stability / (len(metrics) - 1)) if len(metrics) > 1 else 100

# Main evaluation logic with subtle dependencies
metric_set = ['cpu', 'mem', 'disk']
def evaluate_performance(keys, data):
    raw_scores = defaultdict(float)
    penalty_score = 0
    
    # Real scoring logic mixed with distractions
    for entry in data:
        for key in keys:
            if entry[key] > baseline_thresholds[key]:
                excess = entry[key] - baseline_thresholds[key]
                penalty_score += excess * penalty_weights[key]
    
    # Distractor: unused counter
    resource_counter = Counter(m['cpu'] // 10 * 10 for m in data)
    
    # Real stability component
    stability = calculate_stability_index(data)
    
    # Another decoy computation
    temporal_gaps = [data[i+1]['time'] - data[i]['time'] for i in range(len(data)-1)]
    uniform_timing = all(gap == 1 for gap in temporal_gaps)
    
    # Final score combines actual metrics
    base_performance = 100 - (penalty_score / len(data))
    final_adjustment = stability * 0.3 + base_performance * 0.7
    
    # Misleading normalization (not applied)
    if stability > 90:
        final_adjustment *= 1.05
    
    # The actual answer variable
    final_score = int(round(final_adjustment))
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = sum(resource_counter.values()) * 0.1
        final_score = max(final_score, int(fallback))
        
    return final_score

# Execute
final_score = evaluate_performance(metric_set, timestamped_metrics)
print(f"Target result: {final_score}")