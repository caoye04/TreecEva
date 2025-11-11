import itertools

def calculate_signal_strength(raw_data, modulation_factors):
    strength = 0
    for i, (data_point, factor) in enumerate(zip(raw_data, modulation_factors)):
        if i % 2 == 0:
            strength ^= (data_point << 1) & factor
        else:
            strength |= (data_point >> 1) | factor
    return strength

def optimize_routing_path(sensor_readings):
    max_efficiency = -1
    best_path = None
    
    for path in itertools.permutations(sensor_readings.keys(), 3):
        if path[0] > path[-1]:  # Early termination condition
            continue
            
        path_efficiency = 0
        valid_path = True
        
        for i in range(len(path)-1):
            current_sensor = path[i]
            next_sensor = path[i+1]
            
            # Greedy selection with early return
            if sensor_readings[current_sensor] < 0 or sensor_readings[next_sensor] < 0:
                valid_path = False
                break
                
            link_quality = (sensor_readings[current_sensor] & sensor_readings[next_sensor])
            if link_quality == 0:
                valid_path = False
                break
                
            path_efficiency += link_quality
            
        if not valid_path:
            continue
            
        if path_efficiency > max_efficiency:
            max_efficiency = path_efficiency
            best_path = path
    
    return max_efficiency if max_efficiency != -1 else 0

# Sensor network configuration
sensor_network = {
    'alpha': 15,
    'beta': 7,
    'gamma': 12,
    'delta': 9,
    'epsilon': 6
}

raw_signal_data = [3, 5, 2, 8, 1]
modulation_params = [4, 6, 1, 3, 7]

# Calculate base signal strength
base_strength = calculate_signal_strength(raw_signal_data, modulation_params)

# Optimize routing path
optimal_efficiency = optimize_routing_path(sensor_network)

# Compute final transmission efficiency score
if optimal_efficiency > 0 and base_strength > 0:
    transmission_efficiency_score = (base_strength << 2) ^ optimal_efficiency
else:
    transmission_efficiency_score = base_strength | optimal_efficiency

print(f"Result: {transmission_efficiency_score}")