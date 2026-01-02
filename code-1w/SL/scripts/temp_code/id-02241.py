from itertools import compress

def calculate_residual(capacities, logs):
    total_used = 0
    for entry in logs:
        if 'active' in entry and entry['active']:
            total_used += entry['usage']
    
    # Determine effective capacities (non-zero only for systems with recent activity)
    recent_activity = [entry['timestamp'] > 1690000000 for entry in logs]
    active_capacities = list(compress(capacities, recent_activity))
    
    system_count = len(active_capacities)
    average_capacity = sum(active_capacities) / system_count if system_count > 0 else 0
    
    estimated_load = average_capacity * 0.8  # Assume 80% typical utilization
    
    # Calculate residual as difference between total capacity and actual + estimated
    total_capacity = sum(capacities)
    residual_capacity = total_capacity - total_used - estimated_load
    
    debug_flag = True  # Irrelevant flag for logging (distractor)
    return int(residual_capacity)

# System power capacities in MW
system_capacities = [120, 150, 100, 200, 180]

# Usage logs with metadata
usage_records = [
    {'usage': 95, 'active': True, 'timestamp': 1691500000},
    {'usage': 70, 'active': False, 'timestamp': 1689000000},
    {'usage': 110, 'active': True, 'timestamp': 1692000000},
    {'usage': 0, 'active': False, 'timestamp': 1688500000},
    {'usage': 160, 'active': True, 'timestamp': 1693000000}
]

residual_capacity = calculate_residual(system_capacities, usage_records)
print(f"Result: {residual_capacity}")