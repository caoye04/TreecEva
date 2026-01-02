import itertools

# System calibration parameters (irrelevant to final result)
def calibrate_sensor(x):
    return (x * 0.987) + 2.1

def deprecated_normalization(arr):
    total = sum(arr)
    return [a / total for a in arr] if total != 0 else arr

# Misleading signal processing chain
def compute_harmonic_score(values):
    if len(values) == 0:
        return 0
    inv_sum = sum(1 / v for v in values if v != 0)
    return len(values) / inv_sum if inv_sum != 0 else 0

# Irrelevant data structure transformation
def rotate_grid(grid):
    return [list(reversed(col)) for col in zip(*grid)]

# Dummy recursive depth tracker (dead code path)
def track_recursion_depth(n, depth=0):
    if n <= 1:
        return depth
    return track_recursion_depth(n // 2, depth + 1)

# Decoy function using bitwise manipulation (not used in main logic)
def obfuscate_key(n):
    n ^= 0xFF
    n = (n << 1) & 0xFF | (n >> 7)
    return n ^ 0x5A

# Real computation begins here — network node transformation
network_nodes = [
    {'id': 1, 'load': 12, 'active': True, 'tier': 'A'},
    {'id': 2, 'load': 8,  'active': False, 'tier': 'B'},
    {'id': 3, 'load': 15, 'active': True, 'tier': 'A'},
    {'id': 4, 'load': 22, 'active': True, 'tier': 'C'},
    {'id': 5, 'load': 5,  'active': True, 'tier': 'B'}
]

# Irrelevant tier mapping (distractor)
tier_weights = {'A': 1.5, 'B': 1.2, 'C': 1.0}
adjusted_scores = []
for node in network_nodes:
    raw_score = node['load'] * tier_weights.get(node['tier'], 1.0)
    adjusted_scores.append(raw_score * 0.85)

# Unused intermediate calculation (misleading)
avg_adjusted = sum(adjusted_scores) / len(adjusted_scores) if adjusted_scores else 0

# Core logic hidden among distractors
def filter_active_nodes(nodes):
    return [n for n in nodes if n['active']]

def extract_loads(nodes):
    return [n['load'] for n in nodes]

def apply_exponential_decay(lst):
    return [val * (0.9 ** i) for i, val in enumerate(lst)]

def aggregate_transform(nodes):
    # Step 1: Filter only active nodes
    active_nodes = filter_active_nodes(nodes)
    
    # Step 2: Extract their loads
    loads = extract_loads(active_nodes)
    
    # Step 3: Sort in descending order
    sorted_loads = sorted(loads, reverse=True)
    
    # Step 4: Take top 3 using slicing (key operation)
    top_three = sorted_loads[:3]
    
    # Step 5: Apply exponential decay based on position
    decaying_values = apply_exponential_decay(top_three)
    
    # Step 6: Use itertools to generate pairwise products
    pairs = list(itertools.combinations(decaying_values, 2))
    
    # Step 7: Sum all pairwise products
    interaction_sum = sum(a * b for a, b in pairs)
    
    # Step 8: Add sum of original top three for final flux
    final_component = interaction_sum + sum(top_three)
    
    return final_component

# Secondary decoy: unused complex dictionary reduction
def reduce_node_map(node_list):
    acc_map = {}
    for node in node_list:
        t = node['tier']
        acc_map[t] = acc_map.get(t, 0) + node['load']
    return {k: v * 1.1 for k, v in acc_map.items()}

# Fake initialization sequence
initial_sync_flag = True
sync_counter = 0
while initial_sync_flag and sync_counter < 3:
    sync_counter += 1
    initial_sync_flag = False

# Trigger real computation
baseline_reference = [n['load'] for n in network_nodes if n['tier'] == 'A' and n['active']]
reference_magnitude = sum(baseline_reference)

# Key execution point
final_flux = aggregate_transform(network_nodes)

# Print result as required
print(f"Target result: {final_flux}")