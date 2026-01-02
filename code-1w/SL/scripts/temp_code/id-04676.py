def calculate_network_load(data, limits):
    total_load = 0
    status_map = {'low': 1, 'medium': 2, 'high': 3}
    for idx, (bandwidth, usage) in enumerate(zip(data['values'], data['util'])):
        level = 'low'
        if usage > limits['critical']:
            level = 'high'
        elif usage > limits['warning']:
            level = 'medium'
        
        load_factor = status_map[level]
        total_load += bandwidth * load_factor
    
    adjustment = 0
    for i in range(len(data['values'])):
        adjustment += i * 0.1  # Irrelevant accumulation (minimal interference)
    
    return int(total_load)

# Simulated network traffic data
total_load = 0
traffic_data = {
    'values': [10, 20, 30],
    'util': [0.4, 0.75, 0.9]
}
thresholds = {
    'warning': 0.6,
    'critical': 0.8
}

total_load = calculate_network_load(traffic_data, thresholds)
print(f"Result: {total_load}")