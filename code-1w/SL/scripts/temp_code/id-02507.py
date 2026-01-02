from itertools import combinations

# Simulate daily energy consumption patterns for a microgrid over 7 days
daily_generation = [120, 135, 110, 150, 145, 130, 125]  # Solar/wind output per day
daily_loads = [95, 105, 115, 100, 120, 140, 135]       # Household demand per day

# Compute net surplus/deficit per day
net_daily_balance = [gen - load for gen, load in zip(daily_generation, daily_loads)]

# Simulate battery charge accumulation with 80% efficiency and 200-unit cap
current_charge = 0
battery_levels = []
for balance in net_daily_balance:
    if balance > 0:
        current_charge += balance * 0.8  # Store surplus at 80% efficiency
    else:
        discharge_needed = min(abs(balance), current_charge)
        current_charge -= discharge_needed
    current_charge = max(0, min(200, current_charge))  # Clamp within [0, 200]
    battery_levels.append(round(current_charge, 2))

# Distractor: Analyze rare extreme generation-load ratios
extreme_ratios = []
for g, l in zip(daily_generation, daily_loads):
    if l != 0 and g / l > 1.1:
        extreme_ratios.append(g / l)

# Compute rolling 3-day average load (distractor computation)
rolling_avg_load = []
for i in range(len(daily_loads) - 2):
    avg = sum(daily_loads[i:i+3]) / 3
    rolling_avg_load.append(round(avg, 2))

# Generate all possible 3-day usage windows and compute their total net impact
usage_windows = list(combinations(range(7), 3))
window_net_impacts = []
for window in usage_windows:
    total_impact = sum(net_daily_balance[i] for i in window)
    window_net_impacts.append(total_impact)

# Apply non-linear scaling to impacts based on system stress level (lambda function)
scale_stress = lambda x: x * 0.9 if x < 0 else x * 1.1
scaled_impacts = list(map(scale_stress, window_net_impacts))

# Simulate projected usage trajectory under scaled conditions
usage_trajectory = []
cumulative = 0
for impact in scaled_impacts:
    cumulative += impact * 0.7
    usage_trajectory.append(abs(cumulative))

# Introduce dead code path (never executed but looks relevant)
if False:
    fallback_estimate = sum(window_net_impacts) / len(window_net_impacts)
    smoothed = fallback_estimate * 0.95

# Critical statement
peak_capacity = max(usage_trajectory)

# Print result for evaluation
print(f"Result: {peak_capacity}")