import itertools

# System health monitoring simulation with diagnostic computation

def analyze_node(node_data, threshold=0.75):
    weighted_sum = sum(x * 0.1 for x in node_data)  # Irrelevant smoothing
    return sum(node_data) > threshold * len(node_data)


def generate_signature(sequence):
    # Complex but ultimately unused signature generator (red herring)
    base_sig = 1
    for val in sequence:
        base_sig = (base_sig * (val + 1)) % 997
    return base_sig

# Simulated sensor grid readings
sensor_grid = [
    [0.8, 0.9, 0.7, 0.6],
    [0.5, 0.4, 0.3, 0.2],
    [0.7, 0.8, 0.9, 1.0],
    [0.1, 0.2, 0.3, 0.4]
]

# Misleading preprocessing path (dead code)
filtered_grid = []
for row in sensor_grid:
    filtered_row = [x for x in row if x > 0.5]  # Not actually used later
    filtered_grid.append(filtered_row)

# Unused transformation using itertools (distractor)
diagonal_shifts = list(itertools.accumulate([1, -1, 1, -1]))

# Core diagnostics - relevant logic
node_status = [analyze_node(row, 0.65) for row in sensor_grid]

# Simulated system state flags (mixed relevant/irrelevant)
system_state = {
    'active_nodes': sum(1 for x in node_status if x),
    'overload_check': False,
    'last_updated': '2023-12-05',  # Irrelevant metadata
    'version': '3.7.1'  # Distractor constant
}

# Auxiliary function not directly contributing to result
def compute_variance(data_list):
    mean = sum(data_list) / len(data_list)
    return sum((x - mean) ** 2 for x in data_list) / len(data_list)

# Nested conditional structure with decoy branches
event_log = []
if system_state['active_nodes'] > 2:
    event_log.append('STATUS_OK')
    temp_aggregate = []
    for i, row in enumerate(sensor_grid):
        if node_status[i]:
            # Actual contribution path
            processed = [x for x in row if x > 0.25]  # List comprehension (required)
            temp_aggregate.extend(processed)
    
    # Decoy branch with complex unused calculation
    if len(temp_aggregate) % 2 == 0:
        mirrored = [temp_aggregate[-i] for i in range(1, len(temp_aggregate))]
        # This branch does nothing useful

    # Real metric computation
    raw_total = sum(temp_aggregate)
    adjustment_factor = len(temp_aggregate) / 10.0
    adjusted_total = raw_total * adjustment_factor

    # Multiple intermediate variables (some irrelevant)
    baseline_ref = 2.5
    offset_correction = baseline_ref * 0.1  # Unused

    # Critical statement: this determines the answer
    final_diagnostic = adjusted_total - 1.5  # Key line

else:
    # Dead fallback branch (never reached due to input design)
    final_diagnostic = -999
    event_log.append('CRITICAL_DOWNGRADE')

# Additional red herring: unused aggregation over transposed grid
transposed = list(zip(*sensor_grid))
symmetry_score = sum(abs(row[0] - row[-1]) for row in transposed)

# Another decoy function call with no side effects
generate_signature([int(x*10) for x in sensor_grid[0]])

# Final output - must print result
print(f"Result: {final_diagnostic}")