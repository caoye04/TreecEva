def calculate_total_weight(data):
    total_weight = 0
    weights = [2.5, 3.0, 1.8, 4.2, 2.9]
    categories = ['A', 'B', 'C', 'D', 'E']
    threshold = 3.0
    count_above = 0

    for i, (item, qty) in enumerate(zip(data, weights)):
        if item['category'] == 'X':
            continue
        adjusted_qty = qty * item['quantity']
        if qty >= threshold:
            count_above += 1
        total_weight += adjusted_qty

    scaling_factor = 1.1 if count_above > 2 else 1.0
    total_weight *= scaling_factor

    temp_offset = 0.0  # Irrelevant variable for minor interference
    return int(total_weight)

# Simulated sensor data from warehouse inventory
item_data = [
    {'name': 'sensor_a', 'category': 'A', 'quantity': 4},
    {'name': 'sensor_b', 'category': 'B', 'quantity': 5},
    {'name': 'sensor_c', 'category': 'C', 'quantity': 6},
    {'name': 'sensor_d', 'category': 'D', 'quantity': 3},
    {'name': 'sensor_e', 'category': 'E', 'quantity': 7}
]

total_weight = calculate_total_weight(item_data)
print(f"Result: {total_weight}")