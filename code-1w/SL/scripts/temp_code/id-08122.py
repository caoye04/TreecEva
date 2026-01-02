import math

def analyze_pattern(sequence, threshold=0.75):
    length = len(sequence)
    mid = length // 2
    left_half = sequence[:mid]
    right_half = sequence[mid:]
    
    # Distractor: Count character frequencies (not used in final result)
    freq_map = {}
    for char in sequence:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    # Distractor: Redundant transformation
    transformed = ''.join([chr((ord(c) - ord('a') + 3) % 26 + ord('a')) for c in sequence])

    # Relevant: Extract phase-like segments
    step = max(1, len(left_half) // 4)
    phase_slices = []
    for i in range(0, len(left_half), step):
        if i + step <= len(left_half):
            phase_slices.append(left_half[i:i+step])
    
    return phase_slices


def calculate_interference(slices, weights):
    total_interference = 0.0
    base_weight = weights['base']
    
    # Simulate wave-like interference with nested logic
    for i, seg in enumerate(slices):
        segment_value = 0
        for j, c in enumerate(seg):
            # Map char to pseudo-phase (a=0, b=pi/13, ..., z=2pi)
            angle = (ord(c) - ord('a')) * (2 * math.pi / 26)
            segment_value += math.sin(angle) + math.cos(angle * 1.5)
        
        # Weighted contribution
        weighted_contribution = segment_value * base_weight * (weights['factor'] ** i)
        total_interference += weighted_contribution
        
        # Distractor: State tracking with unused variables
        if i % 2 == 0:
            dummy_state = {'index': i, 'value': weighted_contribution, 'flag': True}
        else:
            dummy_state = None
    
    # Final nonlinear scaling
    if total_interference > 0:
        total_interference = math.log(1 + total_interference)
    else:
        total_interference = -math.log(1 - total_interference) if total_interference < 1 else -999

    return total_interference


# Main execution
signal_sequence = "quantumresonance"
config_weights = {
    'base': 1.7,
    'factor': 0.85,
    'offset': 42  # Unused parameter (distractor)
}

# Extract phase components
phase_slices = analyze_pattern(signal_sequence, threshold=0.68)

# Compute net phase shift through interference model
net_phase_shift = calculate_interference(phase_slices, config_weights)

# Distractor: Unrelated list processing
temp_data = [len(s) for s in phase_slices]
avg_len = sum(temp_data) / len(temp_data) if temp_data else 0

# Distractor: Dead code path (never executed due to fixed input)
if len(signal_sequence) > 50:
    net_phase_shift *= 1.5

# Output the target result
print(f"Result: {net_phase_shift}")