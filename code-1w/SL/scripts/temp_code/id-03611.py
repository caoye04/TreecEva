import math

def preprocess_data(raw_samples):
    filtered = [x for x in raw_samples if x > 0.1]
    normalized = [x / sum(filtered) for x in filtered]
    return normalized

def generate_profile(values):
    profile = []
    for v in values:
        profile.append(math.sin(v) + math.cos(v))
    return profile

def analyze_variability(seq):
    variance = sum((x - sum(seq)/len(seq))**2 for x in seq) / len(seq)
    return variance

def calculate_equilibrium(matrix, limit):
    # Misleading intermediate computations
    temp_buffer = []
    for row in matrix:
        temp_buffer.extend([x * 1.5 for x in row if x < limit])
    
    # Actual relevant logic begins here
    aggregated = [sum(col) for col in zip(*matrix)]
    trimmed = aggregated[1:-1]  # Remove edge effects
    
    # Compute weighted center of mass
    total_weight = sum(trimmed)
    if total_weight == 0:
        return 0
    
    weighted_sum = sum(i * val for i, val in enumerate(trimmed))
    center_of_mass = weighted_sum / total_weight
    
    # Secondary adjustment based on symmetry
    reverse_sum = sum(trimmed[::-2])  # Every other element from end
    forward_sum = sum(trimmed[::2])   # Every other element from start
    symmetry_offset = abs(forward_sum - reverse_sum)
    
    # Distractor: unused statistical check
    mean_val = sum(trimmed) / len(trimmed)
    outlier_count = sum(1 for x in trimmed if abs(x - mean_val) > 2 * math.sqrt(symmetry_offset + 1e-5))
    
    # Final computation
    equilibrium_score = int(center_of_mass + symmetry_offset)
    
    # Dead code branch (never executed due to fixed input)
    if False and len(matrix) > 100:
        fallback = sum(temp_buffer) // (len(matrix) + 1)
        return fallback
    
    return equilibrium_score

# Simulated experimental data (fixed seed equivalent)
raw_input = [0.5, 0.8, 0.3, 0.9, 0.2, 0.7, 0.4, 0.6]
processed = preprocess_data(raw_input)
concentration_matrix = [
    [0.1, 0.4, 0.6, 0.3, 0.2],
    [0.2, 0.5, 0.7, 0.4, 0.3],
    [0.1, 0.6, 0.8, 0.5, 0.2],
    [0.3, 0.4, 0.6, 0.7, 0.1]
]

# Irrelevant auxiliary analysis
signal_profile = generate_profile(processed)
variability_index = analyze_variability(signal_profile)
threshold = 1.0  # Fixed threshold

# Key statement
equilibrium_score = calculate_equilibrium(concentration_matrix, threshold)

# Output result
print(f"Result: {equilibrium_score}")