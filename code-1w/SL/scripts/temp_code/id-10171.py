def analyze_metrics(data_points):
    total = 0
    count = 0
    for val in data_points:
        if val > 0:
            total += val ** 0.5
            count += 1
    return total / count if count > 0 else 0


def validate_input(x):
    return x >= 0

base_load = 8472
stress_factor = 3.7
auxiliary_power = 0

# Simulate sensor readings (irrelevant to final result)
sensor_data = [144, 225, 0, 196, -1, 256]
metric_score = analyze_metrics(sensor_data)

# Distractor: power calibration chain with dead-end computation
temp_buffer = []
for i in range(3):
    temp_buffer.append((i + 1) * 1024)

normalized_power = sum(temp_buffer) / 1024  # Red herring
auxiliary_power += normalized_power * 0.1

# Real logic begins
if validate_input(base_load):
    temp_load = base_load * 0.8
    if stress_factor > 3.5:
        adjustment = 1.25 if temp_load > 6000 else 0.9
        temp_load *= adjustment
    
    # Secondary condition with conditional expression
    decay_factor = 0.95 if stress_factor % 1 > 0.5 else 0.98
    temp_load *= decay_factor

    # Final adjustment using helper logic
    def adjust_load(load, factor):
        peak = load * (1 + (factor / 10))
        # Intermediate irrelevant calculation
        safety_margin = peak * 0.02
        reduced_peak = peak - safety_margin
        return int(reduced_peak // 100) * 100  # Quantize to nearest 100

    final_load = adjust_load(base_load, stress_factor)
else:
    final_load = -1

print(f"Result: {final_load}")