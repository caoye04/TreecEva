def process_metrics(logs):
    base_count = len(logs)
    error_filter = lambda x: 'ERROR' in x
    warning_filter = lambda x: 'WARN' in x
    
    errors = list(filter(error_filter, logs))
    warnings = list(filter(warning_filter, logs))
    
    error_ratio = len(errors) / base_count if base_count else 0
    warning_ratio = len(warnings) / base_count if base_count else 0
    
    # Secondary computation with conditional expression
    severity_bonus = 10 if error_ratio > 0.2 else 5
    efficiency_score = (base_count - len(warnings)) * (1 - error_ratio) + severity_bonus
    
    temp_variable_x = 999  # Irrelevant variable (minimal interference)
    final_output = efficiency_score
    return final_output

# Input data
log_data = [
    'INFO: System online',
    'ERROR: Disk full',
    'WARN: High memory usage',
    'ERROR: Disk full',
    'INFO: User login',
    'WARN: CPU spike detected',
    'WARN: Network latency'
]

result = process_metrics(log_data)
print(f"Result: {result}")