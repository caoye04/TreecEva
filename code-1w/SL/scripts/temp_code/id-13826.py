def analyze_system_load(loads):
    # Irrelevant function: analyzes system load but not used in main logic
    avg = sum(loads) / len(loads)
    peak = max(loads)
    return [x for x in loads if x > avg]

# Unused data structures as red herrings
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
error_logs = set(['warning', 'info', 'debug'])
system_uptime = {'server_a': 99.7, 'server_b': 98.4, 'server_c': 99.1}

# Core data for evaluation
metrics = [0.88, 0.76, 0.91, 0.67, 0.83]
benchmark_weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distractor: complex-looking but unused weight normalization
normalized_weights = []
weight_sum = sum(benchmark_weights)
for w in benchmark_weights:
    normalized_weights.append(round(w / weight_sum, 4))

# Unused recursive function to mislead
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n-2)

# Decoy calculation with intermediate results
preliminary_scores = []
for i, m in enumerate(metrics):
    adjusted = m * (i + 1) ** 0.5
    preliminary_scores.append(round(adjusted, 3))

# Real logic buried among distractions
def apply_weight(m, w):
    return m * w

def evaluate_performance(data, weights):
    total = 0.0
    # Use of zip and enumerate together (required Python features)
    for idx, (val, weight) in enumerate(zip(data, weights)):
        if idx % 2 == 0:
            total += apply_weight(val, weight) * 1.1  # Boost even indices
        else:
            total += apply_weight(val, weight) * 0.9  # Reduce odd indices
    
    # Additional adjustment based on cumulative pattern
    correction_factor = 1.0
    cumsum = 0
    for i, v in enumerate(metrics):
        cumsum += v
        if cumsum > 2.5 and i > 2:
            correction_factor = 0.95
            break
    
    return round(total * correction_factor, 6)

# Secondary distractor: string processing unrelated to final result
diagnostic_trace = "cpu=ok|mem=high|disk=ok|net=low"
trace_parts = diagnostic_trace.split('|')
status_dict = {}
for part in trace_parts:
    k, v = part.split('=')
    status_dict[k] = v

# Another dead-end list comprehension
anomalies = [i for i, x in enumerate(preliminary_scores) if x < 0.75]

# Key computation
final_score = evaluate_performance(metrics, benchmark_weights)

# Output required result
print(f"Target result: {final_score}")