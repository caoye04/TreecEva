import heapq
import statistics

def process_sensor_data(raw_readings):
    # Tokenize and parse each reading
    parsed_data = [
        {
            'timestamp': int(reading.split(',')[0]),
            'value': float(reading.split(',')[1]),
            'device_id': reading.split(',')[2]
        }
        for reading in raw_readings
    ]
    
    # Keep only last 5 timestamps using a min-heap as a max-heap (negating values)
    window_heap = []
    
    for entry in parsed_data:
        heapq.heappush(window_heap, (-entry['timestamp'], entry))
        if len(window_heap) > 5:
            heapq.heappop(window_heap)
    
    # Extract the entries in the window
    recent_entries = [entry for _, entry in window_heap]
    
    # Normalize values: subtract minimum then divide by range
    values = [e['value'] for e in recent_entries]
    min_val, max_val = min(values), max(values)
    normalized_values = [(v - min_val) / (max_val - min_val) if max_val != min_val else 0 for v in values]
    
    # Filter out outliers using interquartile range method
    if len(normalized_values) < 2:
        filtered_values = normalized_values
    else:
        sorted_vals = sorted(normalized_values)
        q1 = statistics.median(sorted_vals[:len(sorted_vals)//2])
        q3 = statistics.median(sorted_vals[(len(sorted_vals)+1)//2:])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        filtered_values = [v for v in normalized_values if lower_bound <= v <= upper_bound]
    
    # Calculate mean of filtered values
    if not filtered_values:
        return 0
    
    aggregated_mean = sum(filtered_values) / len(filtered_values)
    return aggregated_mean

# Simulated sensor data: "timestamp,value,device_id"
sensor_readings = [
    "1000,23.5,D1",
    "1001,24.1,D2",
    "1002,22.8,D1",
    "1003,45.0,D3",  # Outlier
    "1004,23.9,D2",
    "1005,24.0,D1",
    "1006,23.7,D3",
    "1007,24.2,D2"
]

aggregated_mean = process_sensor_data(sensor_readings)
print(f"Result: {aggregated_mean}")