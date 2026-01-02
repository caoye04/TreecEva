from collections import defaultdict, Counter
import itertools

# Simulated network node performance metrics over time
node_data = [
    {'node': 'A', 'pings': [95, 102, 98, 97], 'load': 0.45, 'active': True},
    {'node': 'B', 'pings': [110, 115, 108, 120], 'load': 0.78, 'active': True},
    {'node': 'C', 'pings': [89, 90, 92, 87], 'load': 0.33, 'active': False},
    {'node': 'D', 'pings': [150, 160, 155, 158], 'load': 0.91, 'active': True},
    {'node': 'E', 'pings': [93, 94, 96, 92], 'load': 0.52, 'active': True}
]

# Irrelevant function: calculates node name length entropy (dead path)
def calculate_name_entropy(nodes):
    from math import log
    freq = defaultdict(int)
    total = 0
    for node in nodes:
        nlen = len(node['node'])
        freq[nlen] += 1
        total += 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Unused helper: analyzes ping variance (misleading intermediate)
def analyze_variance(ping_lists):
    variances = []
    for pings in ping_lists:
        mean = sum(pings) / len(pings)
        var = sum((x - mean) ** 2 for x in pings) / len(pings)
        variances.append(var)
    return [round(v, 2) for v in variances]

# Real logic begins: extract active nodes with acceptable latency
def filter_stable_nodes(data, max_ping=110):
    stable = []
    for entry in data:
        if not entry['active']:
            continue
        avg_ping = sum(entry['pings']) / len(entry['pings'])
        if avg_ping <= max_ping:
            stable.append({'node': entry['node'], 'avg': avg_ping, 'load': entry['load']})
    return stable

# Transform into nested structure for complex processing
def build_nested_metrics(nodes):
    metrics = defaultdict(lambda: defaultdict(list))
    for node in nodes:
        load_bin = 'high' if node['load'] > 0.5 else 'low'
        first_letter = node['node'][0]
        metrics[load_bin][first_letter].append(node['avg'])
    
    # Add artificial depth with irrelevant categorization
    for lb in metrics:
        for fl in metrics[lb]:
            metrics[lb][fl].sort()
            # Dead computation: smoothed values never used
            smoothed = [metrics[lb][fl][0]]
            for i in range(1, len(metrics[lb][fl])):
                smoothed.append((smoothed[-1] + metrics[lb][fl][i]) / 2)
            metrics[lb][fl] = {
                'raw': metrics[lb][fl],
                'count': len(metrics[lb][fl]),
                'smoothed_avg': sum(smoothed) / len(smoothed) if smoothed else 0,
                'placeholder_flag': True
            }
    return metrics

# Core optimization algorithm with distractors
def optimize_bandwidth(nested_metrics, threshold):
    bandwidth = 1000.0
    adjustments = []
    
    # Real contribution: count qualifying node groups
    valid_groups = 0
    total_load_weight = 0.0
    
    # Misleading loop 1: iterates but collects unused stats
    decoy_stats = []
    for load_type, letters in nested_metrics.items():
        letter_count = 0
        for letter, data in letters.items():
            if data['count'] >= 2:
                letter_count += 1
            # Fake correlation metric
            if data['count'] > 0:
                raw_avg = sum(data['raw']) / len(data['raw'])
                decoy_stats.append(raw_avg * 0.1 if load_type == 'high' else raw_avg * 0.05)
        adjustments.append(letter_count * 0.5)
    
    # Misleading loop 2: processes combinations but only some matter
    all_combinations = list(itertools.combinations(nested_metrics['low'], 2))
    combo_score = 0
    for c in all_combinations:
        combo_score += ord(c[0]) + ord(c[1])
    
    # Real logic: process high-load nodes meeting threshold criteria
    high_load_data = nested_metrics.get('high', {})
    low_load_data = nested_metrics.get('low', {})
    
    # Key calculation: only high-load nodes with raw average above threshold contribute negatively
    for node_group in high_load_data.values():
        raw_values = node_group['raw']
        if raw_values:
            group_avg = sum(raw_values) / len(raw_values)
            if group_avg > threshold:
                bandwidth -= (group_avg - threshold) * 10
    
    # Additional real effect: low-load node count gives bonus
    num_low_groups = len([g for g in low_load_data.values() if g['count'] > 0])
    bandwidth += num_low_groups * 15.5
    
    # Irrelevant sorting of adjustment list
    adjustments.sort(reverse=True)
    
    # Final red herring: uses decoy_stats only to modify unused variable
    temp_shift = sum(decoy_stats) / len(decoy_stats) if decoy_stats else 0
    _ = temp_shift * 2  # Unused
    
    # Critical statement
    final_bandwidth = round(bandwidth, 4)
    
    # Print required output
    print(f"Result: {final_bandwidth}")
    return final_bandwidth

# Execution flow
if __name__ == "__main__":
    # Irrelevant preprocessing
    names = [d['node'] for d in node_data]
    name_counter = Counter(names)
    unique_first_letters = set(name[0] for name in names)
    
    # More distraction: unused Cartesian product
    letter_pings = [(l, d['pings']) for l, d in zip(names, node_data)]
    cross = list(itertools.product([2, 3], repeat=2))
    
    # Actual pipeline
    stable_nodes = filter_stable_nodes(node_data, max_ping=110)
    nested_metrics = build_nested_metrics(stable_nodes)
    threshold = 95.0
    final_bandwidth = optimize_bandwidth(nested_metrics, threshold)
