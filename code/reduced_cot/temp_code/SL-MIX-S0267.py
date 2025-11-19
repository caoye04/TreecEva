import math
from collections import defaultdict

# Sensor readings mapped by hex identifiers (base 16)
sensor_grid = {
    '0xA': 25,
    '0xB': 16,
    '0xC': 9,
    '0xD': 4,
    '0xE': 1
}

calibration_mappings = defaultdict(int)
composite_readings = []

for hex_id, reading in sensor_grid.items():
    numeric_id = int(hex_id, 16)
    if numeric_id % 2 == 0:
        transformed = math.log(math.sqrt(reading)) if reading > 0 else 0
        calibration_mappings[numeric_id] += transformed
    else:
        power_val = math.pow(reading, 1/3.0)
        composite_readings.append(power_val)
        
intermediate_sum = sum(calibration_mappings.values())
processed_composite = [math.exp(val) for val in composite_readings if val > 2]

final_aggregate = 0
for idx, val in enumerate(processed_composite):
    if idx % 2 == 0 and not (val < 5):  # Logical combination
        final_aggregate += math.floor(val)
    elif not (idx % 2 == 0) or val >= 10:
        final_aggregate += math.ceil(val)
        
calibration_factor = round(intermediate_sum + final_aggregate)
print(f"Result: {calibration_factor}")