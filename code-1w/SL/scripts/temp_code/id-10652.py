import itertools

# Simulated system performance metrics from a distributed task scheduler
def collect_metrics(base_load, multiplier=1.0):
    raw_data = [base_load * (i + 1) ** 0.5 for i in range(5)]
    offset_correction = sum(x % 2 for x in raw_data)
    adjusted = [x + offset_correction for x in raw_data]
    return adjusted

# Legacy function - not used but looks relevant
def calculate_efficiency(nodes, utilization):
    efficiency = 0.0
    for n in nodes:
        if n > 5:
            efficiency += utilization * 0.8
        else:
            efficiency += utilization * 0.3
    return efficiency

# Auxiliary transformation: applies noise filtering
def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    filtered = [x for x in data if abs(x - median_val) / median_val < threshold]
    padding = [-1] * (len(data) - len(filtered))
    return filtered + padding  # Deliberate red herring: unused later

# Weight adjustment using bit manipulation (obscure but valid)
def adjust_weights(w):
    shifted = [(w[i] << 1) ^ 3 for i in range(len(w))]
    normalized = [s % 7 + 1 for s in shifted]  # Nonlinear rescaling
    total = sum(normalized)
    return [round(n / total, 6) for n in normalized]

# Secondary scoring (distractor: looks important but unused)
def compute_legacy_rank(score_list):
    inverted = [100 / (1 + s) for s in score_list]
    rank = sum(inverted) / len(inverted)
    return int(rank * 10)

# Main aggregation logic
def aggregate_performance(metrics, weights):
    # Apply logarithmic scaling to dampen high values
    scaled_metrics = [round(m ** 0.7, 6) for m in metrics]
    
    # Irrelevant reshaping operation (distractor)
    reshaped = list(itertools.chain.from_iterable(
        [(s * 0.95, s * 1.05) for s in scaled_metrics]
    ))
    mid_index = len(reshaped) // 2
    left_half = reshaped[:mid_index]
    right_half = reshaped[mid_index:]
    crossover = [left_half[i] * right_half[-i-1] for i in range(len(left_half))]
    
    # Actual computation path
    weighted_sum = sum(scaled_metrics[i] * weights[i] for i in range(len(weights)))
    penalty_factor = 0.9 if len(metrics) > 4 else 1.0
    
    # Dummy control flow with misleading assignment
    if weighted_sum > 100:
        temp_result = weighted_sum * 0.85
    elif weighted_sum > 50:
        temp_result = weighted_sum * 0.9
    else:
        temp_result = weighted_sum
    
    final_value = weighted_sum * penalty_factor  # This is the real result
    return round(final_value, 6)

# Unused diagnostic function (dead code path)
def diagnose_pipeline(internals):
    report = {}
    for key, val in internals.items():
        report[key] = {
            'mean': sum(val)/len(val),
            'peak': max(val),
            'entropy': len(set(val))
        }
    return report

# Initialization parameters
task_load = 12.5
scaling_factor = 1.8

# Collect primary metrics
performance_data = collect_metrics(task_load, scaling_factor)

# Apply filtering (partially relevant)
cleaned_data = filter_outliers(performance_data, threshold=1.2)

# Define base weights (will be transformed)
base_weights = [4, 2, 5, 3, 1]

# Transform weights using complex logic
processed_weights = adjust_weights(base_weights)

# Compute legacy diagnostic (red herring)
legacy_diagnostic = compute_legacy_rank(performance_data)

# Aggregate final performance score
final_score = aggregate_performance(performance_data, processed_weights)

# Print result
print(f"Result: {final_score}")