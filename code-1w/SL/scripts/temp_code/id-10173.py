from itertools import combinations

def analyze_node_pairs(nodes):
    # Irrelevant analysis for distraction
    pair_sums = [sum(pair) for pair in combinations(nodes, 2)]
    avg_sum = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    return avg_sum

def compute_entropy(seq):
    # Dead function - not used in main logic
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

def calculate_stabilized_flux(node_list, factor):
    # Core logic begins
    base_levels = [n * 0.87 for n in node_list if n > 5]
    
    # Distractor: tracking unused stats
    max_level = max(base_levels) if base_levels else 0
    min_level = min(base_levels) if base_levels else 0
    level_range = max_level - min_level
    
    # Real computation
    adjusted = []
    for val in base_levels:
        temp = val * factor
        if temp < 10:
            temp += 2.5
        elif temp > 20:
            temp -= 3.7
        adjusted.append(temp)
    
    # Secondary adjustment
    smoothed = 0
    for i, a in enumerate(adjusted):
        if i % 2 == 0:
            smoothed += a * 1.1
        else:
            smoothed += a * 0.9
    
    # Final transformation
    stabilized = smoothed * 0.95
    return round(stabilized, 4)

# Main execution
energy_nodes = [3, 7, 12, 4, 9, 15]
calibration_factor = 1.3

# Irrelevant preprocessing
node_avg = sum(energy_nodes) / len(energy_nodes)
deviation_score = sum(abs(n - node_avg) for n in energy_nodes)

# Distraction: unused structure
node_pairs_analysis = analyze_node_pairs(energy_nodes)
entropy_estimate = compute_entropy([1, 2, 2, 3, 3, 3])

# Key statement
final_flux = calculate_stabilized_flux(energy_nodes, calibration_factor)

print(f"Result: {final_flux}")