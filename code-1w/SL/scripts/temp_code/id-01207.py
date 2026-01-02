def analyze_performance(logs):
    total_ops = 0
    peak_utilization = 0
    for i, log in enumerate(logs):
        ops = log['operations']
        util = log['utilization']
        total_ops += ops
        if util > peak_utilization:
            peak_utilization = util
    return total_ops, peak_utilization

logs = [
    {'operations': 120, 'utilization': 0.65},
    {'operations': 180, 'utilization': 0.72},
    {'operations': 95, 'utilization': 0.58},
    {'operations': 210, 'utilization': 0.81}
]

# Irrelevant performance analysis (distractor)
operation_total, max_usage = analyze_performance(logs)
scaling_factor = operation_total / 1000.0
adjusted_scaling = scaling_factor * 1.15 if max_usage > 0.7 else scaling_factor

# Core system configuration (relevant)
efficiency_map = {0: 0.5, 1: 0.65, 2: 0.75, 3: 0.82, 4: 0.88}
units = [1, 3, 2, 3, 1, 4, 2]

# Misleading pre-computations (distractor)
unit_count = len(units)
avg_efficiency_guess = sum(efficiency_map[u] for u in set(units)) / len(set(units))
baseline_projection = unit_count * avg_efficiency_guess * 100

# Actual capacity calculation (key logic)
def calculate_system_capacity(unit_list, efficiency_lookup):
    capacity = 0
    temp_buffer = []
    for idx, unit in enumerate(unit_list):
        stage_modifier = 1 + (idx * 0.05)  # Increases slightly per position
        efficiency = efficiency_lookup[unit]
        contribution = efficiency * stage_modifier
        
        # Conditional boost for high-efficiency units at even indices
        if unit >= 3 and idx % 2 == 0:
            contribution *= 1.1
            
        capacity += contribution
        
        # Tracking intermediate values (semi-relevant)
        temp_buffer.append((idx, contribution))
    
    # Post-process with zip to pair adjacent contributions
    smoothed = 0
    for curr, nxt in zip(temp_buffer[:-1], temp_buffer[1:]):
        smoothed += (curr[1] + nxt[1]) * 0.01  # Minor adjustment
    
    return int(capacity * 100 + smoothed)  # Scale up for integer metric

# Execute main logic
final_capacity = calculate_system_capacity(units, efficiency_map)

# Additional distraction: unused data transformation
zipped_units = list(zip(units[::2], units[1::2]))
reindexed_map = {i: efficiency_map[u] for i, u in enumerate(units)}
duplicate_check = len(set(units)) < len(units)

Result: {final_capacity}