from itertools import cycle

# Simulate sensor readings over a rotating system
cycle_readings = [104.5, 98.3, 102.1, 99.7]
reading_cycle = cycle(cycle_readings)

# Initial atmospheric baseline
base_pressure = 101.3

# Extract third reading from cyclic sequence
for _ in range(3):
    current_reading = next(reading_cycle)

# Adjustment logic based on deviation and calibration rule
deviation = current_reading - base_pressure
if deviation > 0:
    adjustment_factor = 0.8
else:
    adjustment_factor = 1.1

adjusted_base = base_pressure + deviation * adjustment_factor

# Minor correction based on fixed offset sequence
correction_offsets = [0.2, -0.1, 0.3]
correction_term = sum(correction_offsets) / len(correction_offsets)

final_pressure = adjusted_base + correction_term
print(f"Result: {final_pressure}")