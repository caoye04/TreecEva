def calculate_processing_efficiency(data_streams):
    # Initialize processing metrics
    raw_processing_times = [45, 28, 67, 34, 52]
    buffer_sizes = [128, 256, 64, 512, 192]
    
    # Calculate normalized processing times (distractor - not used in final answer)
    normalized_times = [time * 1.25 for time in raw_processing_times]
    
    # Filter streams and calculate actual processing durations
    active_streams = [stream for stream in data_streams if stream['status'] == 'active']
    processing_durations = [stream['duration'] for stream in active_streams]
    
    # Apply efficiency factors and sort
    efficiency_factors = [0.85, 1.15, 0.95, 1.05, 0.90]
    adjusted_times = [duration * factor for duration, factor in zip(processing_durations, efficiency_factors)]
    sorted_times = sorted(adjusted_times)
    
    # Calculate items processed with lambda function
    processed_items = list(map(lambda x: int(x // 10), adjusted_times))
    
    # Final calculation (key statement)
    final_processing_time = sorted_times[-1] - processed_items[1]
    
    # Distractor calculation that doesn't affect final result
    unused_metric = sum(buffer_sizes) // len(buffer_sizes)
    
    print(f"Result: {final_processing_time}")
    return final_processing_time

# Input data
stream_data = [
    {'id': 1, 'status': 'active', 'duration': 38},
    {'id': 2, 'status': 'inactive', 'duration': 25},
    {'id': 3, 'status': 'active', 'duration': 42},
    {'id': 4, 'status': 'active', 'duration': 31},
    {'id': 5, 'status': 'active', 'duration': 29}
]

calculate_processing_efficiency(stream_data)