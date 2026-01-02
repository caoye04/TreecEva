def analyze_trends(data, threshold=0.5):
    return [x for x in data if x > threshold]

# Simulate sensor readings from a climate monitoring system
temperature_readings = [0.3, 0.7, 0.4, 0.9, 1.1, 0.6, 0.2]
humidity_readings = [0.8, 0.6, 0.75, 0.92, 0.45, 0.68, 0.71]
pressure_readings = [1.01, 0.99, 1.02, 1.00, 0.98, 1.03, 1.01]

# Misleading transformation - not used in final calculation
smoothed_temps = list(map(lambda x: (x + 0.1) * 0.9, temperature_readings))

# Extract significant temperature events
significant_temps = analyze_trends(temperature_readings, 0.5)

# Calculate average humidity above threshold
high_humidity = [h for h in humidity_readings if h > 0.65]
avg_high_humidity = sum(high_humidity) / len(high_humidity) if high_humidity else 0

# Spurious computation on pressure - looks important but unused
pressure_variance = sum((p - 1.0) ** 2 for p in pressure_readings) / len(pressure_readings)
adjusted_pressure = [p * (1 + pressure_variance) for p in pressure_readings]

# Benchmark results combining multiple metrics
benchmark_results = [
    len(significant_temps),
    int(avg_high_humidity * 100),
    sum(1 for h in humidity_readings if h > 0.7),
    len(temperature_readings) - len(significant_temps)
]

# Auxiliary function that appears complex but is straightforward
def calculate_stability(readings, weight=0.1):
    if len(readings) < 2:
        return 0
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return round(sum(diffs) * weight, 2)

# Unused stability calculations - red herring
temp_stability = calculate_stability(temperature_readings)
humidity_stability = calculate_stability(humidity_readings)

# Core logic: performance metric based on benchmark results
def calculate_performance(results):
    base_score = results[0] * 10
    bonus = results[1] // 10
    penalty = results[3] * 2
    # Weighted combination
    return base_score + bonus - penalty + results[2]

# Final computation step
total_valid_readings = len(temperature_readings) + len(humidity_readings) + len(pressure_readings)
redundant_checksum = sum([len(temperature_readings), len(humidity_readings)])

final_score = calculate_performance(benchmark_results)

print(f"Target result: {final_score}")