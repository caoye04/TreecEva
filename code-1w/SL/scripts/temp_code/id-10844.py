def analyze_response_time(rt):
    return rt < 100

def is_valid_log(entry):
    return isinstance(entry, dict) and 'timestamp' in entry

def calculate_performance(logs):
    valid_entries = [e for e in logs if is_valid_log(e)]
    
    # Irrelevant aggregation (distractor)
    total_duration = sum([e.get('duration', 0) for e in valid_entries])
    avg_duration = total_duration / len(valid_entries) if valid_entries else 0
    
    # Semi-relevant preprocessing
    response_times = [e.get('response_time', 200) for e in valid_entries]
    fast_responses = [rt for rt in response_times if analyze_response_time(rt)]
    
    # Core logic: count successful patterns
    pattern_count = 0
    for i in range(1, len(response_times)):
        if response_times[i] < response_times[i-1]:
            pattern_count += 1
    
    # Distractor: unused complex calculation
    outlier_count = len([rt for rt in response_times if rt > 150])
    penalty_factor = 0.9 if outlier_count > 3 else 1.0
    
    # Key computation
    base_score = len(fast_responses) * 10
    bonus = pattern_count * 5 if pattern_count > 4 else 0
    final_score = base_score + bonus
    
    # Red herring variable
    debug_info = {'base': base_score, 'bonus': bonus, 'patterns': pattern_count}
    
    return final_score

# Simulated benchmark logs
benchmark_logs = [
    {'timestamp': 1, 'response_time': 120, 'duration': 45},
    {'timestamp': 2, 'response_time': 95, 'duration': 50},
    {'timestamp': 3, 'response_time': 80, 'duration': 40},
    {'timestamp': 4, 'response_time': 70, 'duration': 35},
    {'timestamp': 5, 'response_time': 110, 'duration': 55},
    {'timestamp': 6, 'response_time': 60, 'duration': 30},
    {'timestamp': 7, 'response_time': 50, 'duration': 25},
    {'timestamp': 8, 'response_time': 40, 'duration': 20},
    {'timestamp': 9, 'response_time': 130, 'duration': 60},
    {'timestamp': 10, 'response_time': 30, 'duration': 15}
]

# Execution point of interest
final_score = calculate_performance(benchmark_logs)
print(f"Target result: {final_score}")