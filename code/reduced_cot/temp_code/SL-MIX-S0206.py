from collections import defaultdict

def simulate_calibration():
    sensor_readings = [23, -15, 42, -8, 37]
    adjustment_log = defaultdict(int)
    base_offset = 100
    
    for idx, reading in enumerate(sensor_readings):
        temp_factor = (reading * 3) % 17 if reading > 0 else (-reading * 2) % 13
        correction = (temp_factor + idx) % 7
        adjustment_log[reading] += correction
    
    aggregate_shift = sum(adjustment_log.values())
    final_adjustment = (base_offset + aggregate_shift) % 20 if aggregate_shift > 10 else (base_offset - aggregate_shift) % 20
    return final_adjustment

final_adjustment = simulate_calibration()
print(f"Result: {final_adjustment}")