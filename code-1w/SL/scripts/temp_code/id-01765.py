from itertools import combinations

def analyze_quantum_state(states):
    coherence = 0
    decoherence = 0
    for i, state in enumerate(states):
        if i % 2 == 0:
            coherence += state ** 0.5
        else:
            decoherence += state ** 0.3
    return coherence - decoherence

def filter_resonant_modes(modes, threshold=3.5):
    # Irrelevant filtering for distraction
    resonant = [m for m in modes if sum(m) > threshold]
    normalized = []
    for r in resonant:
        norm_val = sum([x**2 for x in r]) ** 0.5
        if norm_val > 0:
            normalized.append([x / norm_val for x in r])
    return normalized

def calculate_thermal_output(energy_levels, shifters):
    base_energy = sum(energy_levels)
    adjustment_factor = 1.0
    temp_buffer = []
    
    for idx, (e, s) in enumerate(zip(energy_levels, shifters)):
        shifted = e * (s + 1) if idx % 2 == 0 else e / (s + 0.5)
        temp_buffer.append(shifted)
    
    # Secondary processing with distractor variables
    avg_temp = sum(temp_buffer) / len(temp_buffer)
    mode_combinations = list(combinations(temp_buffer, 2))
    fluctuation_score = 0
    for pair in mode_combinations:
        fluctuation_score += abs(pair[0] - pair[1])
    
    # Actual computation path
    raw_sum = sum(temp_buffer)
    peak = max(temp_buffer)
    thermal_capacity = int(raw_sum * (peak / avg_temp))  # Key assignment
    
    # Dead code path - misleading
    if len(mode_combinations) > 10:
        dummy_correction = fluctuation_score / len(mode_combinations)
        thermal_capacity -= int(dummy_correction)
    
    return thermal_capacity

# Simulation parameters
energy_states = [1.2, 3.4, 2.1, 5.6, 4.3, 3.9]
phase_shifters = [0.8, 1.1, 0.5, 1.3, 0.9, 1.0]

# Irrelevant pre-processing
state_analysis = analyze_quantum_state(energy_states)
resonant_modes = filter_resonant_modes([[1,2], [3,4], [5,6]], threshold=2.0)
buffer_overflow_sim = [i * 0.1 for i in range(len(energy_states) * 2)]

# Critical execution point
thermal_capacity = calculate_thermal_output(energy_states, phase_shifters)

print(f"Result: {thermal_capacity}")