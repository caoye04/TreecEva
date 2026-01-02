def calculate_performance(op_list, metric_weights):
    weighted_sum = sum(op * w for op, w in zip(op_list, metric_weights))
    normalization = len(op_list)
    return weighted_sum / normalization

# System performance metrics (ops: throughput, latency, energy)
operations = [85, 92, 78]
weights = [0.4, 0.3, 0.3]  # Emphasizing balanced efficiency

# Irrelevant auxiliary variables (minimal distraction - intervention level 4)
temp_log = "Performance logged at UTC"
max_capacity = 100

metric_lambda = lambda x: round(x * 1.05, 2)  # Potential scaling (not used directly)
adjusted_ops = list(map(metric_lambda, operations))

# Key computation
efficiency_score = calculate_performance(operations, weights)

Result: efficiency_score