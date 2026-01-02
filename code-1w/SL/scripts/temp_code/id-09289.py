from itertools import combinations

def analyze_overlap(zones):
    overlap_pairs = []
    for pair in combinations(zones, 2):
        intersect = set(pair[0]) & set(pair[1])
        if len(intersect) > 0:
            overlap_pairs.append(pair)
    return overlap_pairs

def calculate_utilization(profiles):
    totals = []
    for p in profiles:
        totals.append(sum(p.values()))
    avg = sum(totals) / len(totals) if totals else 0
    return round(avg * 0.75, 3)

def calculate_remaining_capacity(units, constraints):
    base_capacities = [u['capacity'] for u in units]
    statuses = [u['status'] for u in units]
    
    active_units = [cap for cap, stat in zip(base_capacities, statuses) if stat == 'active']
    maintenance_count = statuses.count('maintenance')
    
    # Irrelevant aggregation
    temp_aggr = 0
    for i, cap in enumerate(base_capacities):
        if i % 2 == 0:
            temp_aggr += cap * 0.1
    temp_aggr = int(temp_aggr)
    
    total_capacity = sum(active_units)
    reserved_pool = total_capacity * 0.2
    
    # Simulate constraint adjustments
    applied_limits = []
    for c in constraints:
        if c['type'] == 'peak':
            applied_limits.append(c['limit'])
    
    peak_limit_adjustment = min(applied_limits) if applied_limits else 0
    
    adjusted_capacity = total_capacity - reserved_pool
    if peak_limit_adjustment > 0:
        adjusted_capacity = min(adjusted_capacity, peak_limit_adjustment)
    
    # Dummy logic with side calculations
    phantom_load = 0
    for _ in range(maintenance_count):
        phantom_load += 15
    phantom_load = phantom_load * 0.3  # unused but computed
    
    final_capacity = int(adjusted_capacity - maintenance_count * 10)
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = set(base_capacities)
        fallback.discard(0)
        final_capacity += len(fallback)
    
    return final_capacity

# Main execution context
zones_config = [
    {"A": 1, "B": 2},
    {"B": 3, "C": 4},
    {"D": 5}
]

profiles_data = [
    {'input_rate': 10, 'output_rate': 8},
    {'input_rate': 12, 'output_rate': 9}
]

units_list = [
    {'capacity': 100, 'status': 'active'},
    {'capacity': 200, 'status': 'active'},
    {'capacity': 150, 'status': 'maintenance'},
    {'capacity': 300, 'status': 'active'}
]

constraints_list = [
    {'type': 'peak', 'limit': 450},
    {'type': 'base', 'limit': 300}
]

# Trigger analysis (irrelevant to final result but adds cognitive load)
dummy_overlaps = analyze_overlap([[1,2,3], [2,3,4], [5,6]])
avg_util = calculate_utilization(profiles_data)

# Key computation
final_capacity = calculate_remaining_capacity(units_list, constraints_list)

# Output result
print(f"Target result: {final_capacity}")