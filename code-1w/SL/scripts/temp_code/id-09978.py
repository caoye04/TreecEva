import math

def generate_harmonics(bandwidth):
    return [math.sin(i * bandwidth) for i in range(1, 6)]

def evaluate_coherence(signal):
    coherence = sum([x ** 2 for x in signal if x > 0.3])
    normalization = len(signal) + 1
    return coherence / normalization

def compute_entropy(stream):
    entropy = 0.0
    for val in stream:
        if val != 0:
            entropy -= val * math.log(abs(val))
    return entropy

def detect_resonance(pattern):
    magnitude = sum(pattern) / len(pattern)
    threshold = 0.5
    return magnitude > threshold

def normalize_flux(values):
    max_val = max(values)
    return [v / max_val for v in values]

def derive_phase_sequence(entries):
    sequence = []
    for e in entries:
        if e < 0.5:
            sequence.append(int(e * 10))
        else:
            sequence.append(int(e * 5))
    return sequence

def calculate_invariant(data):
    # Irrelevant transformation (dead computation path)
    temp = [d ** 3 for d in data]
    invariant = sum(temp[i] for i in range(0, len(temp), 2))
    return invariant  # Not used later

def simulate_feedback_loop(init_state, iterations):
    state = init_state
    history = []
    for i in range(iterations):
        noise = math.cos(i * 0.5)
        state += noise * 0.1
        history.append(state)
    adjusted = [h * 0.9 for h in history]
    return adjusted

def calculate_equilibrium(matrix, shift):
    # Core relevant logic begins here
    flattened = [item for row in matrix for item in row]
    shifted_values = [flattened[i] * (shift + i) for i in range(len(flattened))]
    
    # Distractor: complex but unused transformation
    decoy_map = {i: math.exp(-i * 0.1) for i in range(len(shifted_values))}
    filtered = [v for v in shifted_values if v > 0]
    
    # Another red herring: entropy-like calculation
    phantom_entropy = 0.0
    for f in filtered:
        if f > 1:
            phantom_entropy += math.log(f) * f

    # Actual critical computation
    aggregate = sum(shifted_values) / (len(shifted_values) + shift)
    correction_factor = math.sin(shift) if shift > 0 else 0.0
    equilibrium = aggregate * (1 + correction_factor)
    
    # This function call looks important but returns unused result
    _ = compute_entropy(flattened)
    
    return equilibrium

# Main execution block
if __name__ == "__main__":
    # Setup input data
    flow_matrix = [
        [1.2, 0.8, 3.1],
        [2.5, 1.7, 0.4],
        [0.9, 2.2, 1.3]
    ]

    phase_shift = 2.0

    # Irrelevant pre-processing steps
    harmonics = generate_harmonics(0.3)
    coherence_score = evaluate_coherence(harmonics)
    resonance = detect_resonance(harmonics)
    normalized_flow = [normalize_flux(row) for row in flow_matrix]
    
    # Simulate side-effect process with no impact on final answer
    dummy_trace = simulate_feedback_loop(0.5, 10)
    invariant_result = calculate_invariant(dummy_trace)  # Unused
    
    # Key execution point
    thermal_gradient = calculate_equilibrium(flow_matrix, phase_shift)

    # More distractions
    phase_sequence = derive_phase_sequence(normalized_flow[0])
    decoy_sum = sum(phase_sequence) * 0.1
    
    # Output the target variable
    print(f"Result: {thermal_gradient}")