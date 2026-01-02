def analyze_production_cycles(raw_data):
    total_output = 0
    cycle_count = 0
    idle_periods = []
    peak_buffer = []
    efficiency_score = 0
    
    for entry in raw_data:
        status_flag = entry['status']
        output_log = entry['output']
        
        # Irrelevant preprocessing: simulate noise filtering
        filtered_log = [x for x in output_log if x > 0]  # list comprehension
        if len(filtered_log) == 0:
            idle_periods.append(len(output_log))
            continue
        
        # Simulate timestamp parsing (unused)
        timestamp_str = entry.get('timestamp', '')
        cleaned_ts = ''.join([c for c in timestamp_str if c.isdigit()])  # string method
        
        # Actual relevant logic
        cycle_total = sum(filtered_log)
        if cycle_total > 25:
            total_output += cycle_total
            cycle_count += 1
            
            # Track peaks (semi-relevant, but not used in final score)
            if cycle_total > 50:
                peak_buffer.append(cycle_total)
    
    # Red herring: unused sorting and statistics
    if peak_buffer:
        sorted_peaks = sorted(peak_buffer, reverse=True)
        median_peak = sorted_peaks[len(sorted_peaks)//2]
        average_peak = sum(sorted_peaks) / len(sorted_peaks)
    
    # Key statement
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Unused combinatorics distraction
    combo_count = 0
    for i in range(len(idle_periods)):
        for j in range(i+1, len(idle_periods)):
            if idle_periods[i] + idle_periods[j] > 10:
                combo_count += 1
    
    # Print required result
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Input data
data_sample = [
    {'status': 'active', 'output': [10, -5, 20, 15], 'timestamp': '2023-04-05T10:00'},
    {'status': 'active', 'output': [30, 40, 5], 'timestamp': '2023-04-05T11:00'},
    {'status': 'idle', 'output': [0, 0, 0, 0], 'timestamp': '2023-04-05T12:00'},
    {'status': 'active', 'output': [60, 10], 'timestamp': '2023-04-05T13:00'},
    {'status': 'active', 'output': [5, 5, 5], 'timestamp': '2023-04-05T14:00'},
    {'status': 'active', 'output': [70], 'timestamp': '2023-04-05T15:00'}
]

analyze_production_cycles(data_sample)