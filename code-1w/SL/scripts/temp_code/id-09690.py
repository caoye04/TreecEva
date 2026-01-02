from itertools import compress, cycle
import math

# Simulated sensor readings from a chemical filtration array
turbidity_readings = [0.45, 0.32, 0.78, 0.15, 0.63, 0.88, 0.29, 0.51]
pressure_fluctuations = [1.02, 0.98, 1.05, 0.94, 1.11, 0.89, 1.03, 0.97]
temperature_spikes = [2.1, 1.8, 3.4, 1.2, 2.9, 4.1, 1.7, 2.5]

# Irrelevant transformation: temperature normalization (unused later)
normalized_temps = [round((t - min(temperature_spikes)) / (max(temperature_spikes) - min(temperature_spikes)), 3) for t in temperature_spikes]

# Distractor: simulate false alarm detection
false_alarms = []
for i, spike in enumerate(temperature_spikes):
    if spike > 3.0 and pressure_fluctuations[i] < 1.0:
        false_alarms.append(i)

# Key masking logic: determine valid windows based on turbidity threshold
valid_window_mask = [turbidity < 0.6 for turbidity in turbidity_readings]

# Use itertools.compress to extract aligned low-turbidity data
filtered_pressures = list(compress(pressure_fluctuations, valid_window_mask))
filtered_indices = list(compress(range(len(turbidity_readings)), valid_window_mask))

# Dead code path: hypothetical recalibration (never used)
if len(filtered_pressures) > 5:
    recalibrated = [p * 0.98 for p in filtered_pressures]
else:
    recalibrated = [p * 1.02 for p in filtered_pressures]

# Compute aggregate stability score (red herring variable)
stability_score = sum(
    abs(filtered_pressures[i] - filtered_pressures[i-1])
    for i in range(1, len(filtered_pressures))
) / len(filtered_pressures) if filtered_pressures else 0

# Real computation begins: purity analysis
raw_purity = sum(1 for t in turbidity_readings if t < 0.6)
event_count = len(turbidity_readings)
base_purity = raw_purity / event_count

# Secondary filter: detect micro-outliers in clean subset
micro_outlier_mask = [abs(p - 1.0) > 0.05 for p in filtered_pressures]
outlier_suppression = sum(micro_outlier_mask) * 0.01
net_purity = base_purity - outlier_suppression

# Efficiency factor derived from cyclic pattern analysis
ideal_cycle = [1.0, 0.99, 1.01, 0.98]
cycle_matcher = list(cycle(ideal_cycle))[:len(filtered_pressures)]

match_score = 0
for i in range(len(filtered_pressures)):
    if abs(filtered_pressures[i] - cycle_matcher[i]) < 0.03:
        match_score += 1

# Introduce bitwise obfuscation (irrelevant but plausible)
decoy_flag = 0b1010 ^ 0b1100 & 0b0110  # Result: 0b1110 -> 14, unused
flag_check = (decoy_flag | 0b0001) & 0b1111  # More distraction

efficiency_factor = (match_score / len(filtered_pressures)) if filtered_pressures else 0

# Critical assignment point — this is the answer target
filtration_yield = net_purity * efficiency_factor

# Additional red herring: string-based diagnostic log
log_parts = [f"S{idx}:OK" for idx in filtered_indices]
diagnostic_log = "|".join(log_parts).upper().replace("OK", "PASS")
diagnostic_checksum = sum(map(ord, diagnostic_log)) % 1000  # Unused checksum

# Final output (must print the target variable)
print(f"Result: {filtration_yield}")