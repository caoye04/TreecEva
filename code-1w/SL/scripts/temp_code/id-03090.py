def analyze_efficiency(records):
    total = 0
    count = 0
    for r in records:
        if r > 0:
            total += r ** 0.5
            count += 1
    return total / count if count else 0

# System capacity data in MW
base_capacities = [120, 150, 135, 167, 142, 189, 134, 178]

# Simulated usage log over 8 hours (in MW)
usage_log = [110, 145, 120, 160, 130, 170, 125, 170]

# Irrelevant historical efficiency metrics (distraction)
historical_efficiency = [0.88, 0.91, 0.85, 0.93, 0.87, 0.89, 0.90, 0.86]
efficiency_score = analyze_efficiency(historical_efficiency)

# Current load analysis
overload_count = 0
margin_sum = 0.0
for i in range(len(base_capacities)):
    margin = base_capacities[i] - usage_log[i]
    margin_sum += margin
    if usage_log[i] > base_capacities[i]:
        overload_count += 1

# Projected capacity expansion (not used in final result)
projected_growth = [c * 1.15 for c in base_capacities]

# Calculate effective remaining capacity per unit
available = [base_capacities[i] - usage_log[i] for i in range(len(base_capacities)) if usage_log[i] < base_capacities[i]]

# Filter out negative margins and compute average headroom
if available:
    avg_headroom = sum(available) / len(available)
else:
    avg_headroom = 0

# Key function combining arithmetic and filtering logic
def calculate_remaining(caps, log):
    surplus = [caps[i] - log[i] for i in range(len(caps))]
    filtered = [s for s in surplus if s > 5]  # Only meaningful surpluses
    return sum(filtered) * 0.9  # 10% safety margin applied

# Misleading intermediate calculation (dead computation)
total_utilization = sum(usage_log) / sum(base_capacities)

# Critical execution point
final_capacity = calculate_remaining(base_capacities, usage_log)

# Output result as required
print(f"Result: {final_capacity}")