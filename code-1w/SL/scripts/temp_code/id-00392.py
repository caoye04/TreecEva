from collections import defaultdict
import math

# Simulate a geothermal energy forecasting system with auxiliary diagnostics

def analyze_fault_lines(seismic_data):
    # Irrelevant helper: analyzes geological data but not used in final result
    cumulative_risk = 0
    for depth, readings in seismic_data.items():
        cumulative_risk += sum([r ** 0.5 for r in readings if r > 5])
    return cumulative_risk

def calculate_thermal_output(energy_stores, efficiency_ratio):
    base_output = 0
    adjustment_factor = 1.0
    
    # Core logic hidden among distractions
    for i, (zone, levels) in enumerate(energy_stores.items()):
        if i % 2 == 0:
            base_output += sum(levels) * efficiency_ratio
        else:
            base_output -= sum(levels) * 0.1  # Penalty for odd zones
    
    # Distractor: complex but unused transformation
    inverted_map = {k: [100 / (v + 1) for v in vs] for k, vs in energy_stores.items()}
    
    # Relevant adjustment
    adjustment_factor *= math.log(1 + len(energy_stores))
    
    return int(base_output * adjustment_factor)

# Real input data
energy_reserves = {
    'north_shaft': [12, 15, 14, 13],
    'east_ridge': [18, 20, 19],
    'west_cavity': [25, 24, 26, 25, 27],
    'south_vent': [8, 9]
}

efficiency_factor = 0.87

# Dead code path: simulation of sensor degradation (unused)
def simulate_degradation(values):
    degraded = []
    for v in values:
        for _ in range(3):
            v = v * 0.98 - 0.1
        degraded.append(max(v, 0))
    return degraded

# Unused diagnostic structure
diagnostic_log = defaultdict(int)
for region in energy_reserves:
    diagnostic_log[region] += 1  # Meaningless increment

# Sensor offset calibration (irrelevant computation)
sensor_offsets = [0.12, -0.05, 0.3, 0.0, -0.1]
adjusted_offsets = [round(abs(o) ** 2, 3) for o in sensor_offsets]
total_calibration = sum(adjusted_offsets) / len(adjusted_offsets)

# Key execution point
thermal_capacity = calculate_thermal_output(energy_reserves, efficiency_factor)

# Additional red herring: bit manipulation on unrelated metric
active_zones = len(energy_reserves)
mask = (1 << 3) - 1
masked_zones = active_zones & mask | 4  # Result unused

# Final output
Result: {thermal_capacity}