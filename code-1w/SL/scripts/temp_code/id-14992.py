def process_metrics(records):
    baseline = 100
    adjustment_factor = 0.95
    temp_buffer = []
    cumulative_shift = 0

    for record in records:
        raw_value = record['value']
        timestamp = record['time']
        
        # Irrelevant time-based filter (never triggered in data)
        if timestamp < 1000:
            offset = 5
        else:
            offset = 0
        
        adjusted = raw_value * adjustment_factor + offset
        temp_buffer.append(adjusted)

        # Side computation with no impact on final result
        anomaly_check = abs(adjusted - baseline) > 20
        if anomaly_check:
            cumulative_shift += 1  # Dead logic, never used

    # Real processing path
    filtered_data = [x for x in temp_buffer if x > 50]  # List comprehension
    sliced_data = filtered_data[1:4]  # Slicing operation
    
    aggregate = sum(sliced_data)
    sample_count = len(sliced_data)
    
    # Extraneous calculation
    avg_deviation = sum(abs(x - 75) for x in sliced_data) / sample_count if sample_count > 0 else 0
    
    efficiency_score = aggregate / sample_count if sample_count > 0 else 0
    
    # Dummy state tracking
    status_log = {'processed': sample_count, 'anomalies': cumulative_shift}
    final_output = efficiency_score * 1.1  # Final transformation

    return final_output

# Input data
data_stream = [
    {'value': 80, 'time': 2000},
    {'value': 90, 'time': 2001},
    {'value': 70, 'time': 2002},
    {'value': 60, 'time': 2003},
    {'value': 40, 'time': 2004}  # Will be filtered out (<= 50)
]

data_slice = data_stream
result = process_metrics(data_slice)
efficiency_score = result / 1.1  # Reverse final transformation to get true efficiency_score
print(f"Result: {efficiency_score}")