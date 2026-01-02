def calculate_energy_threshold(readings):
    min_reading = min(readings)
    max_reading = max(readings)
    avg_reading = sum(readings) / len(readings)
    
    # Normalize readings and filter those above average
    normalized = [round((r - min_reading) / (max_reading - min_reading) * 100) for r in readings]
    filtered_readings = [val for val in normalized if val > 50]
    
    # Sort to ensure order
    filtered_readings.sort()
    
    # Key assignment
    energy_threshold = filtered_readings[-1] if filtered_readings else 0
    
    return energy_threshold

# Simulated sensor readings
sensor_inputs = [23, 45, 67, 89, 12, 34, 78, 90]
result = calculate_energy_threshold(sensor_inputs)
print(f"Target result: {result}")