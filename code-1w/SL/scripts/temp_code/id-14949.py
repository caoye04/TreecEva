def analyze_metrics(data_log, config):
    # Irrelevant preprocessing (distractor)
    temp_buffer = [x ** 0.5 for x in data_log if x > 10]
    adjusted_offsets = {i: val % 7 for i, val in enumerate(temp_buffer)}

    # Core logic disguised among distractions
    accumulator = 0
    for i in range(len(data_log)):
        if i % 3 == 0 and data_log[i] > 5:
            accumulator += data_log[i] // 2

    # Dead code path - never executed due to fixed condition (red herring)
    if config.get('enable_legacy_mode', False):
        accumulator = apply_legacy_transform(accumulator)  # Unused function

    return accumulator


def apply_legacy_transform(x):  # Decoy function
    return (x * 3) ^ 5


def build_metric_framework(base, factor):
    # Complex but partially irrelevant dictionary construction
    framework = {}
    for k in range(1, 6):
        key = f'metric_{k}'
        if k % 2 == 0:
            framework[key] = base * (factor ** k) + 2
        else:
            framework[key] = base + (k * factor) - 1

    # Misleading transformation
    temp_result = sum(framework.values()) / len(framework)
    noise_offset = (temp_result * 0.1) // 1

    # Only this subset is actually used later
    framework['metric_1'] = 17  # Reset to deterministic value
    framework['metric_4'] = 22
    framework['metric_5'] = 8

    return framework

def evaluate_performance(metrics, threshold):
    # Logical evaluation with short-circuiting and red herrings
    score = 0

    # Real logic begins here
    if 'metric_1' in metrics and metrics['metric_1'] > threshold:
        score += int(metrics['metric_1'] * 1.3)

    if 'metric_4' in metrics:
        temp_val = metrics['metric_4']
        # Bit manipulation distraction
        masked = temp_val & 0b1111
        if masked > 5:
            score += (masked ^ 5) * 2  # XOR then multiply

    # Unused branches
    if 'metric_99' in metrics:  # Never exists
        score -= metrics['metric_99']

    if 'metric_5' in metrics:
        comp_val = metrics['metric_5']
        if comp_val < 10 and (comp_val > 0 or True):
            score += 100  # Guaranteed add due to OR with True

    # Final adjustment using combinatorics-like calculation (simple)
    n, r = 5, 2
    combination_factor = 1
    for i in range(r):
        combination_factor *= (n - i)
    combination_factor //= 2  # Simulate C(n,r) approximation

    # This line has no effect — dead code (distraction)
    _ = combination_factor * 10  

    return score

# Main execution flow
if __name__ == '__main__':
    raw_data = [12, 3, 25, 8, 16, 4, 21]
    settings = {'debug': True, 'version': '2.1'}

    # Call analysis (produces intermediate result not directly used)
    intermediate_total = analyze_metrics(raw_data, settings)

    # Build metric map — only some values matter
    metric_map = build_metric_framework(base=3, factor=4)

    # Add decoy entries
    metric_map['aux_1'] = intermediate_total * 2
    metric_map['debug_flag'] = False

    base_threshold = 10

    # Key statement
    final_score = evaluate_performance(metric_map, base_threshold)

    print(f"Result: {final_score}")