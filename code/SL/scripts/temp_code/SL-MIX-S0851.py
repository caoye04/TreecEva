data_stream = [12, 45, 23, 67, 89, 34, 56, 78]
window_size = 3
processed_values = []

for i in range(len(data_stream) - window_size + 1):
    window = data_stream[i:i + window_size]
    window_avg = sum(window) / len(window)
    processed_values.append(round(window_avg, 2))

# Some processing metadata
meta_info = {"source": "sensor_array", "sampling_rate": 100}

final_result = processed_values[-1]
print(f"Result: {final_result}")