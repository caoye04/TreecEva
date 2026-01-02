def preprocess_signal(data):
    return list(map(lambda x: (x * 3) % 7, filter(lambda x: x > 2, data)))

# Irrelevant helper that looks important but isn't used in critical path
def decoy_normalization(vector):
    magnitude = sum([v**2 for v in vector]) ** 0.5
    return [v / magnitude for v in vector] if magnitude else vector

def evaluate_coherence(seq):
    score = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            score += i * 2
        else:
            score -= i
    return score

def generate_checksum(elements):
    # Complex-looking but ultimately unused calculation
    base = sum(elements) % 11
    shift = len([e for e in elements if e % 3 == 0])
    return (base * shift + 5) % 13

def transform_coordinates(x, y):
    # Unused geometric transformation — red herring
    angle = 3.14159 / 4
    new_x = x * __import__('math').cos(angle) - y * __import__('math').sin(angle)
    new_y = x * __import__('math').sin(angle) + y * __import__('math').cos(angle)
    return round(new_x), round(new_y)

def analyze_system_state(sequence, flags):
    # Step 1: Filter relevant quantum states
    active_states = [s for s in sequence if s in flags]
    
    # Step 2: Apply preprocessing that matters
    processed = preprocess_signal(active_states)
    
    # Step 3: Compute coherence (this contributes to final result)
    coherence = evaluate_coherence(processed)
    
    # Step 4: Simulate phase shift using modular arithmetic
    shifted = [(p + coherence) % 9 for p in processed]
    
    # Step 5: Count transitions above threshold
    threshold_events = 0
    for i in range(1, len(shifted)):
        if shifted[i] - shifted[i-1] > 1:
            threshold_events += 1
    
    # Step 6: Use set operations to deduplicate and assess uniqueness
    unique_shifted = set(shifted)
    diversity_index = len(unique_shifted)
    
    # Step 7: Combine metrics into diagnostic
    raw_diagnostic = (coherence * 2) + (threshold_events * 3) - diversity_index
    
    # Step 8: Final adjustment based on global constraint
    if sum(shifted) > 20:
        raw_diagnostic += 5
    else:
        raw_diagnostic -= 2
    
    # Dead code branch — never executes due to prior logic
    if False and len(shifted) > 100:
        fallback = generate_checksum(shifted)
        raw_diagnostic = (raw_diagnostic + fallback) % 17
    
    return raw_diagnostic

# Main execution block
if __name__ == '__main__':
    # Initial sensor readings (simulated)
    quantum_sequence = [1, 4, 6, 3, 8, 2, 9, 5]
    
    # System operational flags — only some match quantum_sequence
    system_flags = {4, 6, 8, 10, 12}
    
    # Unused coordinate grid — misleading structure
    coordinate_grid = [(i, j) for i in range(3) for j in range(3)]
    rotated_coords = [transform_coordinates(x, y) for x, y in coordinate_grid]
    
    # Checksum computed but not used — distractor
    safety_checksum = generate_checksum(quantum_sequence)
    
    # Critical analysis call
    final_diagnostic = analyze_system_state(quantum_sequence, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")