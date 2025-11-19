def process_sensor_data():
    raw_readings = [12, -5, 23, -18, 34, -42, 55]
    
    # Step 1: Apply noise filter (keep only positive values)
    filtered_readings = list(filter(lambda x: x > 0, raw_readings))
    
    # Step 2: Amplify signals (multiply by 2.5)
    amplified_signals = list(map(lambda x: x * 2.5, filtered_readings))
    
    # Step 3: Apply threshold detection
    detected_signals = []
    for signal in amplified_signals:
        if signal < 30:
            level = 'LOW'
        elif signal < 60:
            level = 'MEDIUM'
        else:
            level = 'HIGH'
        
        # Step 4: Convert level back to numeric value
        match level:
            case 'LOW':
                detected_signals.append(signal * 0.5)
            case 'MEDIUM':
                detected_signals.append(signal * 1.2)
            case 'HIGH':
                detected_signals.append(signal * 0.8)
    
    # Step 5: Calculate final signal strength as sum of processed signals
    processed_signal_strength = sum(detected_signals)
    
    return processed_signal_strength

result = process_sensor_data()
print(f"Result: {result}")