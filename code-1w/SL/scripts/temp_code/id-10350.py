from itertools import combinations

# Simulate sensor readings from a power grid with noise filtering
voltage_readings = [220, 230, 215, 240, 235, 225, 210]
current_readings = [10, 12, 9, 14, 13, 11, 8]
noise_threshold = 5

efficiencies = []
raw_margins = []
phantom_loads = 0

for v, c in zip(voltage_readings, current_readings):
    apparent_power = v * c
    real_power = apparent_power * 0.85  # Power factor compensation
    loss_factor = 1.05 if real_power > 2500 else 1.02
    adjusted_power = real_power / loss_factor
    
    # Irrelevant calculation: simulate phantom load detection (dead code path)
    if adjusted_power < 2000:
        phantom_loads += 1
        buffer_zone = adjusted_power * 0.05
    else:
        buffer_zone = 0  # Unused variable

    efficiency = (real_power / apparent_power) * 100
    efficiencies.append(round(efficiency, 2))

    # Semi-relevant: track margin but not used in final logic
    margin = apparent_power - real_power
    raw_margins.append(margin)

# Distractor: unused combination analysis
pairwise_stress = [sum(pair) for pair in combinations(voltage_readings, 2)]
avg_stress = sum(pairwise_stress) / len(pairwise_stress) if pairwise_stress else 0

# Key computational step
normalization_bias = len([m for m in raw_margins if m > 30])
adjusted_efficiencies = [e - 0.5 for e in efficiencies if e > 84]  # Minor correction

# Critical statement
peak_efficiency = max(efficiencies)

# Print result for execution visibility
print(f"Result: {peak_efficiency}")