from functools import reduce

def transform_readings(readings):
    # Apply a non-linear transformation using modular exponentiation
    return [pow(r, 3, 17) for r in readings]

def adjust_values(transformed_vals):
    # Conditional adjustment based on value parity
    adjusted = []
    for val in transformed_vals:
        if val % 2 == 0:
            adjusted.append(val + 5)
        else:
            adjusted.append(val - 3)
    return adjusted

def compute_checksum(vals):
    # Divide and conquer reduction with modular arithmetic
    if len(vals) <= 1:
        return vals[0] if vals else 0
    mid = len(vals) // 2
    left_checksum = compute_checksum(vals[:mid])
    right_checksum = compute_checksum(vals[mid:])
    combined = (left_checksum * 2 + right_checksum * 3) % 19
    return combined

# Sensor readings from a device
sensor_readings = [7, 2, 9, 4, 11, 6, 13]

# Step 1: Transform readings
transformed_readings = transform_readings(sensor_readings)

# Step 2: Adjust values conditionally
adjusted_readings = adjust_values(transformed_readings)

# Step 3: Compute synchronization checksum using divide and conquer
sync_checksum = compute_checksum(adjusted_readings)

print(f"Result: {sync_checksum}")