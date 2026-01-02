def analyze_signal_pattern(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [x / max(raw_readings) for x in raw_readings]
    binary_flags = [1 if x > threshold else 0 for x in normalized]

    # Distractor: unused signal transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val * 1.5)
        else:
            transformed.append(val * 0.8)

    # Real computation begins: extract key indices using enumerate
    event_indices = [i for i, x in enumerate(raw_readings) if x > 30 and i % 2 == 1]

    # Bitwise manipulation chain (relevant)
    accumulated_mask = 0
    for idx in event_indices:
        accumulated_mask ^= idx << 1  # XOR shift pattern
        accumulated_mask |= (idx & 7)  # OR with low bits

    # Secondary distractor: string-based logging (no impact)
    log_tag = "DIAG-" + "-".join([f"{x:.1f}" for x in raw_readings[::3]])
    log_check = sum(1 for c in log_tag if c.isdigit())

    # Data pairing with zip (relevant use)
    paired_metrics = list(zip(raw_readings[1::2], raw_readings[:-1:2]))  # odd-even pairs
    products = [a * b for a, b in paired_metrics]

    # Accumulation through conditional logic
    cumulative_score = 0
    for prod in products:
        if prod > 500:
            cumulative_score += int(prod // 10)
        elif prod > 200:
            cumulative_score += int(prod // 20)
        else:
            cumulative_score += 5

    # Another red herring: recursive count function (never called)
    def count_recursively(n):
        return 1 + count_recursively(n - 1) if n > 0 else 0

    # Adjustment logic based on mask parity (relevant)
    bit_sum = bin(accumulated_mask).count('1')
    adjustment_factor = bit_sum * 17 if accumulated_mask % 2 == 1 else bit_sum * -13

    # Dead code path: unreachable due to structure
    if False:
        cumulative_score *= 2
        adjustment_factor += 100

    # Critical assignment point
    final_diagnostic = cumulative_score + adjustment_factor

    # Final distractor: unrelated character analysis
    chars = 'signal_analysis_v4'
    extra_weight = sum(ord(c) for c in chars if c in 'aeiou') // 100

    # Output the required variable
    print(f"Result: {final_diagnostic}")

# Input data
readings = [25, 64, 12, 48, 33, 72, 18, 58, 41, 29]
analyze_signal_pattern(readings)