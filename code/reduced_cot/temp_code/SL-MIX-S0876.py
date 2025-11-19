from functools import reduce
from collections import namedtuple

def hash_transform(text):
    return reduce(lambda x, y: (x * 31 + ord(y)) & 0xFFFFFFFF, text, 0)

def process_reading(sensor_data, calibration_map):
    base_hash = hash_transform(sensor_data.location)
    adjusted_value = float(sensor_data.temperature) * 1.8 + 32  # Celsius to Fahrenheit
    
    if adjusted_value > 100:
        mode = 'HOT'
    elif adjusted_value < 32:
        mode = 'FREEZING'
    else:
        mode = 'NORMAL'
    
    # Switch-case simulation
    processors = {
        'HOT': lambda v: (v * 2) % 97,
        'FREEZING': lambda v: (v // 3) % 79,
        'NORMAL': lambda v: (v + 10) % 53
    }
    
    processed = processors[mode](base_hash)
    calibrated = processed ^ calibration_map.get(mode, 0xFF)
    return calibrated

def main():
    SensorData = namedtuple('SensorData', ['location', 'temperature'])
    
    sensors = [
        SensorData('arctic_station_01', '-40.0'),
        SensorData('desert_outpost_a', '50.0'),
        SensorData('tropical_buoy_12', '30.0')
    ]
    
    calibration = {'HOT': 0xA5, 'FREEZING': 0x3C, 'NORMAL': 0x6F}
    
    results = []
    for sensor in sensors:
        value = process_reading(sensor, calibration)
        results.append(value)
    
    # Final aggregation step
    final_output = (results[0] << 2) + (results[1] >> 1) - results[2]
    final_output = final_output % 1000
    
    print(f"Result: {final_output}")

if __name__ == "__main__":
    main()