from itertools import compress

def calculate_performance(results):
    # Extract success status and latency values
    success_flags = [entry['success'] for entry in results]
    latencies = [entry['latency'] for entry in results]

    # Compute average latency only for successful executions
    valid_latencies = list(compress(latencies, success_flags))
    avg_latency = sum(valid_latencies) / len(valid_latencies) if valid_latencies else 0.0

    # Performance penalty based on average latency
    penalty = 10 if avg_latency > 50 else 5

    # Count total successful runs using dictionary aggregation
    stats = {'successful': sum(success_flags), 'total': len(results)}
    success_rate = stats['successful'] / stats['total']

    # Final score calculation using conditional expression
    base_score = 100 if success_rate >= 0.8 else 75
    final_score = base_score - penalty

    return final_score

# Benchmark test results from system performance trials
benchmark_results = [
    {'success': True,  'latency': 45},
    {'success': True,  'latency': 55},
    {'success': False, 'latency': 120},
    {'success': True,  'latency': 40},
    {'success': True,  'latency': 60},
    {'success': True,  'latency': 35},
    {'success': False, 'latency': 200},
    {'success': True,  'latency': 50}
]

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")