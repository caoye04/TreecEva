def analyze_performance(logs):
    total_requests = len(logs)
    successful = [log for log in logs if '200' in log]
    failure_count = total_requests - len(successful)
    
    # Extract response times from logs using string slicing
    times = [float(log.split()[-1]) for log in logs]
    avg_response_time = sum(times) / len(times)
    
    # Determine base score using conditional expression
    base_score = 100 if avg_response_time < 50 else 75 if avg_response_time < 100 else 50
    
    # Apply penalty for failures using modular arithmetic
    failure_penalty = (failure_count * 3) % 10
    final_score = base_score - failure_penalty
    
    # Adjustment based on log pattern using string method
    critical_errors = sum(1 for log in logs if log.upper().count('ERR') > 0)
    adjustment = -2 * critical_errors
    
    result = final_score + adjustment
    return result

# Simulated input logs
system_logs = [
    "REQ001 200 OK 45.2",
    "REQ002 200 OK 53.1",
    "REQ003 ERR500 Server 98.7",
    "REQ004 200 OK 32.5",
    "REQ005 ERR404 Not Found 120.3"
]

output = analyze_performance(system_logs)
print(f"Result: {output}")