def calculate_entropy(values):
    """Dummy function to distract from main logic"""
    if len(values) == 0:
        return 0.0
    total = sum(x * x for x in values)
    return total / len(values) if total > 10 else total + 5

# Simulate quantum state transitions
def generate_state_sequence(n):
    sequence = []
    a, b = 1, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b  # Fibonacci-like progression
    return sequence

# Determine parity clusters
def cluster_parities(data):
    even_cluster = [x for x in data if x % 2 == 0]
    odd_cluster = [x for x in data if x % 2 == 1]
    return {'even': even_cluster, 'odd': odd_cluster}

# Main calculation function
def calculate_equilibrium(states):
    # Transform states using modular arithmetic
    transformed = [state % 7 for state in states]
    
    # Filter active states
    active_states = [t for t in transformed if t != 0]
    
    # Compute cumulative interference
    interference = 0
    for i, val in enumerate(active_states):
        interference += val * (i + 1)
    
    # Calculate combinatorial factor based on length
    n = len(active_states)
    combinations = 1
    for i in range(min(n, 4)):
        combinations *= (n - i)
    combinations = combinations // 24 if n >= 4 else combinations // max(1, n)
    
    # Apply conditional adjustment
    adjustment = 3 if n > 5 else 2
    
    # Key computation
    base_score = interference + combinations
    final_score = base_score // adjustment if base_score > 20 else base_score * adjustment
    
    # Distractor: unused entropy calculation
    entropy_proxy = calculate_entropy(active_states)
    
    return final_score

# Initialize simulation parameters
initial_seed = 8
max_iterations = 12

# Generate energy state sequence
raw_sequence = generate_state_sequence(max_iterations)

# Apply initial filtering
filtered_energy = [x for x in raw_sequence if x % 3 != 0]

# Add dummy transformation (irrelevant to final result)
dummy_transform = [x ** 0.5 for x in filtered_energy if x > 5]

# Assign final energy states
energy_states = [e + 1 for e in filtered_energy]

# Perform clustering (not used later, but looks important)
clusters = cluster_parities(energy_states)

# Introduce misleading metric
misleading_index = sum(x % 5 for x in energy_states) / len(energy_states)

# Core computation point
equilibrium_score = calculate_equilibrium(energy_states)

# Output result
print(f"Result: {equilibrium_score}")