import math

def process_metrics(log_entries):
    total_entries = len(log_entries)
    valid_records = [e for e in log_entries if e['status'] == 'OK']
    error_count = total_entries - len(valid_records)

    # Irrelevant aggregation: network latency stats (not used in final score)
    latency_values = [e['metrics']['latency'] for e in log_entries if 'latency' in e['metrics']]
    avg_latency = sum(latency_values) / len(latency_values) if latency_values else 0.0
    peak_latency = max(latency_values) if latency_values else 0.0

    # Core computation: throughput and consistency
    throughput_list = [e['metrics']['requests'] for e in valid_records]
    total_throughput = sum(throughput_list)
    consistency_ratio = len(throughput_list) / total_entries if total_entries > 0 else 0.0

    # Secondary filter: high-load scenarios
    high_load = list(filter(lambda x: x['context']['load_level'] > 7, valid_records))
    load_stress_factor = len(high_load) * 0.5

    # Dummy calculation: memory pressure index (unused)
    mem_pressure = [e['metrics']['memory'] for e in log_entries]
    memory_index = sum(m**0.5 for m in mem_pressure) / len(mem_pressure) if mem_pressure else 0.0

    # Efficiency formula: combines throughput, consistency, and penalizes errors
    base_efficiency = total_throughput * consistency_ratio
    penalty = math.log(1 + error_count) * 10
    efficiency_score = base_efficiency - penalty - load_stress_factor

    # Red herring: unused derived metrics
    normalized_efficiency = efficiency_score / (total_throughput or 1)
    stability_bonus = 10 if all(t > 50 for t in throughput_list) else 0

    final_output = efficiency_score
    return final_output

# Simulated data input
data_log = [
    {
        'status': 'OK',
        'metrics': {'requests': 120, 'latency': 45, 'memory': 256},
        'context': {'load_level': 8}
    },
    {
        'status': 'ERROR',
        'metrics': {'latency': 120, 'memory': 512},
        'context': {'load_level': 5}
    },
    {
        'status': 'OK',
        'metrics': {'requests': 95, 'latency': 60, 'memory': 384},
        'context': {'load_level': 6}
    },
    {
        'status': 'OK',
        'metrics': {'requests': 130, 'latency': 40, 'memory': 200},
        'context': {'load_level': 9}
    },
    {
        'status': 'OK',
        'metrics': {'requests': 110, 'latency': 50, 'memory': 300},
        'context': {'load_level': 4}
    }
]

result = process_metrics(data_log)
print(f"Result: {result}")