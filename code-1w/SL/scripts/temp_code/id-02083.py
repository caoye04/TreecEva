from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (1001, 'temp', 23.5), (1002, 'pressure', 101.3), (1003, 'temp', 24.1),
    (1004, 'humidity', 45),   (1005, 'temp', 24.3), (1006, 'pressure', 101.5),
    (1007, 'temp', 25.0),   (1008, 'humidity', 47), (1009, 'temp', 25.1)
]

# Aggregate readings by type
data_by_type = defaultdict(list)
for ts, sensor_type, value in timestamped_readings:
    data_by_type[sensor_type].append(value)

# Extract temperature trends
temp_readings = data_by_type['temp']
temp_increases = 0
for i in range(1, len(temp_readings)):
    if temp_readings[i] > temp_readings[i-1]:
        temp_increases += 1

# Misleading: pressure analysis (not used in final result)
pressure_readings = data_by_type['pressure']
avg_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_variance = sum((p - avg_pressure) ** 2 for p in pressure_readings)

# Humidity baseline (semi-relevant but not critical)
humidity_baseline = data_by_type['humidity'][0] if data_by_type['humidity'] else 0

# Simulate processing steps
processing_log = []
for i, val in enumerate(temp_readings):
    status = 'stable'
    if i > 0 and val > temp_readings[i-1]:
        status = 'rising'
    elif i > 0 and val < temp_readings[i-1]:
        status = 'falling'
    processing_log.append((i, val, status))

# Count transitions (distractor)
transition_counter = Counter(log[2] for log in processing_log)

# Real computation begins: filter rising temps above threshold
significant_rises = list(filter(lambda x: x > 24.0, temp_readings[temp_increases % 3:]))

# Calculate total fluctuation
fluctuation = 0.0
for i in range(1, len(significant_rises)):
    fluctuation += abs(significant_rises[i] - significant_rises[i-1])

# Efficiency metric based on signal-to-noise in rising phase
noise_estimate = len([x for x in significant_rises if x < 24.8])
signal_count = len(significant_rises) - noise_estimate

# Final efficiency ratio (this is the target)
efficiency_ratio = 0.0
if noise_estimate > 0:
    efficiency_ratio = signal_count / noise_estimate
else:
    efficiency_ratio = float(signal_count)

# Dead code path (never executed, adds interference)
if avg_pressure < 90:
    efficiency_ratio *= 0.5

# Print result for verification
print(f"Result: {efficiency_ratio}")