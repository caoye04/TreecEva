from collections import defaultdict

# Simulate time-series network node congestion data
def generate_congestion_data():
    data = defaultdict(list)
    for t in range(6):
        data['node_a'].append(10 + t * 2)
        data['node_b'].append(15 - t * 3)
        data['node_c'].append(8 + t % 3)
    return data

def smooth_signal(values, factor=0.2):
    smoothed = [values[0]]
    for i in range(1, len(values)):
        smoothed.append(smoothed[-1] * (1 - factor) + values[i] * factor)
    return smoothed

def calculate_node_load(history):
    if len(history) == 1:
        return history[0]
    mid = len(history) // 2
    left = calculate_node_load(history[:mid])
    right = calculate_node_load(history[mid:])
    return left * 0.6 + right * 0.4

def calculate_network_load(congestion_levels):
    loads = {}
    for node, history in congestion_levels.items():
        filtered = smooth_signal(history)
        loads[node] = calculate_node_load(filtered)
    return sum(loads.values())

# Irrelevant helper: counts transitions above threshold (not used in final result)
def count_overload_transitions(timeseries, threshold=12):
    count = 0
    for i in range(1, len(timeseries)):
        if timeseries[i-1] <= threshold < timeseries[i]:
            count += 1
    return count

# Main execution
raw_data = generate_congestion_data()
processed = {k: smooth_signal(v) for k, v in raw_data.items()}
criticality_score = sum(processed['node_a']) * 0.1  # distractor variable
total_load = calculate_network_load(congestion_levels=raw_data)
print(f"Result: {total_load}")