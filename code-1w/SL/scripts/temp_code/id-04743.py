from itertools import dropwhile

# Sensor data processing for environmental monitoring
temperature_readings = [22.3, 19.8, 24.1, 27.5, 20.0, 31.2, 28.9]
sample_shift = [0.5, -0.2, 0.3]

# Baseline calculation using central tendency
temperature_baseline = sum(temperature_readings) / len(temperature_readings)

# Identify elevated temperatures above baseline
threshold_alert = list(filter(lambda x: x > temperature_baseline, temperature_readings))

# Auxiliary transformation (irrelevant to main logic)
adjusted_samples = [x + sample_shift[i % len(sample_shift)] for i, x in enumerate(temperature_readings[:3])]

dropped_values = list(dropwhile(lambda x: x < 25, sorted(threshold_alert)))

# Final output
Result: threshold_alert