def analyze_contributions(raw_inputs):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x ** 0.5 for x in raw_inputs if x > 10]
    temp_buffer = [t for t in temp_buffer if t.is_integer()]

    # Distractor: complex but unused transformation
    encoded = {}
    for i, val in enumerate(raw_inputs):
        encoded[f'item_{i}'] = (val * 3) ^ 7 | (i << 2)

    # Real computation begins: filter and transform
    valid_entries = [v for v in raw_inputs if v % 2 == 1 and v < 50]
    adjusted = [v + 5 for v in valid_entries]

    # Bit manipulation red herring
    checksum = 0
    for a in adjusted:
        checksum ^= a
        checksum = (checksum + (checksum << 3)) & 0xFFFF

    # Unused recursive distraction
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    _ = [fibonacci(6) for _ in range(3)]  # Computationally wasteful, irrelevant

    # Core logic disguised among noise: summation with conditional scaling
    magnitude = sum(adjusted)
    if magnitude > 100:
        magnitude = magnitude // 2
    elif magnitude > 50:
        magnitude = int(magnitude * 0.75)
    else:
        magnitude *= 2

    # Dictionary-based weighting (key relevant step)
    weights = {'level_1': 0.3, 'level_2': 0.5, 'level_3': 0.8}
    tier = 'level_1'
    if magnitude > 90:
        tier = 'level_3'
    elif magnitude > 60:
        tier = 'level_2'

    scaled_score = magnitude * weights[tier]

    # Decoy accumulation loop
    accumulator = 0
    for i in range(1, 11):
        accumulator += i * (i - 1)
    # This affects nothing

    # Tuple unpacking distraction
    config_defaults = (15, 25, 35)
    min_val, _, max_val = config_defaults

    # Final data structure used in evaluation
    metric_data = {
        'base': scaled_score,
        'bonus': 0,
        'penalty': checksum % 10,
        'valid_count': len(valid_entries)
    }

    base_threshold = 42

    # Key statement
    final_score = evaluate_performance(metric_data, base_threshold)
    
    return final_score


def evaluate_performance(metrics, threshold):
    # Redundant validation checks
    if not metrics or 'base' not in metrics:
        return -1
    
    # Complex conditional bonus calculation (mostly bypassed)
    extra = 0
    if metrics['valid_count'] > 5:
        extra += 10
    if metrics['penalty'] < 5:
        extra += 5
    # Logical trap: short-circuit that's never triggered
    if metrics['bonus'] > 0 and (metrics['base'] / (metrics['bonus'] + 1)) > threshold:
        extra += 20

    # Critical formula hidden in middle
    score = metrics['base'] - metrics['penalty'] + extra

    # Dead code due to unreachable condition
    debug_mode = False
    if debug_mode and threshold < 0:
        log_entry = {"error": "invalid_threshold", "time": 0}
        print(log_entry)  # Never executed

    # Normalization via tuple map
    levels = (20, 40, 60)
    for level in reversed(levels):
        if score > level:
            score = (score + level) / 2.0
            break

    return score

# Entry point
input_stream = [12, 15, 22, 27, 33, 41, 44, 48]
result = analyze_contributions(input_stream)
final_score = result
print(f"Target result: {final_score}")