from collections import defaultdict

# Sensor data aggregation over time steps
telemetry_data = [
    {'temp': 72.5, 'pressure': 80, 'humidity': 30},
    {'temp': 76.3, 'pressure': 88, 'humidity': 32},
    {'temp': 74.1, 'pressure': 83, 'humidity': 29}
]

# Extract pressure readings using list comprehension
pressure_readings = [entry['pressure'] for entry in telemetry_data]

# Compute average pressure
avg_pressure = sum(pressure_readings) / len(pressure_readings)

# Determine high-temperature status using logical condition
temperature_status = any(entry['temp'] > 75 for entry in telemetry_data)

# Critical logic step: assess system threshold flag
pressure_level = round(avg_pressure, 1)
threshold_flag = temperature_status and (pressure_level < 85)

print(f"Result: {threshold_flag}")