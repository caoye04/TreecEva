from itertools import combinations

# System parameters for a distributed task scheduler simulation
task_counts = [12, 15, 8, 20, 10]
node_capacities = [16, 12, 18, 9, 14]
base_rating = 73

disruption_factor = 0.0
for i in range(len(task_counts)):
    if task_counts[i] > node_capacities[i]:
        excess = task_counts[i] - node_capacities[i]
        disruption_factor += excess * 0.1

# Simulate communication overhead between nodes
pairwise_stress = 0
for pair in combinations(node_capacities, 2):
    diff = abs(pair[0] - pair[1])
    if diff > 5:
        pairwise_stress += diff * 0.05

# Calculate load distribution efficiency
load_balance_ratio = sum(task_counts) / sum(node_capacities)
adjusted_balance = max(load_balance_ratio, 0.6) if load_balance_ratio < 0.8 else load_balance_ratio

# Misleading intermediate calculations (distractors)
theoretical_max_throughput = len(task_counts) * max(node_capacities)
utilization_penalty = 0
if theoretical_max_throughput > 100:
    utilization_penalty = 5

# Performance metrics influenced by multiple factors
performance_multiplier = 1.0
if adjusted_balance < 0.75:
    performance_multiplier *= 0.85
elif adjusted_balance < 0.9:
    performance_multiplier *= 0.95
else:
    performance_multiplier *= 1.05

if disruption_factor > 0.5:
    performance_multiplier *= 0.9

if pairwise_stress > 1.0:
    performance_multiplier *= 0.97

# Key statement: compute final efficiency score
efficiency_score = base_rating * performance_multiplier

# Irrelevant post-calculation (dead code path)
consistency_flags = []
for count in task_counts:
    if count % 4 == 0:
        consistency_flags.append(True)
    else:
        consistency_flags.append(False)

# Output result
print(f"Result: {efficiency_score}")