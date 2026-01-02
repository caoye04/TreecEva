def analyze_distribution(data_string):
    raw_segments = data_string.split(',')
    parsed_values = [int(x.strip()) for x in raw_segments if x.strip().isdigit()]

    # Irrelevant transformation: character frequency analysis (distractor)
    char_freq = {}
    for char in data_string:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    avg_char_code = sum(ord(k) * v for k, v in char_freq.items()) / max(len(char_freq), 1)

    # Relevant: filter values and compute derived weights
    filtered_weights = []
    cumulative = 0
    for val in parsed_values:
        if val % 2 == 1:  # Only odd values contribute
            cumulative += val
            filtered_weights.append(cumulative)

    # Dead code path: never executed due to logic above (misleading)
    if any(v < 0 for v in parsed_values):
        parsed_values = [abs(v) for v in parsed_values]

    # Semi-relevant: derive adjustment factor based on string pattern
    token_count = len(data_string.replace(' ', '').split(','))
    padding_length = len(data_string) - len(data_string.lstrip('0'))
    adjustment_factor = (token_count % 7) + (padding_length * 0.1)

    # Key computation with distractors around it
    if filtered_weights:
        scale_baseline = sum(filtered_weights) / len(filtered_weights)
        variance_proxy = sum((x - scale_baseline) ** 2 for x in filtered_weights) / len(filtered_weights)
        stability_score = (scale_baseline / (1 + variance_proxy))
        final_density = filtered_weights[-1] * adjustment_factor / len(filtered_weights)
    else:
        final_density = 0.0

    # Extra irrelevant accumulation (dead-end)
    total_pairs = 0
    for i in range(len(parsed_values)):
        for j in range(i + 1, len(parsed_values)):
            if parsed_values[i] + parsed_values[j] > 50:
                total_pairs += 1

    return final_density

result = analyze_distribution('10,13,004,17,22,25')
print(f"Result: {result}")