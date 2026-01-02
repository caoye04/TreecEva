from itertools import compress

def calculate_performance(results):
    # Filter valid test cases (duration > 0 and success)
    valid_durations = [r[1] for r in results if r[2] and r[1] > 0]
    
    # Compute efficiency score using harmonic mean concept
    if not valid_durations:
        return 0.0
    
    inverse_sum = sum(map(lambda x: 1/x, valid_durations))
    harmonic_mean = len(valid_durations) / inverse_sum
    
    # Apply performance bonus based on number of successful tests
    bonus_factor = 1.0 + min(len(valid_durations) * 0.05, 0.5)  # Cap at 50%
    base_score = harmonic_mean * 10
    final_score = base_score * bonus_factor
    
    # Irrelevant distraction: unused variable
    temp_debug_log = [f'Test {i}: {r}' for i, r in enumerate(results)]
    
    return final_score

# Benchmark test results: (test_id, duration_ms, success_flag)
benchmark_results = [
    (101, 50.0, True),
    (102, 40.0, True),
    (103, 0.0, False),  # Invalid due to zero duration
    (104, 25.0, True),
    (105, 35.0, True),
    (106, 45.0, False), # Failed execution
    (107, 30.0, True)
]

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")