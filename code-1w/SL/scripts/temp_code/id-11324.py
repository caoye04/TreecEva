def analyze_signal_data():
    raw_signal = [12, -5, 8, 19, -13, 7, 4, -6, 11]
    threshold = 6
    
    # Normalize signal by shifting baseline
    normalized = [x + 3 for x in raw_signal]
    
    # Extract segments above threshold
    above_threshold = [x for x in normalized if x > threshold]
    
    # Simulate signal reversal for echo cancellation
    reversed_segments = above_threshold[::-1]
    
    # Compute diagnostic sum
    filtered_sum = sum(reversed_segments)
    
    # Irrelevant metadata (minimal distraction)
    sample_rate = 44100
    device_id = "SIG-2023"
    
    print(f"Result: {filtered_sum}")

analyze_signal_data()