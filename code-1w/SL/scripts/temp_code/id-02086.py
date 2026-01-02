import math

def generate_harmonic(index, base_freq):
    return (index + 1) * base_freq * math.pi / 4

def apply_damping(value, damping_factor):
    if value > 0:
        return value * (1 - damping_factor)
    return value * (1 + damping_factor)

def calculate_interference(phases, weights):
    weighted_sum = 0.0
    temp_buffer = []
    
    for i in range(len(phases)):
        raw_contribution = phases[i] * weights[i % len(weights)]
        adjusted = apply_damping(raw_contribution, 0.1)
        temp_buffer.append(adjusted)
    
    # Irrelevant accumulation
    cumulative_noise = 0.0
    for x in temp_buffer:
        cumulative_noise += abs(x) * 0.05
        if cumulative_noise > 10:  # dead code path
            cumulative_noise = 10

    # Actual signal logic
    signal_power = 0.0
    for val in temp_buffer[:len(temp_buffer)//2 + 1]:
        if val != 0:
            signal_power += math.sin(val) ** 2
    
    # Secondary loop with slicing distraction
    mirror_slice = temp_buffer[::-1]
    for j in range(len(mirror_slice)):
        temp_buffer[j] -= mirror_slice[j] * 0.1  # minor perturbation

    final_acc = 0.0
    for k, v in enumerate(temp_buffer):
        phase_lock = k % 3 == 0
        scaling = 1.5 if phase_lock else 0.8
        final_acc += v * scaling

    result = final_acc / (len(temp_buffer) or 1)
    return round(result, 4)

# Main execution
base_frequencies = [2, 3, 5, 7, 11]
frequency_weights = [1.1, 0.9, 1.2, 0.8]
dummy_tracker = {'count': 0, 'flags': []}

phase_sequence = []
for idx, freq in enumerate(base_frequencies):
    harmonic = generate_harmonic(idx, freq)
    dampened_harmonic = apply_damping(harmonic, 0.05)
    if idx % 2 == 0:
        phase_sequence.append(dampened_harmonic)
    else:
        phase_sequence.insert(0, dampened_harmonic)  # alters order

    # Distractor block: tracking irrelevant state
    dummy_tracker['count'] += 1
    dummy_tracker['flags'].append(len(dummy_tracker['flags']) + idx > 2)

# Misleading pre-calculation
average_phase = sum(phase_sequence) / len(phase_sequence)
normalized_phases = [p / (abs(average_phase) + 1e-5) for p in phase_sequence]

# Key computation with conditional expression
net_phase_shift = calculate_interference(
    normalized_phases if len(normalized_phases) > 3 else phase_sequence,
    frequency_weights
)

# Additional red herring: unused transformation
shifted_chars = ''.join([chr((ord('a') + int(abs(p*2)) % 26)) for p in phase_sequence])

Result: {net_phase_shift}