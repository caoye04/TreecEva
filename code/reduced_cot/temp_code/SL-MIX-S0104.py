measurements = [34.2, 67.8, 45.1, 89.3, 23.4, 56.7, 91.2, 12.8]
threshold = 50.0
calibration_factor = 1.05
data_point = [x for x in measurements if x > threshold]
print(f"Result: {data_point}")