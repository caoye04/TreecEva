def analyze_metrics(data):
    # Irrelevant data processing (distractor)
    temp_results = [x ** 2 for x in data if x > 5]
    normalized = [round(x / sum(temp_results), 3) for x in temp_results]
    return sum(normalized[:3]) if len(normalized) > 2 else 0


def validate_inputs(entries):
    # Dead code path - never actually used in final computation
    if all(isinstance(e, int) for e in entries):
        return True
    return False

# Misleading intermediate variables (red herring)
baseline_offset = 17
adjustment_factor = 0.85
shadow_weight = 99

# Simulated system log with performance counters
counter_log = [3, 7, 4, 8, 2, 9, 6]

# Unused transformation (distractor)
doubled_counters = [n * 2 for n in counter_log if n % 2 == 0]

# Critical data structure: assessment log with nested conditions
assessment_log = [
    {'metric': 'latency', 'value': 42, 'weight': 3},
    {'metric': 'throughput', 'value': 18, 'weight': 5},
    {'metric': 'error_rate', 'value': 4, 'weight': 4},
    {'metric': 'availability', 'value': 96, 'weight': 2}
]

# Auxiliary function with conditional expression and recursion
def compute_stability(index, history):
    if index <= 0:
        return history[0] * 0.1
    prev = compute_stability(index - 1, history)
    current = history[index] * 0.1
    # Conditional expression (python idiom)
    return current + (prev * 0.5 if prev > 2.0 else prev * 0.3)

# Secondary calculation that seems important but is unused
phantom_score = compute_stability(3, [10, 20, 15, 25])

# Core evaluation logic (heavily masked by noise)
def evaluate_performance(metrics):
    total_weight = sum(item['weight'] for item in metrics)
    weighted_sum = 0

    for entry in metrics:
        raw_value = entry['value']
        weight = entry['weight']

        # Complex conditional scoring logic
        if entry['metric'] == 'latency':
            score = (100 - raw_value) * weight
        elif entry['metric'] == 'throughput':
            score = (raw_value * 1.5) * weight
        elif entry['metric'] == 'error_rate':
            # Bitwise manipulation as distraction (irrelevant to result)
            adjusted = raw_value & 7
            score = (10 - adjusted) * weight
        else:
            # availability or others
            score = (raw_value * 0.8) * weight

        weighted_sum += score

    # Final adjustment using distractor variables (but only baseline_offset matters)
    base_adjusted = weighted_sum - baseline_offset

    # Destructuring assignment (python feature)
    primary, secondary = base_adjusted * 0.9, base_adjusted * 0.1

    # Conditional expression determines final output
    final_value = primary - secondary if primary > 100 else primary + secondary

    return int(final_value)

# Key execution point
final_score = evaluate_performance(assessment_log)

# Output the target result
print(f"Result: {final_score}")