from itertools import permutations, cycle
import math

def analyze_pattern(sequence):
    # Irrelevant analysis function (dead code path)
    return sum(a * b for a, b in enumerate(sequence)) % 7

def generate_offsets(base, depth):
    # Distractor function: generates unused offsets
    return [base ** i % 13 for i in range(depth)]

def validate_consistency(node_data):
    # Misleading validation that isn't used in final computation
    total = 0
    for key, val in node_data.items():
        if val > 30:
            total += len(str(val))
    return total % 5 == 0

def calculate_tension(chain):
    # Another red herring: complex but unused tension calculator
    acc = 0
    for i, c in enumerate(chain):
        acc += ord(c) ^ (i * 17)
    return acc // 7

def calculate_equilibrium(network, nodes):
    # Core relevant logic with embedded distractions
    
    # Irrelevant preprocessing
    temp_cache = {n: (n * 19 + 7) % 101 for n in nodes}
    buffer_zone = [0] * 5
    for i in range(len(buffer_zone)):
        buffer_zone[i] = (i ** 2) & 15
    
    # Real data transformation
    flux = []
    for k in sorted(nodes):
        if k in network:
            raw_val = network[k]
            # Non-linear transformation
            transformed = math.log(abs(raw_val) + 1) * 3.2
            if transformed > 10:
                transformed = 10
            flux.append(transformed)
    
    # Complex conditional expression
    scaling_factor = 2.5 if len(flux) > 3 else (1.8 if sum(flux) < 15 else 3.1)
    
    # Use of itertools: cycle for wrapping access
    cyclic_flux = cycle(flux)
    sampled = [next(cyclic_flux) for _ in range(len(flux) + 2)]
    
    # Actual equilibrium formula
    weighted_sum = 0.0
    for idx, val in enumerate(sampled):
        weight = math.sin(idx + 0.5)
        weighted_sum += val * weight
    
    # Final adjustment using permutation side-effect (only length matters)
    key_perms = list(permutations([1, 2, 3]))  # 6 permutations
    adjustment = len(key_perms) / 2.0  # = 3.0
    
    result = weighted_sum + adjustment
    return round(result, 4)

# --- Main Execution ---

# Simulated sensor network data (mixed types to distract)
flow_map = {
    5: 42,
    3: 18,
    8: 95,
    1: 6,
    7: 53
}

pressure_nodes = [3, 5, 7, 8]  # Used in calculation

# Dead assignments - irrelevant variables
baseline_ref = [analyze_pattern([4, 8, 15, 16])]
dummy_hash = calculate_tension("checkpoint_Z")
offset_list = generate_offsets(5, 8)
consistency_flag = validate_consistency(flow_map)

# Key statement
equilibrium_score = calculate_equilibrium(flow_map, pressure_nodes)

# Output result
print(f"Result: {equilibrium_score}")