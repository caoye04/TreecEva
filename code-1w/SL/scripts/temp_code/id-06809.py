temperatures_celsius = [25, 30, 35, 40, 45]
offset = 273.15
correction_factor = 1.02

# Convert to Kelvin and apply smoothing using a moving average
temperatures_kelvin = [temp + offset for temp in temperatures_celsius]
smoothed_kelvin = []
for i in range(1, len(temperatures_kelvin) - 1):
    avg_temp = (temperatures_kelvin[i-1] + temperatures_kelvin[i] + temperatures_kelvin[i+1]) / 3
    smoothed_kelvin.append(avg_temp)

# Apply minor adjustment based on calibration data
adjustment_map = {"low": 0.5, "med": 1.2, "high": 0.8}
adjusted_readings = [t * adjustment_map["med"] for t in smoothed_kelvin]

# Final correction before output
final_temperature = adjusted_readings[-1] * correction_factor
print(f"Result: {final_temperature}")