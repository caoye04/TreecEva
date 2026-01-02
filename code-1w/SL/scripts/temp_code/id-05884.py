def calculate_network_capacity():
    server_loads = [78, 85, 90, 67, 88]
    server_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    active_servers = [name for name in server_names if len(name) > 4]
    
    base_capacities = [100, 120, 120, 90, 110]
    utilization_rates = [load / 100 for load in server_loads]
    server_caps = [base_capacities[i] * utilization_rates[i] for i in range(len(base_capacities))]
    
    maintenance_mode = False
    efficiency_factor = 0.95 if not maintenance_mode else 0.75
    total_capacity = sum(server_caps) * efficiency_factor
    
    return total_capacity

result = calculate_network_capacity()
print(f"Result: {result}")