temperatures_celsius = [23.5, 18.2, 25.8, 31.0, 19.4]

# Convert to Fahrenheit and apply sensor correction
fahrenheit_readings = [(temp * 9/5) + 32 + 0.5 for temp in temperatures_celsius]

disruption_factor = 2.1
adjusted_readings = [temp - disruption_factor for temp in fahrenheit_readings]

thermal_offset = len(adjusted_readings) * 0.3
final_temperature = adjusted_readings[-1] + thermal_offset

print(f"Result: {final_temperature}")