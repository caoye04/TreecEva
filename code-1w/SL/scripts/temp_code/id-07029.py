def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 18.7, 30.1, 27.4, 22.0, 19.3, 26.8, 24.2]
    
    # Irrelevant auxiliary data - red herring
    device_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010']
    location_map = {uid: f'Zone-{i % 3 + 1}' for i, uid in enumerate(device_ids)}
    
    # Decoy transformation - unused
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]
    
    # Actual processing begins: filter out readings below threshold
    threshold = 20.0
    filtered_data = [temp for temp in raw_readings if temp >= threshold]
    
    # Multiple assignment and distractor variables
    total_sensors, active_count = len(raw_readings), len(filtered_data)
    utilization_rate = active_count / total_sensors
    
    # Unused complex structure - misleading
    stats_bundle = {
        'mean_raw': sum(raw_readings) / len(raw_readings),
        'variance_raw': sum((x - sum(raw_readings)/len(raw_readings))**2 for x in raw_readings) / len(raw_readings),
        'outlier_flags': [abs(x - sum(raw_readings)/len(raw_readings)) > 2 * (sum((y - sum(raw_readings)/len(raw_readings))**2 for y in raw_readings) / len(raw_readings))**0.5 for x in raw_readings]
    }
    
    # Set operations on disguised irrelevant data
    high_temp_zones = set()
    for i, temp in enumerate(raw_readings):
        if temp > 26:
            zone = location_map[device_ids[i]].lower()
            high_temp_zones.add(zone)
    
    # Distractor: zip and enumerate used but not affecting main logic
    indexed_diagnostics = {}
    for idx, (temp, uid) in enumerate(zip(raw_readings, device_ids)):
        status = 'critical' if temp > 29 else 'elevated' if temp > 25 else 'normal'
        indexed_diagnostics[uid] = {'index': idx, 'status': status}
   
    # Calibration data - relevant
    base_offset = 1.2
    drift_correction = 0.3
    calibration_factor = base_offset - drift_correction
    
    # Real processing function with nested logic
    def process_readings(data, factor):
        adjusted = [t * (1 + factor/100) for t in data]  # Minor scaling
        
        # Nested conditional with early exit red herring
        if sum(adjusted) < 100:
            return -999  # Dead path - never reached
            
        # Bit manipulation decoy
        magic_key = 0
        for val in adjusted:
            shifted = int(val * 10) ^ 0b1101
            magic_key ^= shifted & 0xFF
        
        # Actual computation path
        squared_deviations = [(x - sum(adjusted)/len(adjusted))**2 for x in adjusted]
        variance = sum(squared_deviations) / len(squared_deviations)
        std_dev = variance ** 0.5
        
        # Final diagnostic score based on spread
        penalty = std_dev * 10
        bonus = len(adjusted) * 0.5
        
        result = round(100 + bonus - penalty, 4)
        
        # Another decoy branch
        if magic_key % 7 == 0:
            result -= 50  # Not triggered due to magic_key properties
            
        return result

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()