def calculate_performance(tasks, overhead):
    base_throughput = sum([t['cycles'] for t in tasks])
    complexity_factor = len([t for t in tasks if t['type'] == 'compute'])
    scaling = 1.5 if complexity_factor > 2 else 1.0
    
    # Compute effective workload with scaling
    effective_work = base_throughput * scaling
    
    # Adjust for overhead using lambda-based penalty curve
    penalty_curve = lambda x: x ** 1.2
    adjusted_overhead = penalty_curve(overhead)
    
    # Conditional efficiency boost based on task profile
    efficiency_boost = 0.8 if any(t['priority'] > 7 for t in tasks) else 1.1
    
    # Final performance calculation
    raw_performance = (effective_work - adjusted_overhead) * efficiency_boost
    
    # Normalize using min-max bounds
    normalized = max(raw_performance, 50)  # Floor at 50
    return int(normalized)

# System operation profile
operations = [
    {'cycles': 120, 'type': 'compute', 'priority': 5},
    {'cycles': 85, 'type': 'io', 'priority': 8},
    {'cycles': 200, 'type': 'compute', 'priority': 6},
    {'cycles': 60, 'type': 'network', 'priority': 9}
]

overhead = 45

# Intermediate diagnostic variable (irrelevant to final answer but present)
diagnostic_mode = False
temp_buffer = [x['cycles'] for x in operations if x['type'] == 'io']

# Key computation step
efficiency_score = calculate_performance(operations, overhead)
final_output = efficiency_score

print(f"Result: {final_output}")