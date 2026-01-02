from itertools import combinations
from math import ceil

# Simulate sensor readings from a manufacturing plant with noise filtering
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.2, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 51, 45]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1013, 1011, 1017]

# Filter out extreme values using set logic
valid_temps = {t for t in temperature_readings if 23 <= t <= 25}
valid_humidity = {h for h in humidity_readings if 44 <= h <= 49}
dropped_pressure_indices = {i for i, p in enumerate(pressure_readings) if abs(p - 1013) > 3}

# Normalize remaining data
filtered_temps = sorted(valid_temps)
normalized_humidity = [max(h - 40, 0) for h in valid_humidity]

# Simulate batch production runs under varying conditions
base_output_per_run = 250
fluctuation_factor = sum(filtered_temps) / len(filtered_temps) * 0.1
adjusted_outputs = [int(base_output_per_run + (i * 5) - fluctuation_factor * 10) for i in range(8)]

# Track cumulative performance metrics (some are red herrings)
cumulative_waste = 0
cycle_efficiency = []
running_total_output = 0

for idx, output in enumerate(adjusted_outputs):
    if idx % 3 == 0:
        cumulative_waste += 15
    efficiency = (output / base_output_per_run) * 100
    cycle_efficiency.append(round(efficiency, 2))
    running_total_output += output

# Calculate theoretical max using combinatorics (distractor)
possible_pairs = list(combinations(adjusted_outputs, 2))
theoretical_max = max([a + b for a, b in possible_pairs])
avg_pair_output = int(sum([a + b for a, b in possible_pairs]) / len(possible_pairs))

# Core optimization logic based on threshold filtering and adjustment
stable_outputs = [o for o in adjusted_outputs if abs(o - base_output_per_run) <= 30]
threshold_adjustment = len(stable_outputs) * 3

# Simulate yield optimization pass
def optimize_production(runs):
    total_batches = len(runs)
    base_yield = sum(runs) // total_batches
    peak_count = len([r for r in runs if r > base_yield])
    
    # Secondary adjustment based on environmental normalization
    env_compensation = int(ceil((sum(normalized_humidity) / len(normalized_humidity)) * 0.75))
    
    # Final formula: average output + stability bonus + environment factor
    stability_bonus = threshold_adjustment
    final_calc = base_yield + stability_bonus + env_compensation
    
    # Misleading recursive path (never taken)
    def recursive_boost(n):
        if n <= 1:
            return n
        return recursive_boost(n-1) + recursive_boost(n-2)
    
    # This condition is never true due to fixed data
    if theoretical_max > 10000:
        final_calc += recursive_boost(5)
    
    return final_calc

# Execute main calculation
final_yield = optimize_production(adjusted_outputs)

# Print result as required
print(f"Target result: {final_yield}")