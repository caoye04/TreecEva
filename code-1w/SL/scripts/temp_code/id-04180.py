import math

# Irrelevant helper function (dead code path)
def calculate_entropy(data):
    return -sum(p * math.log2(p) for p in data if p > 0)

# Misleading intermediate computation
temp_calibration = [i ** 2 for i in range(15) if i % 3 == 0]
decoys = {f'key_{i}': i * 1.5 for i in range(10)}

# Core data structures with distractors
event_sequence = [1, 0, 1, 1, 0, 1, 0, 0, 1]
weights = [0.5, 1.2, -0.3, 0.8, 1.1, -0.7, 0.4, 0.9, -0.2]

# Unused transformation matrix
transform_matrix = [[i + j for j in range(9)] for i in range(9)]

# Simulated sensor nodes with metadata
network_nodes = [
    {'id': 'A1', 'type': 'input', 'value': 3.1, 'active': True},
    {'id': 'B2', 'type': 'relay', 'value': 2.7, 'active': True},
    {'id': 'C3', 'type': 'input', 'value': 1.4, 'active': False},
    {'id': 'D4', 'type': 'relay', 'value': 0.9, 'active': True},
    {'id': 'E5', 'type': 'input', 'value': 4.2, 'active': True}
]

# Red herring: complex-looking but unused bit manipulation
def obfuscate_key(x):
    x = (x ^ 0xABCDEF) & 0xFFFF
    x = ((x << 3) | (x >> 13)) & 0xFFFF
    x = (x * 0x9E37) & 0xFFFF
    return x

obfuscated_codes = [obfuscate_key(i * 17) for i in range(1, 6)]

# Real processing begins here
active_values = []
for node in network_nodes:
    if node['type'] == 'input' and node['active']:
        active_values.append(node['value'])

# Secondary data from event sequence
triggered_indices = []
for idx, event in enumerate(event_sequence):
    if event == 1:
        triggered_indices.append(idx)

# Combine using zip and enumerate (required python features)
combined_signals = []
for i, idx in enumerate(triggered_indices):
    if idx < len(weights):  # Prevent index error
        combined_signals.append(active_values[i % len(active_values)] * weights[idx])

# Accumulation with conditional adjustment
signal_sum = 0
for i, val in enumerate(combined_signals):
    if i % 2 == 0:
        signal_sum += val * 1.1
    else:
        signal_sum += val * 0.9

# Decoy accumulation (misleading intermediate result)
dummy_accum = 0
for x in temp_calibration:
    dummy_accum += x // 2

correction_factor = math.sin(math.pi / 6)  # 0.5

# Real transform function
def aggregate_transform(nodes, w):
    base_vals = [node['value'] for node in nodes if node['type'] == 'input']
    weighted_sum = sum(base_vals[i] * w[i*2 % len(w)] for i in range(len(base_vals)))
    count_active_inputs = len([n for n in nodes if n['type'] == 'input' and n['active']])
    penalty = count_active_inputs * 0.25
    return int((weighted_sum - penalty) * correction_factor)

# Critical execution point
final_flux = aggregate_transform(network_nodes, weights)

# Print required output
print(f"Result: {final_flux}")