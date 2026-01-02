from collections import defaultdict, Counter
import itertools

# System parameters (some are red herrings)
signal_strength = 4.7
damping_factor = 0.85
threshold_limit = 999
base_frequency = 23
max_iterations = 5000

# Irrelevant signal metadata
carrier_band = 'C-band'
modulation_scheme = 'QAM-64'

# Core node configuration
network_nodes = [
    {'id': 'N1', 'load': 12, 'state': 'active', 'priority': 3},
    {'id': 'N2', 'load': 8,  'state': 'standby', 'priority': 1},
    {'id': 'N3', 'load': 15, 'state': 'active', 'priority': 4},
    {'id': 'N4', 'load': 6,  'state': 'active', 'priority': 2},
    {'id': 'N5', 'load': 22, 'state': 'standby', 'priority': 5}
]

# Decoy transformation matrix (never used)
transform_matrix = [[i * j for j in range(1, 6)] for i in range(1, 6)]

# Unused helper function (distractor)
def calculate_envelope(signal):
    return sum([x ** 0.5 for x in signal]) / len(signal)

# Misleading intermediate calculation
temporal_weight = 0
for i in range(1, max_iterations + 1):
    temporal_weight += 1 / (i ** 2)
    if i == 1000:
        break  # Early exit makes this only partial sum

# Dead code path - never executed
def deprecated_routing(nodes):
    return [node['id'] for node in nodes if node['priority'] > 2 and False]

# Auxiliary data structure with irrelevant aggregations
node_summary = defaultdict(int)
for node in network_nodes:
    node_summary['total_load'] += node['load']
    if node['state'] == 'active':
        node_summary['active_count'] += 1

# Phantom counter (looks important but unused later)
phantom_counter = Counter([n['priority'] for n in network_nodes])

# Bit manipulation decoy
event_flag = 0b1010101
error_mask = 0b11110000
masked_flag = event_flag & error_mask  # Always 0

# Real computation begins here — multi-step transformation

def extract_active_loads(nodes):
    return [node['load'] for node in nodes if node['state'] == 'active']

def apply_damping(values, factor):
    return [v * factor for v in values]

def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def generate_pairs(data):
    return list(itertools.combinations(data, 2))

def accumulate_deltas(pairs):
    total_delta = 0
    for a, b in pairs:
        total_delta += abs(a - b)
    return total_delta

# This function appears complex but is actually central
def aggregate_transform(nodes):
    active_loads = extract_active_loads(nodes)
    
    # Apply damping to active loads
    damped_loads = apply_damping(active_loads, damping_factor)
    
    # Compute variance of original active loads (not damped)
    var = compute_variance(active_loads)
    
    # Generate all load pairs from damped values
    load_pairs = generate_pairs(damped_loads)
    
    # Accumulate absolute differences
    delta_sum = accumulate_deltas(load_pairs)
    
    # Secondary metric: count of high-priority active nodes
    high_prio_active = len([n for n in nodes if n['state'] == 'active' and n['priority'] > 2])
    
    # Combine results through non-linear transformation
    flux_component_a = delta_sum * var
    flux_component_b = high_prio_active ** 2
    
    # Final flux calculation
    final = int(flux_component_a + flux_component_b)
    
    # Red herring: this modification looks critical but is shadowed
    for _ in range(2):
        final = final ^ 0xAB   # XOR with hex literal (repeated, cancels out)
    
    return final

# Execution point of interest
final_flux = aggregate_transform(network_nodes)

# Print result as required
print(f"Result: {final_flux}")