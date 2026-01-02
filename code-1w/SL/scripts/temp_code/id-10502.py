def analyze_component(signal, threshold=0.5):
    """Irrelevant signal analysis function (dead code path)."""
    if len(signal) == 0:
        return 0
    avg = sum(signal) / len(signal)
    return avg * 0.7 if avg > threshold else avg * 0.3

# Irrelevant data structures and computations
dummy_logs = [{'time': t, 'event': 'ping', 'value': (t * 1.7) % 1} for t in range(10)]
extraneous_matrix = [[i*j + 0.1 for j in range(5)] for i in range(5)]
scaling_factor = 2.3
offset_correction = -0.5

# Real computational components
status_weights = {'active': 3, 'standby': 1, 'idle': 0, 'fault': -5}

def transform_sequence(seq):
    """Apply transformation with slicing and conditional logic."""
    if len(seq) < 3:
        return seq
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]
    # Slice-based manipulation
    transformed = [x * 2 for x in left] + [x + 1 for x in right]
    return [y for y in transformed if y > 0]

def recursive_reduce(data_list, depth=0):
    """Recursively reduce list using alternating operations."""
    if depth >= 3 or len(data_list) == 1:
        return data_list[0] if data_list else 0
    
    new_list = []
    for i in range(0, len(data_list) - 1, 2):
        op_val = data_list[i] * data_list[i+1] if depth % 2 == 0 else data_list[i] + data_list[i+1]
        new_list.append(op_val)
    
    if len(data_list) % 2 == 1:
        new_list.append(data_list[-1])
    
    return recursive_reduce(new_list, depth + 1)

# Decoy function that looks important but isn't used in main path
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    import math
    return -sum(p * math.log(p) for p in probs)

# Core state tracking variables
current_state = 'active'
state_history = ['init', 'boot', 'ready', current_state]

# Benchmark-related data (used)
benchmark_data = {
    'base_cycles': [4, 8, 15, 16, 23, 42],
    'flags': [True, False, True, True],
    'modes': {'fast': 2, 'normal': 1, 'eco': 0.7}
}

# Performance metrics (key input)
metrics = [
    {'type': 'latency', 'value': 120, 'weight': 0.3},
    {'type': 'throughput', 'value': 85, 'weight': 0.5},
    {'type': 'consistency', 'value': 92, 'weight': 0.2}
]

# Misleading intermediate calculations
temp_aggregate = 0
for m in metrics:
    temp_aggregate += m['value'] * m['weight'] * 0.9  # Wrong formula (red herring)

snapshot_buffer = [10, 20, 30, 40, 50]
slice_offset = 2
sample_window = snapshot_buffer[slice_offset:slice_offset+3]  # [30, 40, 50]
window_avg = sum(sample_window) / len(sample_window)  # 40.0 — looks important

# Real evaluation logic
status_flag = status_weights[current_state]

def evaluate_performance(met, bdata):
    base_result = 0
    for entry in met:
        contribution = entry['value'] * entry['weight']
        base_result += contribution
    
    cycle_sum = sum(bdata['base_cycles'])
    flag_bonus = 10 if all(bdata['flags']) else 5
    mode_scale = bdata['modes']['fast']
    
    # Apply transformation to a derived sequence
    raw_seq = [cycle_sum % 100, len(met), flag_bonus]
    processed_seq = transform_sequence(raw_seq)
    
    # Recursive reduction on processed sequence
    reduced_value = recursive_reduce(processed_seq) if processed_seq else 0
    
    # Final composition
    intermediate = base_result + reduced_value
    final = intermediate * mode_scale + status_flag
    
    # Dead branch — never executed due to constant
    if False and 'debug' in bdata:
        final *= 0.5
    
    return final

# Key execution point
eval_snapshot = benchmark_data['base_cycles'][1:4]  # [8, 15, 16]
final_score = evaluate_performance(metrics, benchmark_data)
print(f"Target result: {final_score}")