import itertools

# System configuration constants (irrelevant to final result)
MAX_NODES = 256
BASE_LATENCY_MS = 12.5
VERSION_ID = 'NET_4.2'

# Core data structures
routing_table = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

priority_map = {'high': 3, 'medium': 2, 'low': 1}

# Irrelevant diagnostic counters
packet_loss_count = 0
retransmit_counter = [0] * 4
active_sessions = set()

# Decoy function - never called
def calculate_jitter(timestamps):
    if len(timestamps) < 2:
        return 0.0
    diffs = [abs(a - b) for a, b in zip(timestamps, timestamps[1:])]
    return sum(diffs) / len(diffs) if diffs else 0.0

# Unused transformation
shifted_matrix = [[(cell + 2) % 4 for cell in row] for row in routing_table]

# Priority flags (only some values are actually used later)
priority_flags = [3, 0, 2, 3]

# Nested routing structure with red herring dimensions
nested_routing = [
    [
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 1]
    ],
    [
        [1, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
]

# Dead code path - modifies unused variable
for i in range(len(shifted_matrix)):
    for j in range(len(shifted_matrix[i])):
        if shifted_matrix[i][j] == 2:
            shifted_matrix[i][j] = (shifted_matrix[i][j] + 1) % 4

# Decoy list comprehension with side-effect-free mutation
_ = [x for x in range(8) if x % 2 == 0 and routing_table[x % 4][x % 4] > 0]

# Auxiliary function that appears important but is only used once
def validate_route(route_matrix):
    for row in route_matrix:
        if sum(row) == 0:
            return False
    return True

# Complex multi-step preprocessing with distractors
expanded_routes = []
for layer in nested_routing:
    validated_layer = []
    for route in layer:
        # Simulate checksum (irrelevant)
        parity = sum(route) % 2
        extended = route + [parity]
        validated_layer.append(extended)
    expanded_routes.append(validated_layer)

# Generate all possible sub-paths (mostly unused)
all_combinations = list(itertools.product([0, 1], repeat=3))
path_signatures = [sum(combo) * 2 for combo in all_combinations if sum(combo) > 1]

# Real computation begins here - masked by prior noise
filtered_indices = [
    i for i, flag in enumerate(priority_flags) if flag >= 2
]

effective_routing = [
    nested_routing[i] for i in filtered_indices
]

# Intermediate aggregation with misleading operations
aggregated_masks = []
for cube in effective_routing:
    layer_sum = [0] * 3
    for plane in cube:
        for idx, val in enumerate(plane[:3]):
            layer_sum[idx] += val
    aggregated_masks.append(layer_sum)

# Bit manipulation decoy
checksum_flag = 0
for row in routing_table:
    for cell in row:
        checksum_flag ^= (cell << 1) | 1

# Actual throughput calculation (depends only on aggregated_masks)
def aggregate_throughput(masks, flags):
    total = 0.0
    weight_map = {3: 2.5, 2: 1.8, 1: 0.9}
    
    # Only indices 0 and 1 in flags matter due to filtering above
    relevant_weights = [weight_map[flags[i]] for i in range(len(flags)) if flags[i] >= 2]
    
    for i, mask in enumerate(aggregated_masks):
        # Throughput = weighted sum of active channels
        activity_score = sum(1 for x in mask if x > 0)
        channel_bonus = 1.2 if mask.count(1) >= 2 else 0.8
        total += activity_score * channel_bonus * relevant_weights[i]
    
    # Final adjustment based on structural redundancy
    flat = [cell for layer in masks for plane in layer for cell in plane]
    redundancy_factor = len(flat) / (len(set(flat)) + 1)
    return total * redundancy_factor

# Critical execution point
final_bandwidth = aggregate_throughput(nested_routing, priority_flags)

# Additional irrelevant operations after main computation
compression_ratio = 0.0
if len(expanded_routes) > 2:
    compression_ratio = len(str(expanded_routes)) / float(MAX_NODES)

# Logging of unused metrics
counter_stats = {
    'cycles': 12,
    'phase': 'steady',
    'valid': True
}

# Output the target result
Result: {final_bandwidth}