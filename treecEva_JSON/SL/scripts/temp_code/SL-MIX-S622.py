import numpy as np

# Sensor readings
sensor_data = np.array([3, 7, 2, 8])

# Transformation matrix
transform_matrix = np.array([[1, 0, 2, 1],
                            [1, 2, 0, 1],
                            [0, 1, 1, 2],
                            [2, 1, 1, 0]])

# Apply transformation
transformed_data = np.dot(transform_matrix, sensor_data)

# Lambda function for final processing
process_func = lambda x: sum(x) % 10

# Compute final processed signal
processed_signal = process_func(transformed_data)

print(f"Result: {processed_signal}")