def calculate_performance(results):
    total = 0
    penalties = {"timeout": 2, "error": 3, "warning": 1}
    status_weights = {"pass": 5, "fail": -2}

    for idx, (status, issue) in enumerate(zip(results['statuses'], results['issues'])):
        base = status_weights.get(status, 0)
        penalty = penalties.get(issue, 0)
        adjustment = base - penalty
        total += adjustment

        # Irrelevant tracking variable (minimal distraction)
        _ = f"Step {idx + 1}: {adjustment} -> Running total: {total}"

    return total

# Input data
benchmark_results = {
    'statuses': ['pass', 'pass', 'fail', 'pass', 'fail'],
    'issues': ['none', 'warning', 'timeout', 'none', 'error']
}

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")