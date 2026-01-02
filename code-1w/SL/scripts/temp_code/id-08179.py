def calculate_final_score(stats, thresholds):
    raw_score = sum(stats[metric] for metric in ['accuracy', 'latency', 'throughput'])
    bonus = 10 if all(stats[metric] >= thresholds[metric] for metric in thresholds) else 0
    penalty = 5 if stats['errors'] > 0 else 0
    return raw_score + bonus - penalty

# System performance metrics
telemetry_data = {
    'accuracy': 88,
    'latency': 45,
    'throughput': 120,
    'errors': 1
}

thresholds = {
    'accuracy': 85,
    'latency': 50,
    'throughput': 100
}

# Extract relevant stats
stats = {
    'accuracy': telemetry_data['accuracy'],
    'latency': telemetry_data['latency'],
    'throughput': telemetry_data['throughput'],
    'errors': telemetry_data['errors']
}

final_score = calculate_final_score(stats, thresholds)
print(f"Target result: {final_score}")