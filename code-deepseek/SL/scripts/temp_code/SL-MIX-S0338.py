from itertools import accumulate

def process_sensor_readings():
    raw_readings = [12, 8, 15, 22, 18, 25]
    calibration_offset = 3
    adjusted_readings = [x + calibration_offset for x in raw_readings]
    threshold_filter = [x for x in adjusted_readings if x > 15]
    processed_data = list(accumulate(threshold_filter))
    final_result = sum(processed_data)
    print(f"Result: {final_result}")

process_sensor_readings()