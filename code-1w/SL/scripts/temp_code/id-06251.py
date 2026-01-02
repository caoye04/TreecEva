from itertools import cycle

# Simulate adaptive learning system with performance feedback
initial_weights = [0.8, 0.9, 0.75, 0.85]
learning_rate = 0.05
correction_factors = [1.1, 0.9, 1.2, 0.85, 1.0]

# Irrelevant distractor: unused transformation matrix
distractor_matrix = [[i * j for j in range(3)] for i in range(3)]

# Simulated performance history over multiple iterations
performance_log = []
for epoch in range(4):
    adjusted_weight = initial_weights[epoch] + learning_rate * (epoch - 1)
    if adjusted_weight > 0.9:
        adjusted_weight = 0.9
    performance_log.append(round(adjusted_weight, 3))

# Feedback cycles with diminishing returns
feedback_cycles = []
for i, perf in enumerate(performance_log):
    cycle_entry = {}
    
    # Core metric computation
    base_metric = perf * (1 + learning_rate * i)
    penalty = 0.01 * i ** 2
    effective_metric = max(base_metric - penalty, 0.5)
    
    # Distractor computation: irrelevant temporal decay
    temporal_decay = perf * (0.95 ** i)
    decayed_value = round(temporal_decay, 4)  # Not used later
    
    cycle_entry['metric'] = round(effective_metric, 4)
    cycle_entry['epoch'] = i
    feedback_cycles.append(cycle_entry)

# Aggregation function with selective filtering
def aggregate_performance(cycles):
    total = 0.0
    count = 0
    threshold = 0.78
    
    # Use itertools.cycle for circular traversal (overkill but realistic)
    circular_iter = cycle(cycles)
    for _ in range(len(cycles) * 2):  # Traverse twice
        item = next(circular_iter)
        # Only consider high-confidence feedback
        if item['metric'] > threshold:
            total += item['metric'] * 1.1  # Boost high performers
            count += 1
    
    # Dead code path: never executed due to count >= 1 always true
    if count == 0:
        return 0.5
        redundant_reset = True  # Dead assignment
        total = 0.6  # Never reached

    average_boosted = total / count if count else 0.0
    
    # Final scaling based on number of valid cycles
    scaling_factor = 1 + (count * 0.05)
    final_raw = average_boosted * scaling_factor
    
    # Additional distractor: complex rounding that doesn't affect outcome
    precision_offset = len(str(final_raw).split('.')[1]) if '.' in str(final_raw) else 0
    adjustment = 0.001 * (precision_offset % 3)
    final_adjusted = final_raw - adjustment
    
    return round(final_adjusted, 4)

# Key statement
final_score = aggregate_performance(feedback_cycles)

# Output result as required
print(f"Result: {final_score}")