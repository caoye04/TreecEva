def analyze_temperature_profile(temps):
    smoothed = []
    for i in range(1, len(temps) - 1):
        smoothed.append((temps[i-1] + temps[i] + temps[i+1]) / 3)
    return smoothed

experiment_data = [23.5, 24.1, 25.3, 26.0, 27.8, 28.2, 29.1, 30.0, 30.5, 31.2]

# Irrelevant transformation - distractor
baseline_shift = [t - 20 for t in experiment_data]
log_values = [round(t ** 0.5, 2) for t in baseline_shift]

# Smoothing temperature data (relevant preprocessing)
temperature_trend = analyze_temperature_profile(experiment_data)

# Simulate sensor error correction (partially relevant)
corrected_readings = [round(t * 0.98, 2) for t in temperature_trend]

# Control variables (distractors)
max_temp = max(experiment_data)
min_temp = min(experiment_data)
avg_temp = sum(experiment_data) / len(experiment_data)

# Thresholds for growth phases
thresholds = {
    'germination': 24.0,
    'growth': 26.5,
    'maturation': 29.0
}

# Growth phase tracker
phase_counts = {'germination': 0, 'growth': 0, 'maturation': 0}
daily_phases = []

for temp in corrected_readings:
    if temp >= thresholds['maturation']:
        daily_phases.append('maturation')
        phase_counts['maturation'] += 1
    elif temp >= thresholds['growth']:
        daily_phases.append('growth')
        phase_counts['growth'] += 1
    elif temp >= thresholds['germination']:
        daily_phases.append('germination')
        phase_counts['germination'] += 1
    else:
        daily_phases.append('inactive')

# Compute cumulative phase durations (some irrelevant accumulation)
durations = []
current = 1
for i in range(1, len(daily_phases)):
    if daily_phases[i] == daily_phases[i-1]:
        current += 1
    else:
        durations.append(current)
        current = 1
durations.append(current)

# Harvest yield model based on phase balance
def harvest_results(data, limits):
    total_days = len(data) - 2  # Due to smoothing
    maturation_ratio = phase_counts['maturation'] / total_days if total_days > 0 else 0
    growth_ratio = phase_counts['growth'] / total_days if total_days > 0 else 0
    germ_ratio = phase_counts['germination'] / total_days if total_days > 0 else 0
    
    # Weighted contribution model
    base_yield = 150
    yield_contribution = (
        base_yield * 0.3 * germ_ratio +
        base_yield * 0.5 * growth_ratio +
        base_yield * 0.7 * maturation_ratio
    )
    
    # Penalty for instability (calculated from duration variance)
    if len(durations) > 1:
        mean_duration = sum(durations) / len(durations)
        variance = sum((d - mean_duration) ** 2 for d in durations) / len(durations)
        instability_penalty = int(variance * 2)
    else:
        instability_penalty = 0
    
    final = int(yield_contribution) - instability_penalty
    
    # Distractor calculation (unused)
    hypothetical_max = base_yield * max(germ_ratio, growth_ratio, maturation_ratio)
    efficiency_index = round(final / base_yield, 3) if base_yield > 0 else 0
    
    return final

# Key computation step
final_yield = harvest_results(experiment_data, thresholds)

Result: {final_yield}