def calculate_warehouse_capacity():
    locations = ['A1', 'B2', 'C3', 'D4']
    storage_units = [4, 6, 5, 7]
    unit_capacity = [150, 120, 180, 100]

    # Irrelevant distractor: unused variable
    max_possible = max(unit_capacity) * max(storage_units)

    # Create capacity mapping using zip and dictionary comprehension
    capacity_map = {loc: units * cap for loc, units, cap in zip(locations, storage_units, unit_capacity)}

    # Key computation step
    total_capacity = sum(capacity_map.values())

    # Additional unrelated calculation (minimal interference)
    avg_capacity = total_capacity / len(capacity_map)

    # Print result as required
    print(f"Target result: {total_capacity}")

    return total_capacity

result = calculate_warehouse_capacity()