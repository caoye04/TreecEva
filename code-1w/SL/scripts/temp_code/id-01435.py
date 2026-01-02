from itertools import cycle

# Simulate time-series environmental data for energy transfer analysis
time_intervals = [0.5, 1.0, 1.5, 2.0, 2.5]
base_emissions = [30, 45, 40, 55, 50]
transfer_rates = [0.8, 0.75, 0.9, 0.65, 0.85]

# Auxiliary irrelevant metrics (distractor variables)
power_draw = [120, 135, 128, 142, 138]  # not used in final calculation
thermal_loss = [8.2, 9.1, 8.7, 10.3, 9.6]  # distractor
voltage_stability = [True, True, False, False, True]  # dead code path

# Real-time sensor weight factors (only some are relevant)
weights = [1.1, 0.9, 1.0, 0.95, 1.05]
adjusted_emissions = []
for i, emission in enumerate(base_emissions):
    adjusted = emission * weights[i % len(weights)]
    adjusted_emissions.append(adjusted)

# Compute cumulative effective transfer using sliding window
rolling_effective = []
cycle_weights = cycle([1.0, 0.95])  # alternating correction factor
for j in range(len(adjusted_emissions)):
    raw_transfer = adjusted_emissions[j] * transfer_rates[j]
    corrected_transfer = raw_transfer * next(cycle_weights)
    rolling_effective.append(corrected_transfer)

# Aggregate total net transfer over monitored period
net_transfer = sum(rolling_effective) / len(rolling_effective)  # mean normalized

# Apply system degradation model (unrelated to power_draw despite naming)
system_age_years = 7
degradation_rate = 0.015
efficiency_factor = max(0.7, 1 - (system_age_years * degradation_rate))

# Final energy flux calculation — critical statement
final_flux = net_transfer * efficiency_factor

# Print result as required
print(f"Result: {final_flux}")