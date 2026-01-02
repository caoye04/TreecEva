from collections import defaultdict


def analyze_distribution(data):
    freq = defaultdict(int)
    total = 0
    for item in data:
        freq[item] += 1
        total += item
    average = total / len(data) if data else 0
    return freq, average


def monitor_system_load(load_history):
    peak = max(load_history, default=0)
    trough = min(load_history, default=0)
    volatility = peak - trough
    return volatility  # Not used in final result


def optimize_buffer(sizes, limit):
    adjusted = []
    temp_sum = 0
    
    for i, val in enumerate(sizes):
        if i % 2 == 0:
            adjusted.append(val * 1.5)
        else:
            adjusted.append(val * 0.8)
    
    # Misleading transformation
    squared_offsets = [((x - limit) ** 2) for x in sizes]
    offset_total = sum(squared_offsets)  # Distractor computation
    
    cumulative = 0
    for idx, (orig, adj) in enumerate(zip(sizes, adjusted)):
        if adj > limit * 1.2:
            cumulative += orig // 2
        elif adj < limit * 0.8:
            cumulative += orig
        else:
            cumulative += int(adj)
    
    # Dead code path (never reached due to logic above)
    if False:
        backup = sum(sizes) * 0.9
        cumulative = max(cumulative, backup)
    
    return int(cumulative * 0.95)

# Main execution
workload = [12, 15, 22, 8, 30, 5]
diagnostic_log = [0.4, 0.7, 0.5, 0.9, 0.3]

# Irrelevant preprocessing
freq_map, avg_val = analyze_distribution(workload)
system_volatility = monitor_system_load(diagnostic_log)

threshold = 18
capacities = [10, 20, 14, 16, 25, 9]

intermediate_metric = 0
for index, (a, b) in enumerate(zip(workload, capacities)):
    intermediate_metric += (a - b) ** 2

scaling_factor = 1.1
scaled_caps = [c * scaling_factor for c in capacities]  # Unused list

final_capacity = optimize_buffer(capacities, threshold)
print(f"Result: {final_capacity}")