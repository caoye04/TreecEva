import itertools

# Sensor calibration data
calibration_factor = 1.05
base_offset = 0.75

# Simulated raw sensor readings over time
raw_readings = [98, 102, 97, 103, 101, 99, 100]

# Apply rolling window average using itertools for smoothing
def rolling_window(iterable, size):
    iters = itertools.tee(iterable, size)
    for i in range(size):
        for _ in range(i):
            next(iters[i], None)
    return zip(*iters)

windowed_data = list(rolling_window(raw_readings, 3))
smoothed_values = [sum(window) / 3 for window in windowed_data]

# Adjust for calibration and compute final readings
adjusted_readings = [(val * calibration_factor) + base_offset for val in smoothed_values]
computed_readings = [round(r, 2) for r in adjusted_readings]

# Critical statement
total_pressure = sum(computed_readings)

# Output result
print(f"Result: {total_pressure}")