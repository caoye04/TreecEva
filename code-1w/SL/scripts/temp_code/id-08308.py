def normalize(value, base):
    return (value - base) / base if base != 0 else 0

readings = [105, 230, 180, 99, 250]
valid_readings = [r for r in readings if r > 100]

min_reading = min(valid_readings)
max_reading = max(valid_readings)

scaling_factor = 1.5
adjusted_max = max_reading * scaling_factor

# Determine baseline energy reference
baseline = sum(r // 10 for r in valid_readings) / len(valid_readings)

# Normalize max energy relative to minimum valid reading
energy_threshold = normalize(max_reading, min_reading)

# Apply conditional damping if threshold exceeds safety limit
damped_threshold = energy_threshold * 0.9 if energy_threshold > 1.0 else energy_threshold

# Final adjustment using lambda-based correction
correction = lambda x: x + 0.1 if x < 1.2 else x
energy_threshold = correction(damped_threshold)

print(f"Result: {energy_threshold}")