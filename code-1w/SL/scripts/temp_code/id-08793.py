from collections import defaultdict

# Simulate a thermal processing system with stages and heat retention

def analyze_process_efficiency(stages):
    efficiency_map = defaultdict(float)
    total_time = sum(stage['duration'] for stage in stages)
    max_temp = max(stage['temperature'] for stage in stages)
    baseline_efficiency = 0.78

    # Irrelevant computation: simulate pressure buildup (not used in final result)
    pressure_buildup = 0
    for stage in stages:
        pressure_buildup += stage['duration'] * 0.34
        if pressure_buildup > 50:
            pressure_buildup *= 0.9

    # Semi-relevant: adjust efficiency based on temperature fluctuations
    temp_variance = sum(abs(stages[i]['temperature'] - stages[i+1]['temperature']) 
                        for i in range(len(stages)-1))
    adjusted_efficiency = baseline_efficiency - (temp_variance / 1000)

    for i, stage in enumerate(stages):
        efficiency_map[f'stage_{i}'] = adjusted_efficiency * (stage['temperature'] / max_temp)

    return efficiency_map


def calculate_thermal_capacity(stages):
    # Core logic: compute effective thermal capacity based on duration and temperature
    cumulative_exposure = 0
    decay_factor = 1.0

    # Misleading variable: energy_input appears relevant but isn't directly used
    energy_input = sum(stage['temperature'] * stage['duration'] for stage in stages) * 0.85

    # Real computation with state decay over stages
    for stage in stages:
        intensity = stage['temperature'] / 100.0
        duration_weight = stage['duration'] ** 0.5
        cumulative_exposure += intensity * duration_weight * decay_factor
        decay_factor *= 0.92  # Diminishing contribution over time

    # Additional distraction: normalize using unused pressure data
    normalization_proxy = len(stages) * 1.5
    if normalization_proxy > 10:
        normalization_proxy *= 0.1

    final_capacity = cumulative_exposure * 100
    return int(final_capacity)

# Define process stages in manufacturing pipeline
process_stages = [
    {'temperature': 220, 'duration': 15},
    {'temperature': 250, 'duration': 12},
    {'temperature': 180, 'duration': 8},
    {'temperature': 310, 'duration': 20},
    {'temperature': 290, 'duration': 18}
]

# Analyze efficiency (side computation that doesn't affect thermal capacity)
efficiency_analysis = analyze_process_efficiency(process_stages)

# Track auxiliary metrics (dead code path - never used)
metrics_log = []
for stage_idx, _ in enumerate(process_stages):
    metrics_log.append(f'log_{stage_idx}: complete')

# Key statement: compute thermal capacity
target_capacity = calculate_thermal_capacity(process_stages)
thermal_capacity = target_capacity

# Print final result as required
print(f"Result: {thermal_capacity}")