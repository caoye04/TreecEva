from collections import defaultdict

def process_sensor_data(raw_readings):
    window_size = 3
    processed_signals = []
    
    # Apply sliding window transformation
    for i in range(len(raw_readings) - window_size + 1):
        window = raw_readings[i:i+window_size]
        # Calculate weighted average with bit shifting
        weighted_sum = sum(val << (window_size-j-1) for j, val in enumerate(window))
        processed_signals.append(weighted_sum >> 1)
    
    return processed_signals

def aggregate_calibration(signals_matrix):
    aggregated_signal_strength = 0
    sensor_weights = [1, 2, 3]
    
    # Nested loop processing with conditional accumulation
    for sensor_idx, signals in enumerate(signals_matrix):
        for signal in signals:
            if signal & 1:  # Check if odd (bitwise AND)
                adjusted_signal = signal ^ (sensor_idx << 2)  # XOR with shifted index
                aggregated_signal_strength += adjusted_signal * sensor_weights[sensor_idx % len(sensor_weights)]
            else:
                aggregated_signal_strength -= signal >> 1  # Right shift for even values
    
    return aggregated_signal_strength

# Main execution
sensor_readings_collection = [
    [15, 22, 8, 31, 14],
    [9, 26, 17, 4, 19],
    [33, 12, 7, 28, 5]
]

# Process each sensor's data
processed_sensor_data = [process_sensor_data(readings) for readings in sensor_readings_collection]

# Calculate final calibration value
aggregated_signal_strength = aggregate_calibration(processed_sensor_data)

print(f"Result: {aggregated_signal_strength}")