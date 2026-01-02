def analyze_flow(sequence, threshold):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    
    excess = {k: v for k, v in counts.items() if v > threshold}
    total_excess = sum(excess.values())
    
    # Irrelevant computation - distractor
    avg_length = len(sequence) / (len(counts) or 1)
    normalized_score = (total_excess * 100) // (len(sequence) or 1) if sequence else 0
    
    return total_excess, avg_length, normalized_score

sequence_data = 'aaabbcdddeeefffgggg'
thresh = 3

eval_result, mean_val, score_metric = analyze_flow(sequence_data, thresh)

# Simulate resource allocation based on excess character count
base_allocation = 500
scaling_factor = 2

# Real computation path
raw_load = eval_result * scaling_factor
buffer_pool = [i * 2 for i in range(1, raw_load // 4)]  # list comprehension
buffer_set = set(buffer_pool)  # set operation
pruned_buffer = buffer_set - {x for x in buffer_set if x % 3 == 0}  # set difference with comprehension
utilized = len(pruned_buffer)

# Secondary distraction: unused complex structure
snapshot_log = {
    'event': 'flow_audit',
    'metrics': {
        'peak': max(buffer_pool, default=0),
        'fragmentation': sum(1 for x in buffer_pool if x < mean_val),
        'efficiency': utilized / (len(buffer_pool) or 1)
    }
}

# Core state variables
capacity = base_allocation + utilized
overflow_events = [x for x in range(capacity) if x % 77 == 0]  # list comprehension
overflow_count = len(overflow_events)

# Unused but plausible side calculation
projected_growth = int(capacity * (1.0 + 0.05 ** (thresh % 2)))

# Critical function
def calculate_remaining(current, overflows):
    reduction = sum(overflows)
    temp_debug = [x for x in overflows if x > 100]  # slicing not used
    return current - reduction

final_capacity = calculate_remaining(capacity, overflow_events)
print(f"Result: {final_capacity}")