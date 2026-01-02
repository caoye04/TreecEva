from collections import defaultdict, Counter

# Simulate warehouse inventory optimization with misleading metrics
def analyze_redundancy(flow_map):
    redundant_links = 0
    for key in flow_map:
        if flow_map[key] < 5:
            redundant_links += 1
    return redundant_links

def calculate_entropy(seq):
    freqs = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
    return round(entropy, 4)

def simulate_buffer_levels(initial_level, operations):
    level = initial_level
    history = []
    for op in operations:
        if op > 0:
            level += op * 0.5
        else:
            level -= abs(op) * 0.3
        history.append(round(level, 2))
    return history  # Unused in final result

def optimize_distribution(inventory, demand_sequence):
    stock = defaultdict(int)
    for item, qty in inventory.items():
        stock[item] = qty * 1.0
    
    # Misleading preprocessing
    peak_demand = max(demand_sequence)
    avg_demand = sum(demand_sequence) / len(demand_sequence)
    smoothed_demand = [d * 1.1 for d in demand_sequence if d < avg_demand + 2]
    
    adjustment_factor = 0
    for i, d in enumerate(smoothed_demand):
        if i % 2 == 0:
            adjustment_factor += d * 0.05
        else:
            adjustment_factor -= d * 0.02
    
    # Core logic: compute capacity based on utilization ratio
    total_required = sum(demand_sequence)
    total_available = sum(stock.values())
    
    utilization = total_available / total_required if total_required > 0 else 0
    
    # Apply non-linear scaling based on system stress
    stress_factor = 0
    for d in demand_sequence:
        if d > peak_demand * 0.8:
            stress_factor += 1
    
    penalty = stress_factor * 0.15
    efficiency_score = utilization - penalty
    
    # Final capacity adjusted by efficiency and fake buffer metric
    buffer_metric = calculate_entropy(demand_sequence)
    raw_capacity = total_available * efficiency_score
    
    # Red herring: simulate buffer levels but don't use result
    _ = simulate_buffer_levels(100, demand_sequence)
    
    # Final adjustment using irrelevant but plausible term
    final_capacity = int(raw_capacity - adjustment_factor * 2 + buffer_metric * 10)
    
    return final_capacity

# Setup realistic data
inventory = {
    'A': 85,
    'B': 72,
    'C': 64,
    'D': 93
}

demand_sequence = [23, 15, 18, 27, 14, 20, 25, 16]

# Misleading auxiliary analysis
flow_network = {(i, i+1): val for i, val in enumerate(demand_sequence)}
decoy_analysis = analyze_redundancy(flow_network)

# Key execution point
final_capacity = optimize_distribution(inventory, demand_sequence)

print(f"Result: {final_capacity}")