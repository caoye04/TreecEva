from itertools import chain

raw_readings = [15, 28, 33, 42, 51, 67, 74]
calibration_offset = 5
threshold_map = {1: 25, 2: 40, 3: 60, 4: 75}
metric_map = {25: 8, 40: 12, 60: 18, 75: 22}

temp_adjustment = calibration_offset * 2  # Not used in final calculation
processed_data = []

for reading in raw_readings:
    calibrated = reading - calibration_offset
    if calibrated > 30:
        category_key = None
        for threshold_key, threshold_val in threshold_map.items():
            if calibrated <= threshold_val:
                category_key = threshold_key
                break
        if category_key is not None:
            processed_data.append(threshold_map[category_key])

# Distractor operations that don't affect the result
intermediate_sum = sum(processed_data)
filtered_chain = list(chain(processed_data, [100, 200]))
final_metric = metric_map[processed_data[2]]

print(f"Result: {final_metric}")