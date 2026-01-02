def calculate_performance(base, delta, factor):
    adjusted = base + delta * factor
    normalized = max(0, min(adjusted, 100))
    return round(normalized, 2)

# Simulation parameters
temperature_readings = [22.5, 23.0, 21.8]
baseline = sum(temperature_readings) / len(temperature_readings)
device_age_years = 3
correction_factor = 1.5 if device_age_years > 2 else 1.0
deviation = -4.7

# Irrelevant string operation (distractor)
data_label = "T_2024"
label_suffix = data_label.upper().replace("T", "X")

# Key computation
final_score = calculate_performance(baseline, deviation, correction_factor)
print(f"Result: {final_score}")