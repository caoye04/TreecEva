import itertools

# Environmental sensor data processing simulation
temperature_readings = [23.5, 19.0, 27.3, 22.1, 30.2, 25.8, 18.9, 24.4, 26.7, 21.0]
humidity_levels = [45, 53, 38, 49, 31, 42, 55, 47, 36, 50]
altitude_data = [120, 135, 110, 128, 98, 142, 130, 118, 105, 125]

# Irrelevant transformations (distractors)
decoy_transform = list(map(lambda x: (x - 32) * 5/9, [f * 9/5 + 32 for f in temperature_readings]))
shifted_humidity = [(h + 10) % 100 for h in humidity_levels]

# Real processing begins
valid_range_mask = [20.0 <= temp <= 27.0 for temp in temperature_readings]
filtered_temperatures = list(itertools.compress(temperature_readings, valid_range_mask))

# Misleading intermediate calculation (dead end)
apparent_trend = filtered_temperatures[::2] if len(filtered_temperatures) > 3 else filtered_temperatures
phantom_baseline = sum(apparent_trend) / len(apparent_trend) if apparent_trend else 0.0

# Conditional correction based on auxiliary data (only humidity > 40 matters)
eligible_altitudes = {alt for idx, alt in enumerate(altitude_data) if humidity_levels[idx] > 40}
correction_factor = 1.25 if any(alt < 120 for alt in eligible_altitudes) else 0.85

# Key red herring: complex but unused data structure
temp_histogram = {t: temperature_readings.count(t) for t in set(temperature_readings)}
aggregated_diagnostics = [
    (temp, hum, alt) for temp, hum, alt in zip(temperature_readings, humidity_levels, altitude_data)
    if hum > 45 and alt > 115
]
deep_analysis = [
    round((t - 20) ** 1.5) for t, h, a in aggregated_diagnostics
    if t > 22 and a in eligible_altitudes
]

# Dead function - looks important but never called
def calculate_stability_index(data):
    if not data:
        return 0
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance, 2)

# Secondary distraction: sorting unrelated values
sorted_pairs = sorted(zip(humidity_levels, altitude_data), key=lambda x: x[1], reverse=True)
high_humidity_peaks = [p for p in sorted_pairs if p[0] > 45]

# Core logic embedded within distractions
baseline_reference = sum(temperature_readings) / len(temperature_readings)
adjustment_ratio = len([h for h in humidity_levels if h < 50]) / len(humidity_levels)

# Critical statement with answer computation
filtration_score = sum(filtered_temperatures) * correction_factor

# Final output
print(f"Result: {filtration_score}")