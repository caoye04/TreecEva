from functools import reduce

def calculate_shipping_cost(weight, distance):
    base_rate = 2.5
    return base_rate * weight * (distance / 100)

def apply_divide_and_conquer_discount(weights, costs):
    if len(weights) <= 1:
        return costs
    mid = len(weights) // 2
    left_weights, right_weights = weights[:mid], weights[mid:]
    left_costs, right_costs = costs[:mid], costs[mid:]
    return apply_divide_and_conquer_discount(left_weights, left_costs) + apply_divide_and_conquer_discount(right_weights, right_costs)

def process_shipments():
    # State machine for package routing
    states = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': []}
    current_city = 'A'
    
    # Shipment data: (weight, destination)
    shipments = [(15, 'D'), (8, 'C'), (22, 'D'), (5, 'B'), (12, 'D')]
    distances = {'A': {'B': 120, 'C': 200}, 'B': {'C': 80, 'D': 150}, 'C': {'D': 70}}
    
    total_cost = 0
    shipment_weights = []
    shipment_costs = []
    
    for weight, destination in shipments:
        if weight > 25:
            return 0  # Early return for overweight packages
        
        path_cost = 0
        temp_city = current_city
        
        # Route package through cities using state machine
        while temp_city != destination:
            if not states[temp_city]:
                break
            next_cities = states[temp_city]
            if destination in next_cities:
                path_cost += calculate_shipping_cost(weight, distances[temp_city][destination])
                break
            else:
                # Move to first available city
                next_city = next_cities[0]
                if temp_city in distances and next_city in distances[temp_city]:
                    path_cost += calculate_shipping_cost(weight, distances[temp_city][next_city])
                temp_city = next_city
                
                if temp_city == destination:
                    break
        
        shipment_weights.append(weight)
        shipment_costs.append(path_cost)
        total_cost += path_cost
    
    # Sort weights for divide and conquer discount application
    sorted_indices = sorted(range(len(shipment_weights)), key=lambda i: shipment_weights[i])
    sorted_weights = [shipment_weights[i] for i in sorted_indices]
    sorted_costs = [shipment_costs[i] for i in sorted_indices]
    
    # Apply discount: 10% off for shipments >= 10 weight units
    discounted_costs = [
        cost * 0.9 if weight >= 10 else cost 
        for weight, cost in zip(sorted_weights, sorted_costs)
    ]
    
    # Use divide and conquer to finalize costs
    final_costs = apply_divide_and_conquer_discount(sorted_weights, discounted_costs)
    
    # Sum all discounted costs
    total_discounted_cost = reduce(lambda x, y: x + y, final_costs, 0)
    
    return total_discounted_cost

result = process_shipments()
print(f"Result: {result}")