def calculate_performance(results):
    base_scores = [res['value'] for res in results if res['active']]
    penalties = {k: v for k, v in results[0]['modifiers'].items()}
    adjustment = penalties.get('latency', 0) - penalties.get('throughput', 0)
    raw_total = sum(base_scores) * (0.9 + adjustment * 0.05)
    final_score = int(raw_total - (raw_total * 0.1))
    return final_score

benchmark_results = [
    {
        'value': 85,
        'active': True,
        'modifiers': {'latency': 2, 'throughput': 1}
    },
    {
        'value': 90,
        'active': True,
        'modifiers': {'latency': 3, 'throughput': 2}
    }
]

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")