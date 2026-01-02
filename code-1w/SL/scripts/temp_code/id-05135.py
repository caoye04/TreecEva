def analyze_growth_potential(temp, moisture):
    # Assess base growth potential using non-linear response
    if temp < 15 or temp > 35:
        return 0.0
    base_score = (temp - 15) * (35 - temp) / 100.0
    adjusted_score = base_score * (moisture / 70.0)
    return round(adjusted_score, 3)

# Simulate seasonal climate data (temperature in Celsius, moisture %)
climate_data = [(20, 60), (24, 65), (28, 70), (30, 68), (26, 72), (22, 64)]
soil_conditions = [0.85, 0.92, 0.88, 0.75, 0.95, 0.83]  # Nutrient availability factors

# Misleading irrelevant variables (distractors)
network_buffer = bytearray(b'\x00' * 16)
file_checksum = sum(network_buffer) + len(network_buffer)
redundant_lookup = {i: chr(97 + i) for i in range(10)}

# Secondary helper that seems important but is partially unused
lambda_transform = lambda x, a, b: a * x ** 0.5 + b

# Track intermediate results
weekly_scores = []
for i, (t, m) in enumerate(climate_data):
    score = analyze_growth_potential(t, m)
    weekly_scores.append(score)

# Apply nutrient adjustment using slicing and list comprehensions
adjusted_scores = [
    s * soil_conditions[i] for i, s in enumerate(weekly_scores)
]

# Unused dead-end computation (adds interference)
buffered_readings = weekly_scores[1:-1]  # middle weeks only
smoothed_data = [sum(buffered_readings[i:i+3]) / 3 for i in range(len(buffered_readings) - 2)] if len(buffered_readings) > 2 else [0]

# Core optimization logic
threshold_filter = list(filter(lambda x: x > 0.5, adjusted_scores))
if not threshold_filter:
    final_yield = 0
else:
    peak_efficiency = max(threshold_filter)
    avg_efficiency = sum(threshold_filter) / len(threshold_filter)
    yield_index = (peak_efficiency * 0.4) + (avg_efficiency * 0.6)
    
    # Final transformation with string-based switch (unusual but valid)
    mode_flag = 'high_yield'
    correction_factor = 1.1 if 'high' in mode_flag else 1.0
    
    # Actual final calculation
    final_yield = int(yield_index * 100 * correction_factor)

# Print result as required
print(f"Result: {final_yield}")