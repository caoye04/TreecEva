def analyze_flow_sequence(sequence):
    total_flow = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            total_flow += val * (i + 1)
    return total_flow

# Simulate network traffic data
link_strengths = [3, 7, 2, 8, 5]
efficiency_rates = [0.9, 0.6, 0.8, 0.7, 0.5]

# Misleading intermediate: unused flow analysis
flow_sequence = [x * 2 for x in link_strengths if x > 4]
baseline_flow = analyze_flow_sequence(flow_sequence)

# Construct link matrix using zip and enumerate
link_matrix = []
for idx, (a, b) in enumerate(zip(link_strengths[:-1], link_strengths[1:])):
    multiplier = (idx + 1) / 2.0
    link_matrix.append((a + b) * multiplier)

# Create efficiency map with dictionary comprehension
efficiency_map = {i: rate ** 2 for i, rate in enumerate(efficiency_rates)}

# Dead code path - simulates error correction but not used
error_log = []
for i in range(len(link_strengths)):
    if i in efficiency_map and efficiency_map[i] < 0.6:
        error_log.append(f"Low efficiency at {i}")

# Real computation begins
aggregate_score = 0
for i, strength in enumerate(link_strengths):
    if i in efficiency_map:
        aggregate_score += strength * efficiency_map[i]

# Secondary distraction: unused combinatorics calculation
from math import comb
possible_paths = 0
for i in range(1, 4):
    possible_paths += comb(5, i)  # Irrelevant to final result

# Core logic: network capacity calculation
def calculate_network_capacity(links, eff_map):
    base = sum(links)
    factor = 0
    for i, link in enumerate(links):
        if i % 2 == 1:
            factor += eff_map.get(i, 0.5)
    return int(base * factor)

# Final computation
final_capacity = calculate_network_capacity(link_matrix, efficiency_map)
print(f"Target result: {final_capacity}")