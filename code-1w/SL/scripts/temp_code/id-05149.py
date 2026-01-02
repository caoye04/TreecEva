def calculate_net_flow(flow_rates, positions):
    total = 0
    adjustment_factor = 0.85
    temp_buffer = []

    for i, (key, rate) in enumerate(flow_rates.items()):
        if i % 2 == 0:
            adjusted_rate = rate * adjustment_factor
        else:
            adjusted_rate = rate

        # Irrelevant accumulation (distractor)
        temp_buffer.append(adjusted_rate ** 0.5)

        # Only even-indexed keys contribute to final result
        if i in positions:
            total += int(adjusted_rate)

    # Dead code path (misleading)
    if len(temp_buffer) > 10:
        return sum(temp_buffer) / len(temp_buffer)

    return total


# Simulate sensor data flow rates (key: sensor_id, value: flux rate)
rate_map = {f'sensor_{i}': 15 + i * 3 for i in range(8)}

# Track relevant indices (even-numbered positions)
indices = [i for i in range(len(rate_map)) if i % 2 == 0]

# Auxiliary computation – unrelated to final result
redundant_calc = list(map(lambda x: x ** 2 - x, [4, 8, 15, 16, 23]))

# Secondary structure with zip usage (partially relevant)
enumerated_sensors = list(enumerate(zip(rate_map.keys(), rate_map.values())))
valid_pairs = []
for idx, (sensor_id, val) in enumerated_sensors:
    if 'sensor_3' not in sensor_id and val > 18:
        valid_pairs.append((idx, val))

# Final calculation
final_flux = calculate_net_flow(rate_map, indices)

# Print result
print(f"Result: {final_flux}")