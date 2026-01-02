from itertools import accumulate

# System calibration parameters (some are red herrings)
calibration_factor = 0.87
redundant_offset = 231
legacy_threshold = 950
diagnostic_mode = False

# Process stage efficiencies and energy inputs
stage_efficiency = [0.78, 0.82, 0.69, 0.75, 0.88]
energy_input_kj = [1200, 1450, 1300, 1600, 1750]

# Auxiliary data for distraction
maintenance_cycles = [3, 1, 4, 2, 5]
uptime_hours = [8760, 8750, 8700, 8600, 8800]

# Simulate intermediate diagnostics (not used in final calculation)
if diagnostic_mode:
    avg_uptime = sum(uptime_hours) / len(uptime_hours)
    max_cycle = max(maintenance_cycles)

# Core transformation: compute effective energy per stage
effective_energy = [e * eff for e, eff in zip(energy_input_kj, stage_efficiency)]

# Accumulate energy with lambda-based correction factor
correction_fn = lambda x: x * 1.05 if x > 1300 else x * 0.98
adjusted_energy = [correction_fn(e) for e in effective_energy]

cumulative_load = list(accumulate(adjusted_energy))

# Secondary distraction: simulate legacy system comparison
legacy_simulation = []
for load in cumulative_load:
    if load > legacy_threshold:
        legacy_simulation.append(load * 0.76)
    else:
        legacy_simulation.append(load * 0.45)

# Unused helper function (dead code path)
def deprecated_calc(x, y):
    return (x + y) * redundant_offset // 100

# Critical computation chain
baseline_output = sum(cumulative_load) / len(cumulative_load)
scaling_factor = len([e for e in adjusted_energy if e > 1200])
modulation_index = sum(1 for x in maintenance_cycles if x > 2)

# Key statement
process_stages = {
    'loads': cumulative_load,
    'count': scaling_factor,
    'index': modulation_index
}

def calculate_thermal_output(stages):
    base = sum(stages['loads']) / 1000
    multiplier = stages['count'] * 1.25
    penalty = stages['index'] * 0.15
    return int((base * multiplier) - (base * penalty))

thermal_capacity = calculate_thermal_output(process_stages)
Result: {thermal_capacity}