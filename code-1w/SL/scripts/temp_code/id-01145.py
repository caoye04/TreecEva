def calculate_remaining_capacity(storages, constraints):
    total_used = sum([s['capacity'] * s['utilization'] for s in storages])
    max_threshold = max([c['limit'] for c in constraints])
    min_threshold = min([c['limit'] for c in constraints])
    
    # Irrelevant computation: historical average (not used)
    hist_avg = sum([c['limit'] * 0.85 for c in constraints]) / len(constraints) if constraints else 0
    
    # Simulate adjustment factor based on threshold spread
    spread = max_threshold - min_threshold
    adjustment = spread * 0.1 if spread > 100 else spread * 0.05
    
    baseline_capacity = sum([s['capacity'] for s in storages])
    reserved_margin = baseline_capacity * 0.15
    
    # Dummy loop to calculate unused categories (distractor)
    unused_categories = []
    for s in storages:
        if s['utilization'] < 0.1:
            unused_categories.append(s['type'])
    dummy_sum = sum([hash(cat) % 100 for cat in unused_categories])  # Dead-end calculation
    
    # Conditional expression for dynamic reduction
    reduction_factor = 0.2 if any(s['utilization'] > 0.9 for s in storages) else 0.1
    overused = [s for s in storages if s['utilization'] > 0.9]
    critical_count = len(overused)
    
    # Extra distraction: simulate hypothetical expansion
    hypothetical_growths = {s['type']: s['capacity'] * 1.2 for s in storages}
    growth_sum = sum(hypothetical_growths.values())  # Not used later
    
    # Actual capacity logic
    adjusted_baseline = baseline_capacity - total_used
    safety_adjusted = adjusted_baseline - reserved_margin
    final_reduction = safety_adjusted * (1 - reduction_factor)
    
    # Key statement
    final_capacity = int(final_reduction - adjustment)
    return final_capacity

# Data setup
storages = [
    {'type': 'SSD',     'capacity': 512,   'utilization': 0.95},
    {'type': 'HDD',     'capacity': 2000,  'utilization': 0.72},
    {'type': 'NVMe',    'capacity': 1000,  'utilization': 0.88},
    {'type': 'Tape',    'capacity': 5000,  'utilization': 0.05}
]

constraints = [
    {'limit': 1200},
    {'limit': 300},
    {'limit': 1500},
    {'limit': 800}
]

# Execution
final_capacity = calculate_remaining_capacity(storages, constraints)
print(f"Result: {final_capacity}")