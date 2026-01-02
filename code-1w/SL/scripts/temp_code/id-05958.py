import itertools

# Simulate multi-stage chemical processing with noise and side calculations

def simulate_reaction(temps):
    return [t ** 2 + 3 * t + 1 for t in temps if t > 0]

# Raw input data from sensor array (some values corrupted)
temperature_readings = [-5, 2, -3, 7, 0, 4, -1, 9, 6, 8]

# Irrelevant transformation: normalize to percentages (unused later)
normalized_readings = [round((t + 5) / 15 * 100) for t in temperature_readings if -5 <= t <= 10]

# Step 1: Filter valid temperatures above threshold
effective_temps = [t for t in temperature_readings if t >= 4]

# Step 2: Simulate reaction output using effective temperatures
reaction_outputs = simulate_reaction(effective_temps)

# Step 3: Apply decay model over time (simulated via index)
decay_factors = [0.95 ** i for i in range(len(reaction_outputs))]
applied_decay = [out * fac for out, fac in zip(reaction_outputs, decay_factors)]

# Step 4: Introduce control variables for pH and pressure (only one used)
optimal_ph_levels = [7.2, 7.4, 7.3, 7.6, 7.1]
avg_pressure_kpa = 101.3

calibration_offset = sum([abs(p - 7.3) for p in optimal_ph_levels])  # Distractor: unused

# Step 5: Filter concentrations above safety threshold (key step)
raw_concentrations = applied_decay
safety_threshold = 100
toxic_level_mask = [conc > 150 for conc in raw_concentrations]  # Misleading: not actually used
filtered_concentrations = [c for c in raw_concentrations if c > safety_threshold]

# Step 6: Compute equipment efficiency based on operational hours
equipment_hours = 427
efficiency_factor = max(0.5, 1 - (equipment_hours * 0.001))

# Step 7: Compute final filtration yield — this is the target line
filtration_yield = sum(filtered_concentrations) * efficiency_factor

# Red herring: complex bit manipulation on unrelated metric
status_code = 0b1101 ^ 0b1011
status_code = status_code << 2 | 0b10
final_diagnostic = bin(status_code ^ 0b1111)[2:]

# Dead code path: unused optimization routine
def optimize_flow_rate(flow):
    if flow < 10:
        return flow ** 2
    else:
        return optimize_flow_rate(flow - 5)

# Unused list generated via itertools (distractor)
permutations = list(itertools.permutations([1, 2, 3], 3))
combination_count = len(list(itertools.combinations(['a', 'b', 'c', 'd'], 2)))

# Unrelated statistical check (dead end)
if len(raw_concentrations) > 5:
    mean_val = sum(raw_concentrations) / len(raw_concentrations)
    variance = sum((x - mean_val) ** 2 for x in raw_concentrations) / len(raw_concentrations)

# Output the target result
print(f"Result: {filtration_yield}")