def calculate_network_capacity():
    base_rates = [120, 150, 130, 170, 140]
    maintenance_nodes = {1, 3}
    adjusted_caps = []

    for index, rate in enumerate(base_rates):
        if index in maintenance_nodes:
            adjusted_rate = rate * 0.75
        else:
            adjusted_rate = rate * 1.1
        adjusted_caps.append(int(adjusted_rate))

    total_capacity = sum(adjusted_caps)
    return total_capacity

result = calculate_network_capacity()
print(f"Target result: {result}")