def initialize_sensor_data():
    # Initialize base sensor readings with some noise
    raw_readings = [i * 7 + 3 for i in range(15)]
    calibration_offset = 12
    temperature_adjustment = 8
    
    # Apply calibration adjustments (distractor)
    calibrated_data = [reading - calibration_offset for reading in raw_readings]
    adjusted_temps = [temp + temperature_adjustment for temp in calibrated_data]
    
    # Dead code path - never used
    redundant_calc = sum(adjusted_temps) // len(adjusted_temps)
    
    # Main data processing
    quality_threshold = 5
    sensor_fault_mask = [x % 3 == 0 for x in raw_readings]
    
    # Misleading intermediate calculation
    filtered_faulty = [raw_readings[i] for i in range(len(raw_readings)) if not sensor_fault_mask[i]]
    
    # Core logic - data points meeting quality criteria
    data_points = [x for x in raw_readings if x % 2 == 1]
    valid_data_count = len([x for x in data_points if x > 20])
    
    # Critical execution point
    final_analysis_result = [x for x in data_points if x % quality_threshold == 0]
    
    # Print the target result
    print(f"Target result: {final_analysis_result}")

initialize_sensor_data()