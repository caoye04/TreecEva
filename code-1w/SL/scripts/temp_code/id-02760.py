def analyze_sensor_drift(readings):
    drift = 0
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) > 0.5:
            drift += 0.1
    return drift

# Simulate environmental sensor data
baseline_temp = 22.5
fluctuations = [0.3, -0.4, 0.8, -0.2, 0.6, 0.1, -0.7, 0.9]
temperature_data = [round(baseline_temp + f, 2) for f in fluctuations]

baseline_pressure = 101.3
drift_compensation = analyze_sensor_drift([101.3, 101.4, 101.2, 101.8, 102.1, 101.9, 100.5, 100.3])
pressure_offsets = [0.2, -0.1, 0.5, -0.3, 0.4, 0.0, -0.6, 0.7]
pressure_data = [round(baseline_pressure + p + drift_compensation, 2) for p in pressure_offsets]

# Misleading intermediate calculations
phantom_index = 0
redundant_sum = 0.0
for idx, (t, p) in enumerate(zip(temperature_data, pressure_data)):
    if t > 22.7:
        phantom_index = idx
    redundant_sum += t * 0.01  # Irrelevant accumulation

# Hidden correction factor based on temperature variance
temp_variance = sum((t - baseline_temp) ** 2 for t in temperature_data) / len(temperature_data)
correction_factor = 1.0 if temp_variance < 0.3 else 0.92

# Compute yield using complex conditional logic
yield_factors = []
for t, p in zip(temperature_data, pressure_data):
    efficiency = 0.8 if t < 22.6 else (0.95 if t < 23.0 else 0.75)
    pressure_ratio = p / baseline_pressure
    adjusted_yield = (t * pressure_ratio * efficiency) * correction_factor
    if adjusted_yield > 25.0:
        adjusted_yield *= 0.9  # safety throttling
    yield_factors.append(round(adjusted_yield, 3))

# Determine optimal segment
max_segment_yield = 0.0
for i in range(0, len(yield_factors) - 2):
    segment_avg = sum(yield_factors[i:i+3]) / 3
    if segment_avg > max_segment_yield:
        max_segment_yield = segment_avg

# Final computation with red herring variables
aggregate_metric = sum(yield_factors) / len(yield_factors)
scaling_constant = 1.05  # unused in final logic
final_yield = round(max_segment_yield * scaling_constant, 3)  # scaling_constant used but ineffective due to rounding

# Output result
print(f"Result: {final_yield}")