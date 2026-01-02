from itertools import combinations

# System performance data for 6 components
timing_delays = [12, 7, 9, 4, 15, 3]
base_power = 50

# Calculate efficiency for every pair of components using combined delay and power penalty
efficiencies = []
for i, j in combinations(range(len(timing_delays)), 2):
    combined_delay = timing_delays[i] + timing_delays[j]
    power_penalty = abs(timing_delays[i] - timing_delays[j])
    efficiency = (base_power - power_penalty) / combined_delay
    efficiencies.append(round(efficiency, 3))

# Secondary metric: average stability across mid-range pairs
stability_scores = [efficiencies[i] * 0.9 for i in range(5, 10)]
avg_stability = sum(stability_scores) / len(stability_scores)

# Irrelevant tracking variable (minimal distraction)
processed_pairs = len(efficiencies)

# Key statement
peak_efficiency = max(efficiencies)
print(f"Result: {peak_efficiency}")