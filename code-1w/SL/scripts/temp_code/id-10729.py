import itertools

def calculate_potential_energy(state):
    return sum(x ** 2 for x in state) - 2 * state[0] * state[-1]

def generate_perturbations(base_state, level=1):
    perturbations = []
    for i in range(len(base_state)):
        new_state = base_state[:]
        new_state[i] += level
        perturbations.append(new_state)
    return perturbations

def calculate_entropy(state):
    magnitude = sum(abs(x) for x in state)
    if magnitude == 0:
        return 0.0
    return round(magnitude * 0.5, 3)

def is_stable_configuration(state):
    return all(abs(state[i] - state[i-1]) <= 2 for i in range(1, len(state)))

def calculate_equilibrium(states):
    filtered = [s for s in states if is_stable_configuration(s)]
    
    # Irrelevant helper function (dead code path)
    def unused_normalization(data):
        max_val = max(max(vec) for vec in data)
        return [[x / max_val for x in vec] for vec in data]
    
    scores = []
    for state in filtered:
        energy = calculate_potential_energy(state)
        entropy = calculate_entropy(state)
        # Weighted combination
        score = energy - 3 * entropy
        scores.append(score)
    
    # Distractor variables
    temp_analysis = [s for s in scores if s > -10]
    baseline = len(filtered) * 1.5 if filtered else 0
    adjustment_factor = 0.8 if len(scores) > 2 else 1.0
    
    final_score = sum(scores) * adjustment_factor + baseline
    
    return int(round(final, 0))

# Main execution block
initial_state = [1, -2, 0, 3]

# Generate extended state space
all_states = [initial_state]
for p in generate_perturbations(initial_state, 1):
    all_states.append(p)

for p in generate_perturbations(initial_state, -1):
    all_states.append(p)

# Add some duplicate-like states with minor variation
all_states.append([1, -1, 0, 3])
all_states.append([1, -2, 1, 3])

# Irrelevant transformation (not used later)
transformed = list(map(lambda x: [y * 0.9 for y in x], all_states))

# State categorization (semi-relevant but not critical)
categorized = {"high": [], "low": []}
for s in all_states:
    if sum(s) > 0:
        categorized["high"].append(s)
    else:
        categorized["low"].append(s)

# Critical computation
thermodynamic_states = all_states  # Used in function call

# Additional distractor: unused intermediate
aggregated_stats = {
    "total_configs": len(all_states),
    "avg_length": len(all_states[0]),
    "max_energy": max(calculate_potential_energy(s) for s in all_states)
}

equilibrium_score = calculate_equilibrium(thermodynamic_states)
print(f"Result: {equilibrium_score}")