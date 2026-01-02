def analyze_productivity(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_accumulator = 0
    efficiency_map = {}
    
    for idx, entry in enumerate(logs):
        if not entry.get('active', False):
            continue
            
        raw_value = entry['value'] % 7  # modular arithmetic
        adjusted = (raw_value * (idx + 1)) // 2
        
        if idx % 3 == 0:
            adjusted += 2
        
        temp_accumulator += adjusted
        efficiency_map[idx] = adjusted

    average_temp = temp_accumulator / max(total_entries // 2, 1)
    return temp_accumulator, average_temp, efficiency_map


def compute_baseline_reference(data):
    # Irrelevant computation path (dead helper)
    base = 0
    for item in data:
        base += len(str(item))
    return base

logs_data = [
    {'value': 15, 'active': True},
    {'value': 22, 'active': False},
    {'value': 8, 'active': True},
    {'value': 31, 'active': True},
    {'value': 44, 'active': False}
]

# Key intermediate variables with distractions
summary_stats = []
for i, log in enumerate(logs_data):
    if log['active']:
        summary_stats.append((i, log['value'] % 5))

# Distractor: unused grouping logic
grouped = {}
for i, val in summary_stats:
    key = i % 4
    grouped[key] = grouped.get(key, 0) + val

# Core processing chain
raw_total, avg_hint, efficiency_tracker = analyze_productivity(logs_data)

scaling_factor = 1.5
offset_buffer = sum([v % 4 for v in efficiency_tracker.values()])  # semi-relevant

# Simulate multiple assignment and destructuring
task_metrics, _, used_map = analyze_productivity(logs_data)
efficiency_factor = 0

for k, v in used_map.items():
    efficiency_factor += v * (k + 1)

# Additional distraction: string manipulation not affecting result
log_ids = [f"entry_{i}" for i in range(len(logs_data))]
mapped_names = list(zip(log_ids, [d['value'] for d in logs_data]))
dummy_checksum = sum(ord(c) for name, _ in mapped_names for c in name[:3]) % 99

# Critical evaluation function with nested logic
def evaluate_performance(metrics, factor):
    base = metrics % 100
    boost = factor // 10
    penalty = 0
    
    # Nested conditionals (2-3 levels)
    if boost > 20:
        if base > 50:
            penalty = 5
        else:
            penalty = 3
    elif boost > 10:
        if base < 30:
            penalty = 2
    else:
        penalty = 1
    
    intermediate = (base + boost - penalty) * scaling_factor
    
    # Use of enumerate in final aggregation
    extra_mod = 0
    for j, (idx, val) in enumerate(used_map.items()):
        if j % 2 == 0:
            extra_mod += val % 3
    
    return int(intermediate + extra_mod)

# Final computation step
final_score = evaluate_performance(task_metrics, efficiency_factor)

print(f"Result: {final_score}")