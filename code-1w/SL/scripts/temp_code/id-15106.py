def analyze_sensor_data():
    raw_readings = [105, -20, 300, 15, 0, 400, -5, 88, 250, 99]
    status_codes = ['OK', 'ERROR', 'OK', 'OK', 'OK', 'ERROR', 'WARNING', 'OK', 'OK', 'OK']
    
    # Normalize readings: negative values indicate sensor error
    corrected_readings = [x if x >= 0 else 0 for x in raw_readings]
    
    # Pair readings with status using enumerate and filter by status
    valid_entries = []
    for i, code in enumerate(status_codes):
        if code == 'OK' or code == 'WARNING':
            valid_entries.append(corrected_readings[i])
    
    # Apply threshold filter using slicing: ignore last two entries for stability check
    trimmed_entries = valid_entries[:-2]
    
    # Calculate final sum of qualified sensor readings
    filtered_sum = sum(trimmed_entries)
    
    # Irrelevant auxiliary variable (minimal distraction)
    average_raw = sum(raw_readings) / len(raw_readings)
    
    print(f"Result: {filtered_sum}")

analyze_sensor_data()