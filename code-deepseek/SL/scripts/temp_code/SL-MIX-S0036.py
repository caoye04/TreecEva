def analyze_manufacturing_batch():
    raw_readings = [84, 92, 78, 95, 88, 76, 91, 83, 89, 94]
    quality_metrics = [reading * 0.1 for reading in raw_readings[:5]]
    
    temperature_adjustments = [2.5, -1.8, 3.2, -0.9, 1.7]
    pressure_corrections = [x * 0.5 for x in temperature_adjustments]
    
    processed_values = []
    for i in range(min(len(quality_metrics), len(pressure_corrections))):
        temp_calc = quality_metrics[i] + temperature_adjustments[i]
        adjusted_value = temp_calc * 0.8 + pressure_corrections[i]
        processed_values.append(adjusted_value)
    
    redundant_check = sum(raw_readings[5:]) / len(raw_readings[5:])
    unused_validation = max(raw_readings) - min(raw_readings)
    
    quality_metrics[-1] = max(processed_values[-2:])
    final_quality_score = round(quality_metrics[-1] * 10)
    
    print(f"Target result: {final_quality_score}")

analyze_manufacturing_batch()