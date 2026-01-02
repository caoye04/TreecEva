from functools import reduce

# Simulate analysis of access patterns in a secure logging system
def analyze_pattern(log_entries):
    # Extract durations (in seconds) from log entries using slicing
    durations = [entry[1] for entry in log_entries]
    
    # Filter out entries below threshold using lambda
    valid_durations = list(filter(lambda x: x > 30, durations))
    
    # Compute combinatorial weight: sum of combinations C(n,2) for n = len(valid_durations)
    n = len(valid_durations)
    combinations = n * (n - 1) // 2 if n >= 2 else 0
    
    # Secondary metric: average duration (distraction, not used in final result)
    avg_duration = sum(durations) / len(durations) if durations else 0
    
    # Apply weighting factor based on pattern density
    density_factor = 2 if combinations > 5 else 1
    result = combinations * density_factor
    
    return result

# Sample log data: (timestamp, duration, status)
data = [
    (1623456780, 15, 'FAIL'),
    (1623456800, 45, 'SUCCESS'),
    (1623456820, 60, 'SUCCESS'),
    (1623456840, 25, 'FAIL'),
    (1623456860, 90, 'SUCCESS'),
    (1623456880, 35, 'SUCCESS')
]

# Execute analysis
result = analyze_pattern(data)
print(f"Target result: {result}")