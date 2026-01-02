def process_metrics(log_entries, limit):
    total_entries = len(log_entries)
    valid_count = 0
    error_accumulator = 0
    warning_flags = []
    
    # Secondary tracking for irrelevant diagnostics
    diagnostic_sum = sum([len(entry['message']) for entry in log_entries])
    avg_message_length = diagnostic_sum / total_entries if total_entries > 0 else 0
    
    temp_scale = 1.0 if avg_message_length > 50 else 0.5
    scaling_factor = temp_scale * 2
    
    for i, entry in enumerate(log_entries):
        code = entry['code']
        severity = entry['severity']
        message = entry['message']
        
        # Distractor: track warnings but not used in final logic
        if 'warning' in message.lower():
            warning_flags.append(i)
        
        # Actual filtering logic
        if severity >= limit:
            valid_count += 1
            if code % 2 == 1:
                error_accumulator += code * (i + 1)
    
    # Complex conditional expression with zip and enumerate
    adjustments = [
        (index + 1) * val['code'] 
        for index, val in enumerate(log_entries) 
        if val['severity'] > limit - 1
    ]
    adjustment_total = sum(adjustments) if adjustments else 0
    
    # Semi-relevant transformation
    transformed_data = []
    for a, b in zip(log_entries, reversed(log_entries)):
        if a['code'] > b['code']:
            transformed_data.append(a['severity'] - b['severity'])
    
    # Core calculation chain
    base_metric = valid_count * 100
    penalty = error_accumulator // 5 if error_accumulator > 0 else 0
    bonus = len(warning_flags) // 3  # Unused influence attempt
    efficiency_score = base_metric - penalty + adjustment_total // 10
    
    # Red herring computation
    phantom_score = 0
    for x in range(1, min(total_entries, 10)):
        if x % 2 == 0:
            phantom_score += x ** 2
    
    # Final assignment
    final_output = efficiency_score + len(transformed_data)
    return final_output

# Input data
log_data = [
    {'code': 101, 'severity': 3, 'message': 'System reboot required'},
    {'code': 205, 'severity': 5, 'message': 'Critical failure in module A'},
    {'code': 107, 'severity': 4, 'message': 'Warning: high memory usage'},
    {'code': 302, 'severity': 6, 'message': 'Immediate shutdown initiated'},
    {'code': 103, 'severity': 2, 'message': 'Minor configuration issue'}
]

threshold = 4
result_var = process_metrics(log_data, threshold)
print(f"Result: {result_var}")