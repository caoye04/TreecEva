from collections import defaultdict, Counter

# Simulated system telemetry processing with noise and red herrings
def process_timing_data(raw_intervals):
    if not raw_intervals:
        return [0]
    
    # Irrelevant transformation (dead path)
    inverted_map = {i: 1/v for i, v in enumerate(raw_intervals) if v > 0}
    
    # Real processing begins
    normalized = [x / sum(raw_intervals) for x in raw_intervals]
    thresholds = [0.1, 0.25, 0.5]
    bands = defaultdict(int)
    
    for val in normalized:
        for t in sorted(thresholds):
            if val < t:
                bands[f'below_{t}'] += 1
                break
        else:
            bands['above_0.5'] += 1
    
    # Distractor: unused complex structure
    stats_matrix = [[val * norm for norm in normalized] for val in raw_intervals]
    
    return [int(bands['below_0.25']), len(normalized)]

# Fake diagnostic tree (decoy function - never called)
def legacy_diagnostic_tree(data):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    root = Node(sum(data))
    for d in data[1:]:
        curr = root
        while True:
            if d < curr.val:
                if not curr.left:
                    curr.left = Node(d)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(d)
                    break
                curr = curr.right
    return root

# Red herring list processing
def analyze_flags(flag_seq):
    flag_counter = Counter(flag_seq)
    priority_flags = [k for k, v in flag_counter.items() if v >= 2]
    # Complex but unused bitwise analysis
    mask = 0
    for pf in priority_flags:
        mask ^= hash(pf) & 0xF
    return sorted(priority_flags), mask

# Real signal extraction with decoys embedded
def extract_sequence_signature(events):
    timestamps = [e[0] for e in events]
    codes = [e[1] for e in events]
    
    # Real logic: compute variance-like metric on inter-arrival times
    deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    mean_delta = sum(deltas) / len(deltas)
    fluctuation_score = sum((d - mean_delta) ** 2 for d in deltas) / len(deltas)
    
    # Distractor: irrelevant tuple unpacking
    event_pairs = list(zip(events, events[1:]))
    for (t1, c1), (t2, c2) in event_pairs:
        _ = (t2 - t1) * (hash(c1) % 7)
    
    return int(fluctuation_score * 10)

# Main aggregation with multiple concepts
def aggregate_metrics(log_entries, health_diagnostics):
    timing_analysis = []    
    diagnostic_weights = {'stable': 1, 'caution': 3, 'alert': 5, 'critical': 10}
    base_weight = diagnostic_weights[health_diagnostics.get('system_state', 'stable')]
    
    # Process each log segment
    for entry in log_entries:
        time_key = entry['timestamp']
        interval_data = entry['intervals']
        
        # Real processing step
        processed = process_timing_data(interval_data)
        signature = extract_sequence_signature(entry['events'])
        
        # Compute weighted contribution
        weight = base_weight + (time_key % 4)
        score = (processed[0] * weight) + (signature // 2)
        timing_analysis.append(score)
    
    # Aggregate with slicing distraction
    extended_analysis = timing_analysis + timing_analysis[::-1]  # mirroring - unused
    mid_slice = extended_analysis[len(timing_analysis)//2 : len(extended_analysis)//2 + 3]
    
    # Final computation
    raw_total = sum(timing_analysis)
    adjustment_factor = len([d for d in health_diagnostics['issues'] if d != 'network_jitter'])
    final_diagnostic = raw_total - (adjustment_factor * base_weight)
    
    # Dead code: complex enumeration with no effect
    for idx, (orig, mirror) in enumerate(zip(timing_analysis, extended_analysis[:len(timing_analysis)])):
        if idx % 2 == 0:
            _ = orig ^ mirror ^ (idx * 3)
    
    return final_diagnostic

# Simulated input data - DO NOT MODIFY
timing_log = [
    {
        'timestamp': 1205,
        'intervals': [120, 80, 200, 90],
        'events': [(1200, 'A'), (1280, 'B'), (1480, 'C'), (1570, 'D')]
    },
    {
        'timestamp': 1230,
        'intervals': [95, 210, 85],
        'events': [(1230, 'X'), (1325, 'Y'), (1535, 'Z')]
    }
]

diagnostics = {
    'system_state': 'alert',
    'issues': ['disk_slow', 'cpu_spike', 'network_jitter'],  # network_jitter should be ignored in count
    'uptime': 87430  # irrelevant field
}

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, diagnostics)
print(f"Target result: {final_diagnostic}")