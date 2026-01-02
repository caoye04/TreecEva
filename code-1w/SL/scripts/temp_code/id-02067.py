import itertools

# System calibration constants (irrelevant to final result)
def calibrate_sensor(x):
    return (x * 1.05) - 3 if x > 10 else x + 2

def deprecated_normalization(arr):
    # Dead function - never called
    return [a / sum(arr) for a in arr]

# Irrelevant data transformation chain
temp_offsets = [1.2, 0.8, -0.5, 1.0]
adjusted_temps = []
for t in temp_offsets:
    adjusted_temps.append(round(t ** 2, 2))

# Unused symbolic mappings
symbol_table = {'A': 65, 'B': 66, 'C': 67}
symbol_checksum = sum(symbol_table.values()) % 17

# Real computation begins here: network node analysis
network_nodes = [
    {'id': 'N1', 'load': 12, 'active': True, 'flags': [1, 0, 1]},
    {'id': 'N2', 'load': 8,  'active': False, 'flags': [0, 1, 1]},
    {'id': 'N3', 'load': 15, 'active': True, 'flags': [1, 1, 0]},
    {'id': 'N4', 'load': 7,  'active': True, 'flags': [0, 0, 1]}
]

# Misleading intermediate: bit flag reduction (not used in final result)
node_signatures = []
for node in network_nodes:
    sig = 0
    for i, f in enumerate(node['flags']):
        sig |= (f << i)
    node_signatures.append(sig)

# Another red herring: string-based status encoding
status_map = {}
for node in network_nodes:
    status_str = f"{node['id']}-{node['active']}"
    hash_val = 0
    for c in status_str:
        hash_val += ord(c) * 31
    status_map[node['id']] = hash_val % 100

# Core logic disguised among distractions
working_nodes = [n for n in network_nodes if n['active']]

# Compute effective load using flag-weighted summation (actual relevant logic)
effective_loads = []
for node in working_nodes:
    weight = sum(node['flags']) + 1  # base weight of 1
    effective_loads.append(node['load'] * weight)

# Apply non-linear scaling via polynomial transform (key step)
scaled_loads = [x**2 - 2*x + 1 for x in effective_loads]

# Accumulation through cyclic pairwise combinations (itertools usage)
pairs = list(itertools.combinations(scaled_loads, 2))
aggregated_pairs = 0
for a, b in pairs:
    aggregated_pairs += (a + b) // 2

# Secondary distraction: unused recursive reducer
def recursive_reduce(lst):
    if len(lst) <= 1:
        return lst[0] if lst else 0
    return recursive_reduce([lst[i] + lst[i+1] for i in range(0, len(lst)-1, 2)])

# Final transformation chain with string manipulation decoy
flux_basis = aggregated_pairs

# String obfuscation layer (irrelevant)
trace_id = "FLX-{}-{}"
trace_parts = []
for i, load in enumerate(scaled_loads):
    trace_parts.append(trace_id.format(i, hex(int(load))[-2:]))

# Final aggregation with hidden offset
base_offset = len([n for n in network_nodes if not n['active']])  # count inactive
offset_factor = base_offset * 100

# Actual final flux calculation
intermediate_flux = flux_basis + offset_factor

# Key statement
final_flux = aggregate_transform(network_nodes)

# Definition of actual transform function (used above)
def aggregate_transform(nodes):
    active_only = [n for n in nodes if n['active']]
    total = 0
    for node in active_only:
        flag_sum = sum(node['flags'])
        # Complex but deterministic weighting
        contribution = (node['load'] + flag_sum) ** 2
        total += contribution
    # Add fixed adjustment based on system constants (hidden)
    adjustment = sum(temp_offsets) * 10  # uses earlier irrelevant array
    return int(total - adjustment)  # deterministic integer result

print(f"Result: {final_flux}")