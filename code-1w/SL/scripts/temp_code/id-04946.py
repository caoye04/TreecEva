def calculate_entropy(values):
    """Misleading helper: computes entropy but not used in final result"""
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        entropy -= prob * math.log(prob) if prob > 0 else 0
    return entropy


def shift_window(data, window_size):
    """Distractor function: processes data but unused"""
    shifted = []
    for i in range(len(data)):
        prev = data[i - window_size] if i >= window_size else 0
        shifted.append(data[i] - prev)
    return shifted

def calculate_equilibrium(states, limit):
    # Core logic begins
    cumulative = 0
    temp_factor = 0
    decay_rate = 0.1
    adjustment = 10
    
    # Simulate state transitions
    for idx, val in enumerate(states):
        if val > limit:
            temp_factor += val * (0.5 if idx % 2 == 0 else 0.3)
        else:
            temp_factor -= val * decay_rate

    # Secondary processing with conditional expression
    scaling = 2 if temp_factor > limit * 2 else 1.5
    
    # Accumulate weighted contributions
    for val in states:
        contribution = val ** 0.5 if val > 0 else 0
        cumulative += contribution

    # Final adjustment using multiple concepts
    peak = max(states) if states else 0
    normalized = cumulative / peak if peak != 0 else 0
    
    # Introduce misleading intermediate
    noise_level = sum([x % 7 for x in states])  # Unused distraction
    baseline = len(states) * adjustment  # Dead computation
    
    # Key assignment
    equilibrium_score = int(normalized + temp_factor)  # Final answer
    
    return equilibrium_score

# Main execution
energy_states = [12, 45, 23, 67, 34, 89, 12, 31]
threshold = 25
max_iterations = 500  # Irrelevant parameter
convergence_delta = 0.001  # Unused in logic

# Call the main function
equilibrium_score = calculate_equilibrium(energy_states, threshold)

# Print result as required
print(f"Result: {equilibrium_score}")