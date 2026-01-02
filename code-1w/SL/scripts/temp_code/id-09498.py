def process_metrics(log, thresh):
    entry_count = len(log)
    valid_entries = [e for e in log if e['status'] == 'OK']
    error_entries = [e for e in log if e['status'] != 'OK']
    temp_sum = sum(e['value'] for e in valid_entries)
    avg_value = temp_sum / len(valid_entries) if valid_entries else 0
    
    # Distractor: irrelevant computation on timestamps
    timestamps = [e['timestamp'] for e in log]
    time_range = max(timestamps) - min(timestamps) if timestamps else 0
    time_density = len(timestamps) / (time_range + 1)
    
    # Distractor: unused helper function
    def smooth_data(seq):
        return [sum(seq[max(0,i-1):i+2]) / len(seq[max(0,i-1):i+2]) for i in range(len(seq))]
    
    # Semi-relevant transformation
    clipped_values = [min(v['value'], thresh) for v in valid_entries]
    bonus_factor = 1.5 if len(valid_entries) > 3 else 1.0
    penalty = 0.9 if any(e['retry'] for e in error_entries) else 1.0
    
    # Core logic with lambda and conditional expression
    transform = lambda x: x ** 0.5 if x > thresh else x * 0.1
    transformed = sum(transform(v['value']) for v in valid_entries)
    
    # State tracking with intermediate variables
    base_score = transformed * bonus_factor * penalty
    adjustment = 10 if time_density > 2 else 5
    efficiency_score = base_score + adjustment  # Key variable
    
    # Dead code path (never executed due to condition)
    if entry_count < 0:
        efficiency_score *= 0.8
    
    # Final output assignment
    final_output = efficiency_score
    return final_output

# Input data
data_log = [
    {'value': 25, 'status': 'OK', 'retry': False, 'timestamp': 10},
    {'value': 16, 'status': 'OK', 'retry': False, 'timestamp': 12},
    {'value': 9, 'status': 'ERROR', 'retry': True, 'timestamp': 15},
    {'value': 36, 'status': 'OK', 'retry': False, 'timestamp': 18},
    {'value': 49, 'status': 'OK', 'retry': False, 'timestamp': 20},
    {'value': 64, 'status': 'OK', 'retry': False, 'timestamp': 25}
]
threshold = 20

result = process_metrics(data_log, threshold)
efficiency_score = result
print(f"Result: {efficiency_score}")