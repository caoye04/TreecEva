def calculate_inventory_value(items, quantities, base_weights):
    # Simulate adjustment of weights based on item durability and quantity
    adjusted_weights = []
    temp_buffer = [0] * len(items)  # Irrelevant pre-allocation (minor distraction)

    for i, (item, qty) in enumerate(zip(items, quantities)):
        durability = len(item) % 3 + 1  # Simulated durability factor
        base_weight = base_weights[i]
        adjusted_weight = base_weight * qty * (durability / 2.0)
        adjusted_weights.append(adjusted_weight)

    extra_check = sum(quantities) > 0  # Distractor: unused logical check
    total_weight = sum(adjusted_weights)
    return total_weight

# Input data
items = ['gear', 'pulley', 'shaft', 'bearing']
quantities = [4, 6, 2, 8]
base_weights = [1.5, 2.0, 3.0, 1.0]

result = calculate_inventory_value(items, quantities, base_weights)
print(f"Result: {result}")