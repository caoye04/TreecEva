from collections import defaultdict

def calculate_residual(capacities, log):
    usage_count = defaultdict(int)
    for entry in log:
        usage_count[entry] += 1
    
    total_used = 0
    for key, count in usage_count.items():
        if key in capacities:
            total_used += capacities[key] * count
    
    base_capacity = sum(capacities.values())
    temp_var = base_capacity * 0.1  # Irrelevant computation (minimal interference)
    residual_capacity = base_capacity - total_used
    return residual_capacity

capacities = {'A': 120, 'B': 85, 'C': 200}
usage_log = ['A', 'B', 'A', 'C', 'B', 'A']

# Key execution point
residual_capacity = calculate_residual(capacities, usage_log)
print(f"Result: {residual_capacity}")