from itertools import combinations

# Simulate a network flow analysis with validation checks
nodes = [3, 7, -2, 5, -8, 4, 6]
weights = [1.1, 0.9, 1.5, 0.7, 1.2, 0.8, 1.0]
dummy_tracker = {i: 0 for i in range(len(nodes))}

# Irrelevant pre-processing: shuffle signs based on index parity (not used later)
sign_flipped = []
for idx, val in enumerate(nodes):
    if idx % 2 == 0:
        sign_flipped.append(-val)
    else:
        sign_flipped.append(val)

# Compute weighted contributions (semi-relevant but overridden later)
weighted_values = []
for val, weight in zip(nodes, weights):
    weighted_values.append(val * weight)

# Real logic begins: find all 3-node subsets with positive sum
valid_triplets = 0
for triplet in combinations(range(len(nodes)), 3):
    if sum(nodes[i] for i in triplet) > 0:
        valid_triplets += 1

# Secondary distraction: count magnitude transitions
magnitude_shifts = 0
for i in range(1, len(nodes)):
    if abs(nodes[i]) > 2 * abs(nodes[i-1]):
        magnitude_shifts += 1

# Core state computation
activation_count = 0
for val in nodes:
    if val > 0:
        activation_count += 1

# Distractor: unused helper list
status_flags = ['high' if w > 0.9 else 'low' for w in weights]

# Compute net flow using only positive node values scaled by activation
net_positive = sum(v for v in nodes if v > 0)
net_negative = sum(v for v in nodes if v < 0)
baseline_adjustment = len(nodes) - activation_count

# Key interference: complex conditional that doesn't affect final logic
if valid_triplets > 15:
    temp_offset = magnitude_shifts * 2
else:
    temp_offset = -1

# Final computation chain
raw_flow = net_positive + net_negative
scaled_flow = raw_flow * 1.5
threshold = 5.0

# Critical statement with answer determination
equilibrium_score = net_flow if abs(net_flow) > threshold else baseline_adjustment

# Correction: actually use computed scaled_flow as net_flow was undefined
net_flow = round(scaled_flow, 2)
equilibrium_score = net_flow if abs(net_flow) > threshold else baseline_adjustment

print(f"Result: {equilibrium_score}")