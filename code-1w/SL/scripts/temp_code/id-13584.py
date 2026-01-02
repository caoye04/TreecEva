import itertools

def analyze_signal_strength(nodes):
    # Irrelevant function: analyzes signal but not used in final calculation
    total = 0
    for node in nodes:
        if node % 3 == 0:
            total += node * 0.7
        elif node % 5 == 0:
            total += node * 0.4
    return round(total, 2)


def filter_channels(channels):
    # Dead-end filtering logic with no impact on result
    valid = []
    for c in channels:
        if c > 10 and c % 2 == 0:
            valid.append(c ** 0.5)
    return [v for v in valid if v < 7]


def compute_latency(n, load_factor):
    # Misleading computation that simulates performance metrics
    base = 1.0
    for i in range(1, n + 1):
        base *= (1 + (load_factor / i))
    return int(base) % 100


def aggregate_throughput(groups, factor):
    # Core logic hidden among distractions
    raw_data = list(itertools.chain.from_iterable(groups))
    filtered = [x for x in raw_data if x % 4 == 2]  # Only values like 2, 6, 10, ...
    
    # Decoy transformation
    disguised_sum = sum(x ** 2 for x in raw_data if x < 15)
    disguised_sum -= sum(filtered) * 0.3  # Red herring operation
    
    # Actual throughput logic
    window_size = 3
    max_window = 0
    for i in range(len(filtered) - window_size + 1):
        window = filtered[i:i + window_size]
        if len(window) == window_size:
            product = 1
            for w in window:
                product *= w
            if product > max_window:
                max_window = product

    # Final adjustment using factor
    adjusted = max_window * factor
    
    # Distractor: unused branching
    if adjusted > 1000:
        adjusted = (adjusted // 100) * 97
    
    return int(adjusted)

# Main execution block
node_list = [12, 15, 18, 22, 26, 30, 34]
signal_result = analyze_signal_strength(node_list)  # Irrelevant call

channel_list = [5, 12, 16, 18, 20, 24]
filtered_channels = filter_channels(channel_list)  # Dead-end path

latency_score = compute_latency(6, 1.25)  # Misleading metric

# Critical data structure
network_groups = [
    [2, 6, 10],           # Contains 2,6,10 -> all %4==2
    [14, 18, 22, 26],     # 14, but 18%4=2? No -> only 14
    [30, 34, 38, 42]      # 30%4=2 → yes; 38%4=2 → yes; 42%4=2 → yes
]
efficiency_factor = 1.75

# Key statement
final_bandwidth = aggregate_throughput(network_groups, efficiency_factor)

# Print required output
print(f"Result: {final_bandwidth}")