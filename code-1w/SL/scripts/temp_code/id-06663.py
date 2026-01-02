import math

# Simulated sensor array data from industrial filtration system
turbidity_readings = [0.45, 0.67, 1.23, 0.89, 2.01, 1.44, 0.98, 3.21, 2.76, 1.99]
pressure_drops = [12.1, 14.3, 18.9, 15.6, 22.4, 19.8, 16.7, 28.1, 25.3, 20.2]
flow_rates = [5.5, 5.4, 5.1, 5.3, 4.8, 5.0, 5.2, 4.5, 4.6, 4.9]

timestamp_groups = {
    'morning': slice(0, 4),
    'afternoon': slice(4, 7),
    'evening': slice(7, 10)
}

# Irrelevant transformation: normalize flow rates (not used in final logic)
normalized_flows = [round((x - min(flow_rates)) / (max(flow_rates) - min(flow_rates)), 3) for x in flow_rates]

# Distractor function: calculates efficiency but is never called
def calculate_thermal_efficiency(temp_list):
    return sum([t * 0.83 for t in temp_list if t > 15.0])

# Critical data processing
high_turbidity = [i for i, t in enumerate(turbidity_readings) if t > 1.0]
low_flow_periods = [i for i, f in enumerate(flow_rates) if f < 4.7]
stable_pressure = [i for i, p in enumerate(pressure_drops) if 15 <= p <= 20]

# Misleading intermediate result
apparent_correlation = len([x for x in high_turbidity if x in low_flow_periods])

# Set operations on phase indices
maintenance_windows = {1, 4, 7, 9}
calibration_cycles = {0, 2, 5, 8}

# Complex slicing based on time groups
morning_indices = set(range(*timestamp_groups['morning'].indices(10)))
afternoon_indices = set(range(*timestamp_groups['afternoon'].indices(10)))
evening_indices = set(range(*timestamp_groups['evening'].indices(10)))

diurnal_variability = morning_indices | evening_indices

# Decoy statistical calculation
weighted_variance = 0.0
for i in range(len(turbidity_readings)):
    diff = turbidity_readings[i] - sum(turbidity_readings)/len(turbidity_readings)
    weighted_variance += diff ** 2 * (pressure_drops[i] / 10)
weighted_variance /= len(turbidity_readings)

# Define effective filters using bitwise and arithmetic logic
filter_flags = 0
for idx in high_turbidity:
    filter_flags |= (1 << idx)

# Convert back to index list
extracted_filters = []
for i in range(10):
    if filter_flags & (1 << i):
        extracted_filters.append(i)

effective_filters = set(extracted_filters)

# Define operational phases using set logic
startup_phase = {0, 1, 2}
runtime_phase = {3, 4, 5, 6}
shutdown_phase = {7, 8, 9}

operational_phases = runtime_phase.union(stable_pressure)

# Introduce red herring variable with similar name
effective_filter_count = len(effective_filters) + 5  # fake metric

# Key statement — this is where the answer is determined
filtration_score = len(effective_filters & operational_phases)

# Dead code path — never executed
def update_calibration_matrix():
    nonlocal calibration_cycles
    new_cycle = {x+1 for x in calibration_cycles if x < 9}
    calibration_cycles.update(new_cycle)

# Unused cleanup routine
temporal_outliers = []
for group_slice in timestamp_groups.values():
    segment = turbidity_readings[group_slice]
    mean_val = sum(segment) / len(segment)
    for val in segment:
        if abs(val - mean_val) > 0.5:
            temporal_outliers.append(True)

# Print target result
print(f"Result: {filtration_score}")