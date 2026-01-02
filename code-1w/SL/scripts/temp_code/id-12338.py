def analyze_sequence(data):
    # Irrelevant transformation: character frequency counting
    freq = {}
    for char in ''.join(map(str, data)):
        freq[char] = freq.get(char, 0) + 1
    
    # Distractor: unused complex list comprehension
    distractor_list = [x ** 2 for x in data if x % 3 == 0 and x > 5]
    temp_result = sum(distractor_list) // len(distractor_list) if distractor_list else 0

    # Meaningful but obfuscated preprocessing
    processed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            processed.append(val * 1.5)
        else:
            processed.append(val + 2.5)
    
    # Dead code path (never executed due to fixed condition)
    backup_mode = False
    if backup_mode and len(processed) > 100:
        processed = [x / 2 for x in processed]

    # Another red herring: string slicing on numeric conversion
    str_rep = ''.join([str(int(x)) for x in processed[:5]])
    slice_value = int(str_rep[1:4]) if len(str_rep) >= 4 else 0  # Unused later

    # Key transformation: normalize using max and shift by index sum
    max_val = max(processed)
    index_sum = sum(i for i, x in enumerate(processed) if x > 10)
    normalized = [(x / max_val) + index_sum * 0.01 for x in processed]

    return normalized


def calculate_weights(length):
    # Decoy weight generator with unused trigonometric logic
    import math
    weights = []
    for i in range(length):
        base = math.cos(i * math.pi / 4)  # Misleading use of trig
        adjusted = abs(base) * 1.5
        weights.append(adjusted if adjusted > 0.5 else 0.5)
    
    # Dead function call placeholder
    def validate_integrity(w):
        return sum(w) % 1 != 0  # Never called

    return weights


def evaluate_performance(metrics, weights):
    # Element-wise multiplication using zip
    product_values = []
    for m, w in zip(metrics, weights):
        product_values.append(m * w)
    
    # Secondary processing with enumerate and filtering
    adjusted_sum = 0
    for i, val in enumerate(product_values):
        if i % 3 == 0:
            adjusted_sum += val * 1.1
        elif val > 5:
            adjusted_sum += val * 0.9
        else:
            adjusted_sum += val
    
    # Final non-linear adjustment
    if adjusted_sum > 50:
        adjusted_sum = (adjusted_sum ** 0.5) * 3
    else:
        adjusted_sum = adjusted_sum * 1.8

    # Critical result
    final_score = int(adjusted_sum * 100) / 100.0  # Rounded to 2 decimal places

    # Distractor: unrelated string operation chain
    metadata_tag = "perf_eval_2024"
    tag_suffix = metadata_tag[5:].upper().replace('_', '')
    hash_value = sum(ord(c) for c in tag_suffix)  # Computed but not used

    return final_score

# Main execution flow
raw_data = [12, 7, 15, 3, 9, 14, 6, 11]
data_metrics = analyze_sequence(raw_data)
weights = calculate_weights(len(data_metrics))
final_score = evaluate_performance(data_metrics, weights)

# Output the required result
print(f"Target result: {final_score}")