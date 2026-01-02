from collections import defaultdict

# Simulate quantum energy decay across lattice points
def simulate_lattice_decay(steps, base_energy):
    lattice = defaultdict(float)
    decay_rate = 0.87
    for step in range(1, steps + 1):
        for i in range(1, 6):
            lattice[i] += base_energy / (step ** 0.5) * (decay_rate ** step)
    return dict(lattice)

# Misleading decoy function - never called
def deprecated_flux_model(x, y):
    temp = 0
    for i in range(x):
        for j in range(y):
            temp += (i - j) ** 2
    return temp // max(x, 1)

# Energy normalization using reference baseline
def normalize_energy(sequence, ref_level=1.0):
    normalized = []
    peak = max(sequence) if sequence else 1
    for val in sequence:
        norm_val = (val / peak) * ref_level
        if norm_val > 0.5:
            norm_val *= 0.9
        normalized.append(round(norm_val, 6))
    # Dead code path - result unused
    if len(normalized) > 10:
        smoothed = [sum(normalized[i:i+3])/3 for i in range(len(normalized)-2)]
    return normalized

# Determine activation thresholds based on mode
def generate_threshold_map(mode='standard'):
    base_map = {'low': 0.45, 'med': 0.68, 'high': 0.89}
    if mode == 'aggressive':
        return {k: v * 0.9 for k, v in base_map.items()}
    elif mode == 'conservative':
        return {k: v * 1.1 for k, v in base_map.items()}
    else:
        return base_map

# Core flux calculation with conditional gating
def calculate_gated_flux(values, gates):
    total = 0.0
    for v in values:
        category = 'low'
        if v > gates['med']:
            category = 'high'
        elif v > gates['low']:
            category = 'med'
        
        contribution = 0.0
        if category == 'high':
            contribution = v * 1.25
        elif category == 'med':
            contribution = v * 0.8
        else:
            contribution = v * 0.3
        total += contribution
    
    # Apply artificial damping factor
    damping = 0.93
    return total * damping

# Main net flux computation combining multiple factors
def calculate_net_flux(seq, th_map):
    # Preprocessing: filter and scale
    filtered = [x for x in seq if x > th_map['low']]
    scaled = [x * 1.15 for x in filtered]
    
    # Secondary filtering based on dynamic condition
    dyn_threshold = sum(scaled) / len(scaled) * 0.75 if scaled else 0
    refined = [x for x in scaled if x > dyn_threshold]
    
    # Compute gated flux
    flux = calculate_gated_flux(refined, th_map)
    
    # Irrelevant accumulator - distractor
    dummy_accum = 0
    for i in range(len(refined)):
        if refined[i] > 0:
            dummy_accum += (refined[i] % 7) * 0.1
    
    # Tertiary adjustment based on count
    count_bonus = len(refined) * 0.25 if len(refined) > 3 else 0
    final = flux + count_bonus
    
    # Unused transformation branch
    if len(refined) > 5:
        alt_final = sum(refined) * 0.88
        final = max(final, alt_final)
    
    return round(final, 6)

# Primary execution flow
lattice_data = simulate_lattice_decay(steps=12, base_energy=4.5)
energy_sequence = list(lattice_data.values())

# Normalize the energy readings
energy_sequence = normalize_energy(energy_sequence, ref_level=1.0)

# Generate mapping for threshold logic
threshold_map = generate_threshold_map(mode='standard')

# Spurious variable - no impact on final result
baseline_check = sum(1 for x in energy_sequence if x > 0.5)

# Critical statement
final_flux = calculate_net_flux(energy_sequence, threshold_map)

# Print result as required
print(f"Target result: {final_flux}")