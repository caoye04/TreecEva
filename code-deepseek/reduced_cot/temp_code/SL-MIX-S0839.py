def process_temperature_data(sensor_readings):
    base_temp = 20
    calibration_offset = 3
    debug_counter = 0
    irrelevant_multiplier = 7
    
    # Distractor: complex calculation that's not used
    unused_value = (base_temp * irrelevant_multiplier) // calibration_offset + 15
    
    temp_adjustments = []
    processed_values = []
    
    for i, reading in enumerate(sensor_readings):
        # Misleading intermediate calculation
        temp_variance = reading % 4
        debug_counter += temp_variance * 2
        
        if i % 2 == 0:
            adjustment = reading + calibration_offset
        else:
            adjustment = reading - calibration_offset
        
        # Dead code path that never executes
        if reading > 100:
            emergency_adjust = reading // 2
            processed_values.append(emergency_adjust)
        
        temp_adjustments.append(adjustment)
        
        # Conditional expression for processing
        processed_val = adjustment * 2 if adjustment < base_temp else adjustment // 2
        processed_values.append(processed_val)
    
    # Another distractor calculation
    total_debug = debug_counter + len(sensor_readings)
    
    # Zip with offsets for additional complexity
    zipped_data = list(zip(temp_adjustments, processed_values))
    
    # Final calculation with integer division
    final_temperature = temp_adjustments[-1]
    
    print(f"Debug total: {total_debug}")
    print(f"Result: {final_temperature}")
    return final_temperature

# Main execution
sensor_data = [15, 22, 18, 25, 20, 28]
final_temp = process_temperature_data(sensor_data)