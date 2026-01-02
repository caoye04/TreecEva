import itertools

# Irrelevant helper function (dead code path)
def unused_signal_filter(data):
    return [x for x in data if x > 0.5]

# Misleading intermediate computation
temp_calibration = sum([i * 0.1 for i in range(10)])

# Real input parameters
stress_levels = list(range(1, 21))

# Distractor: complex-looking but unused configuration
decoys = {
    'noise_threshold': 0.87,
    'bandwidth_limit': 256,
    'mode': 'adaptive',
    'payload': [i ** 0.5 for i in range(100) if i % 17 == 0]
}

# Material configuration with red herring keys
material_config = {
    'elastic_modulus': 210e3,
    'yield_ratio': 0.42,
    'damping_factor': 0.03,
    'grain_orientation': [(i, j) for i, j in itertools.product([1, -1], repeat=2)],
    'decoy_matrix': [[0 for _ in range(4)] for _ in range(4)]  # Unused
}

# Irrelevant set operation (distraction)
observed_phases = set(['alpha', 'beta', 'gamma'])
expected_phases = set(['alpha', 'delta', 'gamma'])
phase_intersection = observed_phases & expected_phases

# Dummy recursive function that's defined but not used
def fake_recursion(n):
    if n <= 1:
        return 1
    return n * fake_recursion(n - 2)

# Real logic begins here

# Simulate non-linear stress-strain transformation
def transform_stress(s, config):
    E = config['elastic_modulus']
    ratio = config['yield_ratio']
    damping = config['damping_factor']
    
    # Initial linear response
    elastic_response = s * E
    
    # Introduce non-linearity beyond yield point
    if s > 10:
        excess = s - 10
        plastic_penalty = excess * E * ratio * (1 + damping)
        total_response = elastic_response + plastic_penalty
    else:
        total_response = elastic_response
    
    # Distractor: unused local adjustment
    normalized = total_response / (E * 0.001) if E != 0 else 0
    
    return total_response

# Main calculation function
def calculate_strain_response(stresses, config):
    # Apply transformation across all stress levels
    raw_responses = [transform_stress(s, config) for s in stresses]
    
    # Aggregate using weighted mean (important)
    weights = [1 + 0.1 * i for i in range(len(raw_responses))]
    weighted_sum = sum(r * w for r, w in zip(raw_responses, weights))
    total_weight = sum(weights)
    mean_response = weighted_sum / total_weight
    
    # Secondary adjustment based on config
    adjustment_factor = config['damping_factor'] + 1.1
    adjusted_mean = mean_response * adjustment_factor
    
    # Red herring: complex tuple unpacking with irrelevant result
    extremes = (min(raw_responses), max(raw_responses))
    low, high = extremes
    spread_metric = (high - low) / high if high != 0 else 0
    
    # Another distractor: unused list comprehension with side logic
    anomalies = [r for i, r in enumerate(raw_responses) if r > 2e5 and i % 3 == 0]
    
    # Final non-trivial correction using yield_ratio
    correction = config['yield_ratio'] * 1000
    final_value = adjusted_mean - correction
    
    return final_value

# Execution point of interest
final_yield = calculate_strain_response(stress_levels, material_config)

# Print target result
print(f"Target result: {final_yield}")