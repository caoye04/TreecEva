from itertools import cycle

# Simulate sensor readings over time
time_cycles = 8
sensor_readings = [1.2, 0.8, 1.5, -0.3, 2.0, 1.1, 0.7, 1.8]
baseline_energy = 10
adjustment = 0
active = False
energy_threshold = 0

# Pattern for system activation (every third cycle)
system_active_pattern = cycle([False, False, True])

for i in range(time_cycles):
    reading = sensor_readings[i]
    adjustment += reading * 0.5

    if i % 3 == 0:
        active = next(system_active_pattern)

    if reading > 1.4:
        baseline_energy -= 1

    # Critical statement
    energy_threshold = max(0, baseline_energy + adjustment) if active else 0

Result: {energy_threshold}