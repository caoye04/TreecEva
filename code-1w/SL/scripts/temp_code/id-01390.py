import itertools

# Irrelevant helper function (dead code path)
def dummy_normalization(data):
    return [x / sum(data) for x in data]

# Misleading intermediate calculation with decoy variables
temp_offsets = [0.1, -0.2, 0.15, -0.05, 0.3]
decoherence_factors = [0.98, 1.02, 0.99, 1.01, 0.97]

# Real data: quantum process stages with phase and energy values
process_stages = [
    {'phase': 0.5, 'energy': 200, 'stability': True},
    {'phase': 1.2, 'energy': 450, 'stability': True},
    {'phase': 0.8, 'energy': 320, 'stability': False},
    {'phase': 1.6, 'energy': 610, 'stability': True},
    {'phase': 0.9, 'energy': 380, 'stability': True}
]

# Decoy transformation using zip and enumerate (not used in final result)
for idx, (offset, factor) in enumerate(zip(temp_offsets, decoherence_factors)):
    adjusted = (offset + 0.01) * factor

# Unused list comprehension with set operation distraction
effective_indices = {i for i in range(len(process_stages)) if process_stages[i]['stability']}
irrelevant_pairs = list(itertools.combinations([p['energy'] for p in process_stages], 2))

# Core logic disguised within distraction
stable_phases = []
energy_accumulator = 0

for i, stage in enumerate(process_stages):
    if stage['stability']:
        # Only stable stages contribute to thermal integral
        normalized_phase = stage['phase'] * (stage['energy'] / 100.0)
        stable_phases.append(normalized_phase)
        energy_accumulator += stage['energy']

# Red herring: complex-looking but unused bitwise chain
checksum = 0
for val in temp_offsets:
    checksum ^= int(abs(val) * 1000) & 255

# Actual thermal integral calculation
phase_product = 1.0
for p in stable_phases:
    phase_product *= max(p, 0.1)  # Avoid zeroing

energy_factor = energy_accumulator / len(stable_phases) if stable_phases else 0

# Key statement: what is the value of thermal_capacity here?
thermal_capacity = calculate_thermal_integral(process_stages)

# Function defined after use (distractor for reading order)
def calculate_thermal_integral(stages):
    stable_energies = [s['energy'] for s in stages if s['stability']]
    base_integral = sum(stable_energies)
    
    # Apply non-linear correction based on phase variance
    stable_phases = [s['phase'] for s in stages if s['stability']]
    mean_phase = sum(stable_phases) / len(stable_phases)
    variance = sum((p - mean_phase) ** 2 for p in stable_phases) / len(stable_phases)
    correction = 1 + (variance * 0.5)
    
    # Final thermal capacity
    return int(base_integral * correction)

# Print target result
Result: {thermal_capacity}