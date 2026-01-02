def process_metrics(log, limit):
    # Initialize tracking variables
    event_count = 0
    total_duration = 0.0
    idle_time = 0
    peak_memory_usage = []
    efficiency_score = 0
    
    # Auxiliary computation - not directly impacting final score
    baseline_adjustment = sum([i**2 for i in range(5)]) / 10.0
    
    for entry in log:
        duration = entry.get('duration', 0)
        status = entry.get('status')
        memory = entry.get('memory', [])

        if duration > limit:
            total_duration += duration
            event_count += 1
            
            # Track peak memory across qualifying events
            if memory:
                peak_memory_usage.append(max(memory) if memory else 0)
        else:
            idle_time += duration  # Accumulate sub-threshold durations

        # Dummy logic to increase cognitive load
        temp_flag = True if duration > 0 and status == 'active' else False
        if temp_flag:
            baseline_adjustment += 0.1  # Red herring adjustment

    # Compute aggregate metrics
    avg_peak_memory = sum(peak_memory_usage) / len(peak_memory_usage) if peak_memory_usage else 0
    
    # Core efficiency formula (only this affects final answer)
    if event_count > 0:
        raw_efficiency = total_duration / event_count
        normalized = raw_efficiency * (1 + avg_peak_memory / 100)
        efficiency_score = int(normalized) + len(peak_memory_usage)
    
    # Irrelevant summary structure
    summary_report = {
        'events_processed': event_count,
        'total_active_time': total_duration,
        'idle_wasted': idle_time,
        'baseline': baseline_adjustment,
        'efficiency_score': efficiency_score
    }
    
    # Final assignment - key execution point
    final_output = efficiency_score
    return final_output

# Simulated input data
data_log = [
    {'duration': 12, 'status': 'active', 'memory': [34, 67, 89]},
    {'duration': 8,  'status': 'idle'},
    {'duration': 15, 'status': 'active', 'memory': [45, 92]},
    {'duration': 10, 'status': 'active', 'memory': [50, 60, 70, 95]},
    {'duration': 5,  'status': 'active'}
]
threshold = 9

# Execute
result_var = process_metrics(data_log, threshold)
print(f"Result: {result_var}")