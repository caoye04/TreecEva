def analyze_growth_potential(soil_data, temp_seq):
    growth_index = 0
    adjustment_factor = 0.85
    for i, (moisture, ph) in enumerate(soil_data):
        if moisture < 30 or ph < 5.5:
            continue
        trend_score = sum(1 for t in temp_seq if t > 25)
        growth_index += (moisture * 0.3 + ph * 2.1) * (trend_score / len(temp_seq))
    return growth_index

soil_conditions = [(45, 6.2), (20, 6.0), (60, 6.8), (35, 5.3)]
temperatures = [22, 24, 26, 28, 27, 25, 23]
baseline_growth = analyze_growth_potential(soil_conditions, temperatures)

# Irrelevant auxiliary calculation (distractor)
noise_level = sum(t ** 0.5 for t in temperatures if t % 2 == 0)
reference_metric = noise_level * 1.7

# Key data structures
plots = [
    {'id': 'A1', 'size': 120, 'crop_type': 'wheat', 'yield_last': 98},
    {'id': 'B2', 'size': 85,  'crop_type': 'barley', 'yield_last': 75},
    {'id': 'C3', 'size': 150, 'crop_type': 'wheat', 'yield_last': 110}
]

weather_factors = [0.92, 0.78, 0.88, 0.95, 0.72]

# Lambda for seasonal adjustment
season_adj = lambda x: x * 1.1 if x > 0.8 else x * 0.9

# Distractor loop with zip and enumerate (semi-relevant)
monitoring_logs = []
for idx, (plot, wf) in enumerate(zip(plots, weather_factors * 2)):
    if idx >= len(plots): break
    status_flag = 'optimal' if wf > 0.8 else 'suboptimal'
    log_entry = f'{plot["id"]}:{status_flag}'
    monitoring_logs.append(log_entry)

# Real processing begins
adjustment_map = {p['id']: season_adj(wf) for p, wf in zip(plots, weather_factors)}

# Core efficiency calculation
size_weights = [p['size'] / 100 for p in plots]
scaled_yields = [p['yield_last'] * adjustment_map[p['id']] for p in plots]

# Secondary distractor: unused helper function
unused_helper = lambda a, b: (a + b) / 2 if a > b else (b - a) * 1.5

# Simulated pest impact (not actually used but looks important)
pest_pressure = 0
for w in weather_factors:
    if w < 0.75:
        pest_pressure += 10

# Actual key computation
weighted_efficiency = sum(
    size_weights[i] * scaled_yields[i] * (1 + baseline_growth / 100)
    for i in range(len(plots))
)

# Final yield calculation
final_yield = int(weighted_efficiency * 0.89)

# Output result
print(f"Result: {final_yield}")