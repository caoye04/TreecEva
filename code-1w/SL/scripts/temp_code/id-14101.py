from itertools import combinations

# Simulate a performance benchmark analyzer for code optimization tasks
def analyze_response_times(raw_logs):
    parsed = [float(x.split()[1]) for x in raw_logs if 'ms' in x]
    filtered = [t for t in parsed if t > 0]
    avg_time = sum(filtered) / len(filtered) if filtered else 0
    return avg_time

def extract_key_metrics(log_lines):
    metrics = {}
    temp_store = []
    for line in log_lines:
        if 'ERROR' in line:
            temp_store.append(0)
        elif 'SUCCESS' in line:
            val = float(line.split(':')[-1].strip())
            temp_store.append(val)
    metrics['success_count'] = len([x for x in temp_store if x > 0])
    metrics['total_attempts'] = len(temp_store)
    metrics['raw_values'] = temp_store
    return metrics

def calculate_consistency(data_list):
    diffs = [abs(data_list[i] - data_list[i-1]) for i in range(1, len(data_list))]
    consistency_score = 100 - (sum(diffs) / len(diffs) * 10) if diffs else 100
    noise_factor = 0.98  # minor adjustment factor (distractor)
    adjusted = consistency_score * noise_factor  # not actually used later
    return consistency_score

def calculate_performance(dataset):
    # Parse logs
    response_time = analyze_response_times(dataset['timing_logs'])
    
    # Extract success metrics
    results = extract_key_metrics(dataset['result_logs'])
    success_rate = results['success_count'] / results['total_attempts'] if results['total_attempts'] else 0
    
    # Compute stability from timing
    timing_stability = calculate_consistency(results['raw_values'])
    
    # Generate auxiliary distraction data
    pairs = list(combinations([1, 2, 3, 4], 2))
    pair_sum = sum(a + b for a, b in pairs)  # irrelevant computation
    dummy_dict = {i: i**2 for i in range(5)}
    dummy_lookup = dummy_dict.get(10, 0)  # dead-end lookup
    
    # Weighted performance score
    time_weight = 0.4
    rate_weight = 0.35
    stability_weight = 0.25
    
    normalized_time = max(0, 100 - (response_time * 2))  # assume max 50ms ideal
    
    # Final composite score
    final_score = (
        normalized_time * time_weight +
        success_rate * 100 * rate_weight +
        timing_stability * stability_weight
    )
    
    # Extra unused variables to increase cognitive load
    debug_info = {'processed': True, 'version': '2.1'}
    calibration_offset = 0.034  # never applied
    
    return int(round(final_score))

# Input dataset
benchmark_data = {
    'timing_logs': [
        'Request completed: 12.5 ms',
        'Processing delay: 15.0 ms',
        'Response time: 10.3 ms',
        'Latency: 13.7 ms',
        'Reconnect: 16.2 ms'
    ],
    'result_logs': [
        'STATUS: SUCCESS : 1',
        'STATUS: SUCCESS : 1',
        'STATUS: ERROR : failed precondition',
        'STATUS: SUCCESS : 1',
        'STATUS: SUCCESS : 1',
        'STATUS: SUCCESS : 1',
        'STATUS: ERROR : timeout',
        'STATUS: SUCCESS : 1'
    ]
}

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")