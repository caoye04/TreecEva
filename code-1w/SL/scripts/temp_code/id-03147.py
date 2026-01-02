from collections import defaultdict

# Simulate a chemical reaction equilibrium process across temperature phases
def calculate_reaction_potential(temperatures, base_constant):
    potential = 0
    temp_factor = 1.0
    for t in temperatures:
        if t > 300:
            temp_factor *= 1.05
        elif t < 273:
            temp_factor *= 0.98
        potential += (t * temp_factor) % 97
    return int(potential)

# Track molecular state transitions during phase shifts
def track_molecular_states(phases):
    state_count = defaultdict(int)
    transition_energy = 0
    for i in range(len(phases) - 1):
        current, next_phase = phases[i], phases[i+1]
        delta = abs(hash(current[:2]) - hash(next_phase[:2])) % 13
        transition_energy += delta
        state_count[current] += 1
    state_count['final'] += 1  # irrelevant update
    return transition_energy

# Find index where forward and reverse reaction potentials balance
def find_equilibrium_index(sequence):
    total = sum(sequence)
    left_sum = 0
    for i, value in enumerate(sequence):
        # Check if left_sum equals right_sum (excluding current element)
        right_sum = total - left_sum - value
        if left_sum == right_sum:
            return i
        left_sum += value
    return -1

# Experimental parameters
temp_phases = [298, 305, 315, 273, 260, 250, 320]
molecular_phases = ['solid', 'liquid', 'gas', 'plasma', 'liquid', 'solid']
baseline_k = 42.7

# Irrelevant precomputations (distractors)
reaction_potential = calculate_reaction_potential(temp_phases, baseline_k)
energy_signature = track_molecular_states(molecular_phases)
scaling_factor = (reaction_potential * energy_signature) % 1000 / 100

# Core sequence representing enthalpy-entropy compensation values
process_sequence = [4, 7, 3, 9, 2, 8, 5]

# Additional distracting calculations
entropy_adjustments = [x * scaling_factor for x in process_sequence]
adjusted_total = sum([abs(x - scaling_factor) for x in entropy_adjustments])

# Key computation
equilibrium_index = find_equilibrium_index(process_sequence)

# Print final result
print(f"Result: {equilibrium_index}")