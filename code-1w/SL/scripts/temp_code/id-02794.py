def analyze_system_metrics(response_times, error_rates, threshold=0.5):
    # Simulate analysis of system health based on response times and errors
    avg_response = sum(response_times) / len(response_times)
    high_latency_count = sum(1 for rt in response_times if rt > 2.0)
    total_errors = sum(error_rates)
    
    # Distractor: irrelevant computation for 'peak_load_estimate'
    peak_load_estimate = (max(response_times) * len(response_times)) // (min(response_times) + 0.1)
    
    # Distractor: dead code path (never executed due to condition)
    if False and total_errors > 100:
        return -1
    
    # Conditional expression used for dynamic weight adjustment
    weight = 0.8 if avg_response < 1.5 else 0.4
    
    # Composite metric calculation with weighted components
    latency_penalty = high_latency_count * 10
    error_penalty = int(total_errors * 5.5)
    base_score = 100 - latency_penalty - error_penalty
    
    # Early return not taken, but adds cognitive load
    if base_score <= 0:
        return 0
    
    adjusted_score = base_score * weight
    return max(adjusted_score, 10)


def calculate_performance_rating(log_data):
    # Extract relevant fields from structured log entries
    timestamps = [entry['ts'] for entry in log_data]
    responses = [entry['resp'] for entry in log_data]
    errors = [entry['err'] for entry in log_data]
    
    # Distractor: unused variable 'duration'
    duration = timestamps[-1] - timestamps[0] if timestamps else 0
    
    # Filter out warm-up phase (first 10% of data)
    cutoff = len(responses) // 10
    trimmed_responses = responses[cutoff:]
    trimmed_errors = errors[cutoff:]
    
    # Compute auxiliary statistic: median response time (not directly used)
    sorted_responses = sorted(trimmed_responses)
    mid = len(sorted_responses) // 2
    median_response = (sorted_responses[mid] + sorted_responses[~mid]) / 2
    
    # Use conditional expression to decide strictness level
    strict_mode = True if median_response > 1.2 else False
    eval_threshold = 0.3 if strict_mode else 0.7
    
    # Call helper function with trimmed data
    raw_performance = analyze_system_metrics(trimmed_responses, trimmed_errors, threshold=eval_threshold)
    
    # Final nonlinear transformation using bitwise influence (simulated)
    magic_factor = 17
    perturbation = (hash(str(raw_performance)) ^ magic_factor) & 0xF  # bitmask to get low 4 bits
    final_score = int(raw_performance + (perturbation * 0.25))
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Simulated log data (deterministic)
data_log = [
    {'ts': 100, 'resp': 0.8, 'err': 0.1},
    {'ts': 101, 'resp': 1.1, 'err': 0.2},
    {'ts': 102, 'resp': 2.3, 'err': 0.6},
    {'ts': 103, 'resp': 0.9, 'err': 0.1},
    {'ts': 104, 'resp': 1.7, 'err': 0.3},
    {'ts': 105, 'resp': 2.5, 'err': 0.8},
    {'ts': 106, 'resp': 1.3, 'err': 0.1},
    {'ts': 107, 'resp': 3.1, 'err': 1.1},
    {'ts': 108, 'resp': 0.7, 'err': 0.0},
    {'ts': 109, 'resp': 1.9, 'err': 0.4},
    {'ts': 110, 'resp': 2.2, 'err': 0.7},
    {'ts': 111, 'resp': 1.0, 'err': 0.1},
]

# Execute main function
calculate_performance_rating(data_log)