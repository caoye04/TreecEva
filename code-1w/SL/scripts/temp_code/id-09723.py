def analyze_pattern(sequence, threshold=3):
    char_count = {}
    for char in sequence:
        char_count[char] = char_count.get(char, 0) + 1

    frequent_chars = {k for k, v in char_count.items() if v >= threshold}
    
    # Irrelevant computation: counts even indices but not used in final result
    even_index_chars = set()
    for i, char in enumerate(sequence):
        if i % 2 == 0:
            even_index_chars.add(char)

    return frequent_chars


def generate_weight_map(labels):
    weight_map = {}
    for idx, label in enumerate(labels):
        weight_map[label] = (idx + 1) * 0.5
    
    # Distractor: unused transformation
    scaled_weights = [w ** 2 for w in weight_map.values()]
    total_scale = sum(scaled_weights)
    normalized = {k: v**2/total_scale for k, v in weight_map.items()} if total_scale > 0 else weight_map
    
    return weight_map  # Actual return, not normalized


def calculate_interference(phases, amplitudes):
    phase_values = []
    for i, (k, v) in enumerate(phases.items()):
        if k in amplitudes:
            phase_values.append(v * amplitudes[k])
    
    # Simulate wave superposition with conditional sign flip
    net_phase_shift = 0
    for i, val in enumerate(phase_values):
        if i % 2 == 0:
            net_phase_shift += val
        else:
            net_phase_shift -= val
    
    # Dead code: computes magnitude but doesn't use it
    magnitude = sum(abs(v) for v in phase_values)
    energy = magnitude ** 2 if magnitude > 1 else 0
    
    return net_phase_shift

# Main execution
signal_sequence = "abccbaadeeffggg"
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Step 1: Identify high-frequency characters
common_symbols = analyze_pattern(signal_sequence, threshold=3)

# Step 2: Generate amplitude weights for all labels
weights = generate_weight_map(labels)

# Step 3: Create phase mapping using enumerate and zip
phase_components = [180, 90, -90, 45, -45, 30, -30]
phase_map = dict(zip(labels, phase_components))

# Intermediate distractor: builds a state tracker that goes unused
state_log = []
for idx, (char, phase) in enumerate(zip(signal_sequence, signal_sequence)):
    if idx < 5:
        state_log.append(f'{idx}:{char}')

# Key statement
net_phase_shift = calculate_interference(phase_map, weights)

print(f"Result: {net_phase_shift}")