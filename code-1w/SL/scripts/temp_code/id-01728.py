from itertools import combinations
from functools import reduce

# Simulate thermodynamic state analysis with interference

def evaluate_stability(temp, pressure):
    return (temp > 300) and (pressure < 50)

# Irrelevant helper: calculates molecular variance (not used in final result)
def compute_molecular_variance(sequence):
    base_values = [hash(str(s)) % 100 for s in sequence]
    mean = sum(base_values) / len(base_values)
    return sum((x - mean) ** 2 for x in base_values) / len(base_values)

# Core logic: determine valid phase transitions
def generate_phase_pairs(elements):
    pairs = list(combinations(elements, 2))
    filtered = [p for p in pairs if (p[0] + p[1]) % 3 != 0]  # arbitrary filter
    return filtered

# Misleading function that appears important but is unused
def deprecated_flow_integral(x):
    total = 0
    for i in range(1, x + 1):
        total += i * (i % 7)
    return total

# Main calculation engine
def calculate_entropy_subset(items):
    entropy = 0
    for item in items:
        if isinstance(item, tuple) and len(item) == 2:
            entropy += item[0] * item[1]
    return max(entropy, 1)

# Critical function: computes net energy flux based on state regimes
def calculate_net_flow(states, pressures):
    # Step 1: Extract high-energy states
    active_states = [s for s in states if s[1] > 40]
    
    # Step 2: Determine stable configurations
    stable_mask = [evaluate_stability(s[0], p) for s, p in zip(active_states, pressures)]
    
    # Step 3: Compute base contribution using lambda reduction
    base_contrib = reduce(lambda acc, x: acc + x[0] // 10, active_states, 0)
    
    # Step 4: Apply pressure modulation (only even-indexed ones matter)
    modulated = sum([p * (i % 2 + 1) for i, p in enumerate(pressures) if i % 3 != 2])
    
    # Step 5: Combine via entropy-weighted factor
    pair_list = generate_phase_pairs([1, 2, 3, 4, 5])
    entropy_factor = calculate_entropy_subset(pair_list)
    
    # Step 6: Final net flux computation
    net = base_contrib * modulated // entropy_factor
    
    # Distractor variables below
    dummy_sequence = [(1,2), (3,4), (5,6)]
    temp_debug = [compute_molecular_variance(dummy_sequence)] * 3
    
    return net

# Input data setup
thermal_states = [(350, 45), (400, 60), (250, 30), (420, 80), (380, 42)]
pressure_regimes = [20, 65, 35, 90, 48]

# Execution point of interest
net_flux = calculate_net_flow(thermal_states, pressure_regimes)

# Print target result
print(f"Result: {net_flux}")