def analyze_grid_stability(loads, thresholds):
    # Irrelevant analysis function (dead code path)
    stable_count = 0
    for idx, load in enumerate(loads):
        if load < thresholds[idx % len(thresholds)]:
            stable_count += 1
    return stable_count

# Simulate power grid load behavior over time
grid_loads = [120, 150, 130, 170, 160, 140, 180, 190]
efficiency_rates = [0.85, 0.90, 0.88, 0.87, 0.91, 0.89, 0.86, 0.92]

# Distractor variables: thermal limits and safety margins (not used in final calculation)
thermal_limits = [200, 195, 190, 185, 180, 175, 170, 165]
safety_margin = 0.93
maintenance_factor = 1.05

# Historical data for comparison (unused but plausible)
historical_peaks = {
    'spring': 165,
    'summer': 188,
    'autumn': 155,
    'winter': 175
}

# Red herring computation: average load with decay adjustment
decay_weights = [0.5 ** i for i in range(len(grid_loads))]
decay_adjusted_avg = sum(grid_loads[i] * decay_weights[i] for i in range(len(grid_loads)))

# Real logic begins: normalize loads by efficiency
normalized_loads = []
for i, (load, eff) in enumerate(zip(grid_loads, efficiency_rates)):
    adjusted = load / eff
    normalized_loads.append(adjusted)

# Calculate rolling 3-period maxima (distractor)
rolling_maxes = []
for i in range(2, len(normalized_loads)):
    rolling_maxes.append(max(normalized_loads[i-2:i+1]))

# Identify high-stress periods (comparison operations)
stress_periods = []
for val in normalized_loads:
    if val > 160:
        stress_periods.append(val)

# Core algorithm: find peak effective capacity
max_efficiency = max(efficiency_rates)
min_efficiency = min(efficiency_rates)
efficiency_ratio = max_efficiency / min_efficiency

# Actual key calculation
aggregate_stress = 0
for val in stress_periods:
    aggregate_stress += val ** 0.5  # root-based weighting

baseline_capacity = sum(grid_loads) / len(grid_loads)

# Complex composite formula with bit manipulation twist
bit_encoded = 0
for i, rate in enumerate(efficiency_rates):
    if rate > 0.88:
        bit_encoded |= (1 << i)  # bitwise shift accumulation

# Final peak capacity derived from combinatorics of valid pairs
valid_pairs = 0
n = len(stress_periods)
for i in range(n):
    for j in range(i + 1, n):
        if abs(stress_periods[i] - stress_periods[j]) < 10:
            valid_pairs += 1

# Key statement
peak_capacity = int(baseline_capacity + aggregate_stress - valid_pairs * 2 + (bit_encoded & 255))

# Print result
print(f"Result: {peak_capacity}")