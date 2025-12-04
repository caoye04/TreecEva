initial_readings = [15.2, 18.7, 22.3, 19.8, 25.1]
calibration_offset = 2.5
processed_measurements = [reading - calibration_offset for reading in initial_readings]
quality_check = len(processed_measurements) > 3
final_volume = processed_measurements[-1]
print(f"Result: {final_volume}")