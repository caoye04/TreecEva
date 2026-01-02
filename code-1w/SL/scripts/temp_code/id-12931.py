import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSETS = {'sensor_a': 0.05, 'sensor_b': -0.03, 'sensor_c': 0.07}
BASELINE_NOISE_FLOOR = 0.002

# Irrelevant helper function – dead code path
sanitize_input = lambda x: [val for val in x if isinstance(val, (int, float))]

# Real data processing begins
raw_readings = [
    (1, 1024, 'A'), (2, 2048, 'B'), (3, 512, 'A'),
    (4, 4096, 'C'), (5, 256, 'B'), (6, 8192, 'A')
]

# Extract only numeric ID and value (index 0 and 1)
extracted = [(item[0], item[1]) for item in raw_readings]

# Simulate noise filtering (some relevant, some not)
filtered_noise = list(filter(lambda x: x[1] > 500, extracted))  # Only values > 500 kept

# Mapping of sensor type to dynamic threshold (unused in logic but looks important)
threshold_map = {
    'A': lambda v: v * 0.1,
    'B': lambda v: v * 0.15,
    'C': lambda v: v * 0.2
}

# Decoy computation: appears critical but unused
aggregated_stats = {}
for typ in ['A', 'B', 'C']:
    subset = [x for x in raw_readings if x[2] == typ]
    if subset:
        values = [x[1] for x in subset]
        aggregated_stats[typ] = {
            'avg': sum(values) / len(values),
            'max': max(values),
            'exceeds_1024': len([v for v in values if v > 1024])
        }

# Actual signal analysis: count how many high-value entries per ID category
signal_groups = {}
for item in filtered_noise:
    group_key = item[0] % 3  # Artificial grouping: 0, 1, or 2
    if group_key not in signal_groups:
        signal_groups[group_key] = []
    signal_groups[group_key].append(item[1])

# Transform into growth ratios using logarithmic scaling (key step)
growth_factors = []
for key in sorted(signal_groups.keys()):
    series = sorted(signal_groups[key])
    if len(series) > 1:
        # Compute cumulative log ratio across sorted values
        log_sum = 0
        for i in range(1, len(series)):
            log_sum += math.log(series[i] / series[i-1])
        growth_factors.append(round(log_sum, 6))
    else:
        growth_factors.append(0.0)

# Secondary transformation: apply bitwise weighting based on group index (misleading)
weighted_accumulator = 0
for idx, factor in enumerate(growth_factors):
    shift_val = idx + 1
    # Bit manipulation that looks significant but only adds fixed offset
    weighted_accumulator += int(factor * 100) << shift_val

# Now compute actual diagnostic: sum of all original high values (after filter)
relevant_values = [x[1] for x in filtered_noise]
total_energy = sum(relevant_values)

# Diagnostic rule: if total energy has even number of bits set, scale by 1.5, else 0.75
bit_count = bin(total_energy).count('1')
scale_factor = 1.5 if bit_count % 2 == 0 else 0.75
adjusted_diagnostic = total_energy * scale_factor

# Final adjustment based on growth pattern count (only two groups had multiple entries)
growth_trigger = len([g for g in growth_factors if g > 0])

# Key statement
final_diagnostic = analyze_readings(filtered_data, threshold_map) if 'filtered_data' in locals() else adjusted_diagnostic * 0.9

# But wait — filtered_data was never defined... so fallback activates
# Correction: use correct variable name
final_diagnostic = adjusted_diagnostic

# Add red herring: complex set operation with no impact
unique_power_levels = set(relevant_values)
reference_set = {512, 1024, 2048, 4096, 8192}
divergence_score = len(unique_power_levels ^ reference_set)  # Unused

# Another decoy function
validate_consistency = lambda data: all(d > 0 for d in data)
validation_result = validate_consistency(relevant_values)  # True, but unused

# Print final answer as required
print(f"Result: {final_diagnostic}")