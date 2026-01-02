from itertools import cycle

# Simulate agricultural yield optimization with environmental constraints
def normalize_readings(sensor_data):
    base_offset = 0.87
    adjusted = [reading * base_offset for reading in sensor_data]
    return [val + 0.13 for val in adjusted]  # Compensate for calibration lag

# Secondary processing: filter unstable growth phases
def filter_growth_phases(phases, threshold=0.75):
    stable_mask = [phase > threshold for phase in phases]
    return [phase for phase, mask in zip(phases, stable_mask) if mask]

# Main calculation pipeline
soil_samples = [0.68, 0.72, 0.81, 0.93, 0.67, 0.74]
humidity_log = [0.77, 0.82, 0.69, 0.91]

# Irrelevant signal processing (distractor)
signal_noise_floor = 0.15
filtered_signals = [max(0, x - signal_noise_floor) for x in humidity_log]
denoised_aggregate = sum(filtered_signals) / len(filtered_signals) if filtered_signals else 0

# Normalize and combine sensor inputs
calibrated_soil = normalize_readings(soil_samples)
calibrated_humidity = normalize_readings(humidity_log)

# Simulate time-series alignment using cycling
sensor_cycle = cycle([1, 0, 1])
temporal_weights = [next(sensor_cycle) for _ in range(len(calibrated_soil))]
weighted_soil = [soil * weight for soil, weight in zip(calibrated_soil, temporal_weights)]

# Effective area metrics after weighting
area_metrics = [
    (calibrated_soil[i] + calibrated_humidity[i % len(calibrated_humidity)]) / 2
    for i in range(len(calibrated_soil))
]

# Growth cycle simulation with conditional suppression
growth_cycles = []
for i, metric in enumerate(area_metrics):
    if i % 2 == 0:
        growth_cycles.append(metric ** 2)
    else:
        growth_cycles.append(metric * 0.85)

# Misleading intermediate aggregation (dead path)
avg_cycle_potential = sum(growth_cycles) / len(growth_cycles) if growth_cycles else 0
potential_boost = avg_cycle_potential * 0.12  # Unused enhancement factor

# Filter only high-efficiency cycles
efficient_cycles = filter_growth_phases(growth_cycles, threshold=0.7)

# Final efficiency model incorporating diminishing returns
def calculate_harvest_efficiency(area_factors, cycles):
    base_efficiency = sum(area_factors) * 100
    cycle_bonus = len(cycles) * 5.5
    penalty = 0
    for f in area_factors:
        if f < 0.75:
            penalty += 3
    # Apply non-linear scaling on bonus
    adjusted_bonus = cycle_bonus * (0.9 ** penalty)
    total_effort = base_efficiency + adjusted_bonus
    
    # Red herring computation (not used)
    theoretical_max = len(area_factors) * 110
    utilization_ratio = total_effort / theoretical_max if theoretical_max > 0 else 0
    
    return total_effort * 0.83  # Final system efficiency factor

final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
print(f"Result: {final_yield}")