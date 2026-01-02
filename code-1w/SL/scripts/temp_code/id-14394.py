def process_temperatures(raw_readings):
    # Normalize temperature readings from sensors
    normalized = [(t - 32) * 5/9 for t in raw_readings]
    return [round(temp, 2) for temp in normalized if temp > -50]

# Simulate sensor data (Fahrenheit)
sensor_data = [68, 77, 104, 32, 50, 86, 95]

# Irrelevant transformation: convert to Kelvin for no reason
temp_kelvin = [(t + 459.67) * 5/9 for t in sensor_data]

# Process temperatures into Celsius
processed_celsius = process_temperatures(sensor_data)

# Compute moving average as a distraction
window_size = 3
moving_averages = [sum(processed_celsius[i:i+window_size]) / window_size 
                    for i in range(len(processed_celsius) - window_size + 1)]

# Weighted adjustment factors based on time of day (mock)
factors = [0.9, 1.1, 1.0, 0.95, 1.05]
adjusted_readings = [processed_celsius[i] * factors[i % len(factors)] 
                     for i in range(len(processed_celsius))]

# Apply correction for calibration drift (only affects index 0)
drift_correction = lambda x, i: x * 0.98 if i == 0 else x
corrected = [drift_correction(val, idx) for idx, val in enumerate(adjusted_readings)]

# Calculate quality metrics (unused)
variance = sum((x - sum(corrected)/len(corrected))**2 for x in corrected) / len(corrected)
quality_flag = variance < 100

# Core logic: count how many exceed threshold and apply formula
threshold_exceeds = sum(1 for c in corrected if c > 25)
base_score = threshold_exceeds * 17

# Secondary factor: sum of original processed values above 20
top_contributors = sum(p for p in processed_celsius if p > 20)
bonus = int(top_contributors // 10)

# Final calculation
final_score = base_score + bonus

print(f"Result: {final_score}")