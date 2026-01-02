def calculate_payload_efficiency(weights, max_capacity):
    normalized_weights = [w / max_capacity for w in weights]
    packed_weights = []
    temp_sum = 0
    
    for i, weight in enumerate(normalized_weights):
        if temp_sum + weight <= 1.0:
            packed_weights.append(weight)
            temp_sum += weight
        else:
            break
    
    total_load = sum(packed_weights)
    efficiency = total_load / len(normalized_weights)
    status = "Optimal" if efficiency > 0.7 else "Suboptimal"
    return total_load

weights = [150, 200, 300, 100, 250]
max_capacity = 400
efficiency_result = calculate_payload_efficiency(weights, max_capacity)
print(f"Result: {efficiency_result}")