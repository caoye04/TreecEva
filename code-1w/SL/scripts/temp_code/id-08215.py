def calculate_entropy(values):
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * math.log(prob)
    return entropy

# Simulate quantum energy state transitions
def generate_energy_states(seed=42):
    states = []
    value = seed
    for i in range(8):
        if i % 3 == 0:
            value = (value * 1664525 + 1013904223) % 2**32
        elif i % 4 == 1:
            value = (value * 69069 + 1) % 2**32
        else:
            value = (value ^ (value >> 5)) % 2**20
        states.append(value % 100 + i)
    
    # Irrelevant transformation
    temp_data = [x * x for x in states if x < 50]
    temp_sum = sum(temp_data) // len(temp_data) if temp_data else 0
    
    # Another distraction: simulate noise
    noise_offset = 0
    for shift in [2, 3, 5]:
        noise_offset += (seed >> shift) % 10
    
    # Modify states based on cyclic rule
    adjusted = []
    for idx, s in enumerate(states):
        if idx > 0 and states[idx-1] % 4 == 0:
            adjusted.append(s + 2)
        else:
            adjusted.append(s - 1)
    
    return adjusted

# Determine system stability score
def calculate_equilibrium(energy_levels):
    size = len(energy_levels)
    
    # Compute gradient between consecutive states
    gradients = [energy_levels[i+1] - energy_levels[i] for i in range(size-1)]
    
    # Track direction changes (local maxima/minima)
    turning_points = 0
    for i in range(1, len(gradients)-1):
        if gradients[i-1] * gradients[i+1] < 0 and abs(gradients[i]) >= 1:
            turning_points += 1
    
    # Calculate center of mass
    weighted_sum = sum(i * e for i, e in enumerate(energy_levels))
    total_energy = sum(energy_levels)
    center_of_mass = weighted_sum / total_energy if total_energy != 0 else 0
    
    # Compute variance as instability measure
    mean_energy = total_energy / size
    variance = sum((e - mean_energy)**2 for e in energy_levels) / size
    
    # Distractor: unused complexity
    harmonic_proxy = 0
    for e in energy_levels:
        if e != 0:
            harmonic_proxy += 1 / abs(e)
    harmonic_proxy = size / harmonic_proxy if harmonic_proxy != 0 else 0
    
    # Conditional expression determining damping factor
    damping_factor = 2.0 if variance < 100 else (1.5 if variance < 150 else 1.0)
    
    # Final equilibrium formula: combines structural and statistical properties
    peak_ratio = turning_points / size
    balance_score = (center_of_mass + 1) / (variance + 1)
    
    # Key statement
    equilibrium_score = int((balance_score * 100) - (peak_ratio * 50) + (damping_factor * 10))
    
    # Dead code branch — never executed due to fixed input characteristics
    if any(x < 0 for x in energy_levels):
        fallback = sum(abs(x) for x in energy_levels)
        equilibrium_score = fallback % 100
    
    return equilibrium_score

# Main execution flow
energy_states = generate_energy_states()

# Additional distractions
snapshot_log = {"timestamp": 123456789, "readings": energy_states.copy(), "status": "stable"}
shadow_copy = [x for x in energy_states]
sync_flag = len(energy_states) % 2 == 0

# Critical computation
final_entropy = calculate_entropy(energy_states)
equilibrium_score = calculate_equilibrium(energy_states)

print(f"Result: {equilibrium_score}")