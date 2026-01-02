def calculate_efficiency(data):
    normalized = [x / sum(data) for x in data]
    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified info-theoretic measure
    return int(-entropy * 100)

# Sensor simulation (distractor: not actually sensors)
base_load = [120, 85, 140, 95, 110]
adjustment_factor = 1.1
temperature_offset = 3.5  # Unused in final logic

# Data preprocessing
filtered = [val for val in base_load if val > 90]
log_data = [int(x * adjustment_factor) for x in filtered]

# Critical computation
energy_score = calculate_efficiency(log_data)

# Output result
print(f"Result: {energy_score}")