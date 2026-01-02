from itertools import combinations

# Simulate performance readings from a distributed computing cluster
node_loads = [23, 45, 67, 34, 56, 78, 89, 12]
response_times = [0.23, 0.47, 0.61, 0.34, 0.55, 0.72, 0.81, 0.19]

# Irrelevant baseline for comparison (distractor)
baseline_score = sum(node_loads) / len(node_loads)

# Calculate efficiency scores using non-linear weighting
weighted_scores = []
for i, load in enumerate(node_loads):
    score = (load / (response_times[i] + 0.1)) * 0.85
    weighted_scores.append(round(score, 3))

# Generate all possible pairs of nodes for redundancy analysis (semi-relevant)
pairwise_stability = []
for pair in combinations(weighted_scores, 2):
    stability = abs(pair[0] - pair[1])
    pairwise_stability.append(stability)

# Filter out unstable configurations below threshold
stable_configs = [s for s in pairwise_stability if s < 50]

# Compute rolling average of last 5 stable configurations (distractor)
if len(stable_configs) >= 5:
    recent_avg = sum(stable_configs[-5:]) / 5
else:
    recent_avg = sum(stable_configs) / len(stable_configs) if stable_configs else 0

# Core metric: efficiency derived from original weighted scores
normalized_efficiencies = [ws / max(weighted_scores) * 100 for ws in weighted_scores]

# Apply decay factor based on position in list (simulating latency impact)
efficiencies = []
for idx, eff in enumerate(normalized_efficiencies):
    decayed = eff * (0.95 ** idx)
    efficiencies.append(round(decayed, 3))

# Introduce auxiliary calculation (dead code path - distractor)
temp_analysis = []
for e in efficiencies:
    if e > 60:
        temp_analysis.append(e * 1.1)
    elif e > 40:
        temp_analysis.append(e * 0.9)

# Key statement
peak_efficiency = max(efficiencies)
print(f"Result: {peak_efficiency}")