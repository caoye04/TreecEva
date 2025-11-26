def calculate_temperature_score(temps, threshold):
    valid_temps = [t for t in temps if t > threshold]
    if not valid_temps:
        return 0
    avg_temp = sum(valid_temps) / len(valid_temps)
    return round(avg_temp * 1.5, 2)

temperature_data = [15.2, 18.7, 22.1, 19.8, 16.5, 14.9, 20.3]
threshold_value = 16.0
baseline_temp = 18.0

# Calculate the temperature metric
temperature_metric = calculate_temperature_score(temperature_data, threshold_value)

print(f"Target result: {temperature_metric}")