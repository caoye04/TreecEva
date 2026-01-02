import math

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

def calculate_entropy(data):
    total = sum(data)
    probabilities = [(x / total) for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# Distractor variables
temp_buffer = [0] * 100
redundant_flag = True
useless_counter = 0

# Real computation begins
metrics = {
    'latency': 45,
    'throughput': 88,
    'accuracy': 94,
    'energy_efficiency': 76,
    'scalability': 81
}

weights = {
    'latency': 0.2,
    'throughput': 0.25,
    'accuracy': 0.3,
    'energy_efficiency': 0.15,
    'scalability': 0.1
}

# Misleading intermediate transformation (not used in final result)
shadow_metrics = {k: v * 1.05 for k, v in metrics.items() if v < 90}

# Conditional expression with lambda abstraction layer
calculate_bonus = lambda base: base * 1.1 if base > 90 else base * 1.02

# Simulated historical baseline (distractor)
historical_avg = {
    'latency': 50,
    'throughput': 80,
    'accuracy': 92
}

# Accumulation with filtering and adjustment
adjusted_metrics = {}
for key, value in metrics.items():
    if key == 'latency':
        adjusted_metrics[key] = 100 - value  # Invert latency
    else:
        adjusted_metrics[key] = value

# Another red herring: unused matrix operation
data_matrix = [[i + j for j in range(5)] for i in range(5)]
matrix_trace = sum(data_matrix[i][i] for i in range(5))

# Core weighted sum calculation
total_weight = sum(weights.values())
weighted_sum = sum(adjusted_metrics[metric] * weight for metric, weight in weights.items())

# Apply conditional bonus based on accuracy threshold (logical branching)
base_performance = weighted_sum / total_weight
if metrics['accuracy'] >= 90:
    base_performance = calculate_bonus(base_performance)

# Additional adjustment based on throughput
if metrics['throughput'] > 85:
    base_performance *= 1.05

# Final aggregation with string-based dispatch (unnecessary complexity)
dispatch_map = {
    'A': lambda x: x * 1.1,
    'B': lambda x: x * 1.05,
    'C': lambda x: x * 1.0
}

evaluation_tier = 'B' if base_performance > 90 else 'C'
final_score = int(dispatch_map[evaluation_tier](base_performance))

# Dead code block (never executed)
if False:
    for _ in range(10):
        useless_counter += 1
        temp_buffer[useless_counter] = useless_counter * 2

# Output result
print(f"Result: {final_score}")