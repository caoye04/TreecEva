from itertools import compress

def calculate_performance(results):
    # Extract success flags and timings
    successes = [r[0] for r in results]
    times = [r[1] for r in results]

    # Compute average time of successful runs
    valid_times = [t for t, s in zip(times, successes) if s]
    avg_time = sum(valid_times) / len(valid_times) if valid_times else 0.0

    # Performance score: base count of successes with time penalty
    base_score = sum(successes)
    time_penalty = avg_time * 0.1
    raw_score = base_score - time_penalty

    # Apply non-linear boost if more than half succeeded
    boosted = raw_score * 1.5 if base_score > len(results) // 2 else raw_score

    # Normalize to integer scale
    return int(round(boosted * 10))

# Benchmark test outcomes: (success, execution_time_ms)
benchmark_results = [
    (True, 120),
    (True, 80),
    (False, 200),
    (True, 90),
    (True, 110),
    (False, 150)
]

# Irrelevant auxiliary data (minimal distraction)
config = {'version': '2.1', 'debug': False}

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")