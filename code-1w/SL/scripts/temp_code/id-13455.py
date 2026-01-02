def analyze_metrics(raw_data):
    # Irrelevant data transformation (distractor)
    temp_buffer = [x ** 2 for x in raw_data if x % 3 == 0]
    processed = [x for x in raw_data if x > 0]
    
    # Dead code path (unused function)
    def decrypt_key(token):
        return sum([ord(c) % 7 for c in str(token)])

    # Misleading intermediate result
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    scaling_factor = 1.75  # Used nowhere important

    # Actual relevant logic begins: filter and transform
    filtered = [x for x in processed if x < 100]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]

    # Bit manipulation red herring
    bit_flag = 0
    for val in normalized:
        bit_flag ^= int(val) & 7
    bit_flag = (bit_flag << 3) | (bit_flag >> 2)

    # Set operations (required language feature)
    unique_quarters = {int(x // 25) for x in normalized}
    expected_quarters = {0, 1, 2, 3}
    missing_quarters = expected_quarters - unique_quarters

    # Another distraction: unused dictionary aggregation
    stats_summary = {}
    for i, val in enumerate(normalized):
        stats_summary[f'entry_{i}'] = {
            'raw': processed[i] if i < len(processed) else 0,
            'norm': val,
            'flag': (val * 17) % 9
        }

    # Core logic buried in noise: compute metric set based on distribution
    q1, q2, q3 = 25, 50, 75
    count_in_q2 = len([x for x in normalized if q1 <= x < q2])
    count_in_q3 = len([x for x in normalized if q2 <= x < q3])
    balance_ratio = count_in_q2 / count_in_q3 if count_in_q3 != 0 else 0

    metric_set = set()
    metric_set.add(round(balance_ratio * 100))
    metric_set.add(len(missing_quarters) * 10)
    metric_set.add(len(filtered) % 7 * 5)

    # Control flow with nested conditionals (modular arithmetic)
    adjustment = 0
    for val in filtered:
        if val % 4 == 0:
            adjustment += 1
        elif val % 5 == 0:
            adjustment -= 1

    metric_set.add(adjustment * 3)

    # Decoy assignment (never used)
    final_report = {
        'data': list(normalized),
        'checksum': sum(int(x) for x in normalized) % 1000,
        'status': 'processed'
    }

    return metric_set


def evaluate_performance(metrics):
    # Complex decision logic with short-circuiting and comparisons
    base = 0
    if 20 in metrics and 15 in metrics and (30 in metrics or 25 in metrics):
        base += 50
    elif 10 in metrics:
        base += 20
    else:
        base += 5

    # Additional computation using set characteristics
    max_metric = max(metrics)
    min_metric = min(metrics)
    range_bonus = (max_metric - min_metric) // 10

    # Case conversion distraction (string manipulation)
    mode_flag = "".join([chr(97 + (m % 26)) for m in metrics[:3]])
    mode_flag = mode_flag.upper().lower()  # Redundant operations

    # Real contribution to answer
    count_even = len([m for m in metrics if m % 2 == 0])
    parity_bonus = count_even * 7

    # Dictionary usage (suggested paradigm)
    bonuses = {
        'range': range_bonus,
        'parity': parity_bonus,
        'base': base
    }

    # Final score calculation
    final_score = sum(bonuses.values())

    # Irrelevant output formatting
    report_lines = []
    for k, v in sorted(bonuses.items()):
        report_lines.append(f'{k}: {v:>3}')

    return final_score

# Main execution
raw_input_data = [85, -3, 12, 9, 44, 67, 21, 72, 3, 99, 50, 15, 6]
metric_result = analyze_metrics(raw_input_data)
final_score = evaluate_performance(metric_result)
print(f'Target result: {final_score}')