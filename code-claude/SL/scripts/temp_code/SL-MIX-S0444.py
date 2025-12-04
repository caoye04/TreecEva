import itertools

def process_signal(raw_data):
    # Process the signal data (not actually used in final calculation)
    return [x * 0.8 + 2 for x in raw_data]

# Sensor readings from different stations
sensor_stations = [
    [12, 15, 9, 3, 8],
    [7, 10, 6, 14, 11],
    [5, 13, 4, 16, 2]
]

# Configuration parameters
threshold_values = [8, 10, 12]
decay_factor = 0.9
boost_value = 5

# Flatten the sensor readings
all_readings = list(itertools.chain.from_iterable(sensor_stations))

# Sort the readings for analysis (not directly used in final calculation)
sorted_readings = sorted(all_readings)

# Calculate some statistics (not directly used in final calculation)
average_reading = sum(all_readings) / len(all_readings)
median_reading = sorted_readings[len(sorted_readings) // 2]

# Apply primary threshold filter
filtered_by_threshold = [reading for reading in all_readings if reading >= threshold_values[1]]

# Apply secondary processing
processed_signals = []
for reading in filtered_by_threshold:
    # Apply conditional processing based on reading value
    if reading > threshold_values[2]:
        adjusted = reading * decay_factor + boost_value
    else:
        adjusted = reading * decay_factor
    processed_signals.append(adjusted)

# Extract specific signal segments using slicing
signal_segment_a = processed_signals[:2]  # First two signals
signal_segment_b = processed_signals[-3:]  # Last three signals

# Apply different processing to each segment (segment_a not used in final result)
enhanced_segment_a = [x + 2 for x in signal_segment_a]
filtered_segment_b = [x for x in signal_segment_b if x > 14]

# Combine relevant signals
filtered_signals = processed_signals[2:-3] + filtered_segment_b

# Calculate final signal strength
final_signal_strength = sum(filtered_signals)

print(f"Result: {final_signal_strength}")