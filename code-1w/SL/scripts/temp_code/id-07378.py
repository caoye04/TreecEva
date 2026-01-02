def analyze_data_stream(raw_values, threshold=50):
    # Irrelevant preprocessing: normalize values (not used in final logic)
    normalized = [round((x - min(raw_values)) / (max(raw_values) - min(raw_values)) * 100) for x in raw_values]
    stats_log = {'processed': len(raw_values), 'outliers': 0}

    # Decoy transformation: bit manipulation with no impact
    decoy_shifted = []
    for val in raw_values:
        temp = (val << 2) ^ 0xA5
        if temp > 200:
            decoy_shifted.append(temp % 100)

    # Real logic begins: identify candidates using modular arithmetic and set filtering
    candidate_set_a = {x for x in raw_values if x % 7 == 0}
    candidate_set_b = {x for x in raw_values if x > threshold}

    # Logical combination using set operations (intersection)
    potential_targets = candidate_set_a & candidate_set_b  # Numbers divisible by 7 AND above threshold

    # Secondary filter: must have odd digit sum
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    refined_candidates = [n for n in potential_targets if digit_sum(n) % 2 == 1]

    # Misleading sort and reversal (does not affect sum)
    refined_candidates.sort(reverse=True)
    if len(refined_candidates) > 3:
        _ = [refined_candidates[i] * 1.5 for i in range(3)]  # Dead computation

    # Final filtering: exclude numbers containing digit '4'
    filtered_candidates = [n for n in refined_candidates if '4' not in str(n)]

    # Key statement
    filtered_sum = sum(filtered_candidates)

    # Red herring: complex unused data structure
    history_tree = {}
    for i, v in enumerate(raw_values):
        history_tree[i] = {
            'value': v,
            'flags': [],
            'meta': bin(v ^ 0xFF)[:8] if v % 3 == 0 else None
        }

    # Output the required result
    print(f"Result: {filtered_sum}")

# Input data with deterministic behavior
input_stream = [42, 56, 63, 70, 84, 91, 105, 112, 119, 126]
analyze_data_stream(input_stream)