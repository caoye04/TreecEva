from functools import reduce

def calculate_modular_weights(weights, modulus_base):
    return list(map(lambda w: w % modulus_base, weights))

def compute_loading_efficiency(processed_weights, capacity):
    loaded = 0
    efficiency_scores = []
    for weight in sorted(processed_weights, reverse=True):
        if loaded + weight <= capacity:
            loaded += weight
            efficiency_scores.append(weight * (loaded % 7))
    return efficiency_scores

# Package weights for the current delivery run
shipment_weights = [23, 45, 12, 67, 89, 34, 56, 78]
truck_capacity = 150
mod_base = 17

# Process weights using modular arithmetic
modular_weights = calculate_modular_weights(shipment_weights, mod_base)

# Apply greedy loading algorithm
efficiency_scores = compute_loading_efficiency(modular_weights, truck_capacity)

# Calculate final efficiency score using functional reduction
final_efficiency_score = reduce(lambda acc, score: (acc + score) % 13, efficiency_scores, 0)

print(f"Result: {final_efficiency_score}")