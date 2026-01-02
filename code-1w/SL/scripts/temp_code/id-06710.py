def analyze_soil_ph(readings):
    adjusted = [r + 0.3 for r in readings if r < 6.0]
    return sum(adjusted) / len(adjusted) if adjusted else 7.0

soil_samples = [5.8, 6.2, 5.9, 7.1, 6.3]
base_ph = analyze_soil_ph(soil_samples)

humidity_levels = {"morning": 88, "afternoon": 63, "night": 91}
peak_humidity = max(humidity_levels.values())

# Distractor: irrelevant weather score computation
temp_fluctuation = 4.5
weather_score = (peak_humidity * 0.7) + (temp_fluctuation * 2)
if weather_score > 70:
    stability_index = 3
else:
    stability_index = 1

area_metrics = [
    {"area": 120, "fertility": 8, "slope": 3},
    {"area": 95, "fertility": 6, "slope": 8},
    {"area": 140, "fertility": 9, "slope": 5}
]

growth_cycles = [
    [23, 25, 24, 22],
    [19, 20, 21, 18],
    [27, 26, 28, 25]
]

# Misleading intermediate calculation
effective_cycles = []
for cycle in growth_cycles:
    avg_cycle = sum(cycle) / len(cycle)
    if avg_cycle > 20:
        effective_cycles.append(avg_cycle * 1.1)
    else:
        effective_cycles.append(avg_cycle * 0.9)

# Core logic with distractors
slope_penalty = 0
for metric in area_metrics:
    if metric["slope"] > 6:
        slope_penalty += 0.15

base_fertility = sum(m["fertility"] for m in area_metrics) / len(area_metrics)
adjusted_fertility = base_fertility * (1 - slope_penalty)

# Simulate yield per area with conditional efficiency
yields = []
for i, metric in enumerate(area_metrics):
    base_yield = metric["area"] * adjusted_fertility
    cycle_efficiency = sum(growth_cycles[i]) / len(growth_cycles[i]) / 24.0
    # Use conditional expression and list comprehension
    modifier = 1.2 if cycle_efficiency >= 1.0 else 0.85
    adjusted_yield = base_yield * modifier
    yields.append(adjusted_yield)

# Final aggregation
aggregate_yield = sum(yields)
penalty_factor = 0.95 if base_ph < 6.0 else 1.0
final_yield = aggregate_yield * penalty_factor

# Irrelevant formatting path (dead code)
report_mode = "detailed"
output_format = "csv" if report_mode == "brief" else "json"

# Print final result as required
print(f"Result: {final_yield}")