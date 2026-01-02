import itertools

# Irrelevant helper function (decoy)
def normalize_signal(data):
    return [x / sum(data) for x in data]

# Another decoy function with misleading intermediate calculations
def compute_entropy(arr):
    total = 0
    for x in arr:
        if x > 5:
            total += x * 0.3
        else:
            total -= x * 0.1
    return round(total, 4)

# Core physics simulation parameters (some are red herrings)
base_frequency = 42.5
modulation_index = 17
reference_phase = 987

# Real input data
pressure_nodes = [3, 7, 15, 31, 63]
flow_sequence = [1, 2, 4, 8, 16]

# Distractor: unused but plausible-looking transformation
echo_chain = [2**i for i in range(5)]
damping_factor = sum(echo_chain) / len(echo_chain)

# Misleading intermediate array (never used in final calculation)
stress_tensor = [[i + j for j in range(5)] for i in pressure_nodes]

# Early preprocessing that looks important but only a slice is used
temporal_buffer = []
for idx, val in enumerate(flow_sequence):
    if idx % 2 == 0:
        temporal_buffer.append(val * 2)
    else:
        temporal_buffer.append(val // 2)

temporal_buffer.append(999)  # Red herring value

# Actual relevant slicing operation
active_flow = flow_sequence[:4]  # Uses slicing — key python feature

# Bit manipulation decoy chain
bit_noises = []
for p in pressure_nodes:
    bit_noises.append(p ^ 255 & 15)

# Real logic embedded within distractions
def calculate_diffusion(path, nodes):
    # Nested logic with multiple steps and early returns
    if len(path) < 3:
        return -1
    
    accumulated = 0
    for i in range(len(nodes)):
        if nodes[i] % 2 == 1:
            # Trigonometric distraction with meaningful core
            angle = path[i] if i < len(path) else 1
            delta = int(abs(32 * (nodes[i] / (angle + 1e-6))))
            accumulated += delta
        else:
            # Dead code path (never reached due to odd values in nodes)
            accumulated -= 100
            break
    
    # Additional transformation using itertools
    pairs = list(itertools.combinations([2, 3, 5], 2))
    multiplier = 1
    for a, b in pairs:
        multiplier *= (a + b)  # Computes (2+3)*(2+5)*(3+5) = 5*7*8 = 280
    
    # Final adjustment based on active_flow slice
    flow_sum = sum(active_flow)  # 1+2+4+8 = 15
    adjustment = flow_sum & 7  # 15 & 7 = 7 (bitwise AND)
    
    # Critical computation
    result = (accumulated * adjustment) // (multiplier + 1)  # Avoid division by zero
    
    # Early return alternative (not triggered)
    if result < 0:
        return 0
        
    return result

# Secondary irrelevant assignment
calibration_matrix = {i: base_frequency * i for i in range(7)}

# Key execution point
thermal_gradient = calculate_diffusion(flow_sequence, pressure_nodes)

# Print required output
print(f"Result: {thermal_gradient}")