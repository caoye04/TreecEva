def calculate_stability(data):
    if not data:
        return 0
    
    avg = sum(data) / len(data)
    stable_count = sum(1 for x in data if abs(x - avg) < 5)
    
    adjustment = 1.5 if stable_count > len(data) * 0.7 else 0.8
    
    return round(avg * adjustment)

# Sensor readings in kPa
readings = [102, 98, 101, 99, 103, 100, 97]

# Irrelevant auxiliary variable (minimal distraction)
temperature_offset = 2.3

pressure_index = calculate_stability(readings)

Result: pressure_index