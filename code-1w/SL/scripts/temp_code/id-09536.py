def calculate_performance(flags, data_map):
    base = len(flags)
    multiplier = data_map['efficiency'] * (1 + data_map['accuracy'])
    adjustment = sum([data_map[k] for k in flags if k in data_map])
    return int((base * multiplier) + adjustment)

# System performance metrics
evaluation_metrics = {
    'efficiency': 2.5,
    'accuracy': 0.8,
    'latency': 45,
    'throughput': 120,
    'reliability': 3.2
}

# Optional bonus conditions triggered
bonus_conditions = ['efficiency', 'accuracy', 'reliability']

# Irrelevant string processing (distractor with moderate relevance)
diagnostic_log = "System check passed at 2023-12-05".replace(' ', '_').upper()
log_length = len(diagnostic_log)

# Main computation
temp_result = evaluation_metrics['latency'] // 5
final_score = calculate_performance(bonus_conditions, evaluation_metrics)
print(f"Result: {final_score}")