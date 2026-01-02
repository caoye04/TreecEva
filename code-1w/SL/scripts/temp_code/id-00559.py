def analyze_performance(data, threshold_fn):
    filtered = [x for x in data if threshold_fn(x)]
    return sum(filtered) // len(filtered) if filtered else 0

# Sensor metrics from system diagnostics
temperatures = [23, 45, 56, 67, 32, 40]
pressures = [101, 98, 105, 110, 95]
efficiency_scores = [78, 85, 90, 65, 88]

# Combined metric using modular weighting
metrics = [(t + p) % s for t, p, s in zip(temperatures, pressures, efficiency_scores)]

# Threshold function to filter significant values
threshold_func = lambda x: x > 40

# Final performance analysis
final_analysis = analyze_performance(metrics, threshold_func)

# Secondary variables (distractors)
avg_temp = sum(temperatures) / len(temperatures)
normalized_pressure = max(pressures) - min(pressures)
baseline = len(efficiency_scores) * 2

target_result = final_analysis
print(f"Result: {target_result}")