def analyze_performance(records):
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    outlier_threshold = 100
    adjusted_values = []

    for i, entry in enumerate(records):
        if not isinstance(entry, int) or entry < 0:
            continue
        if entry > outlier_threshold:
            adjusted_values.append(outlier_threshold)
        else:
            adjusted_values.append(entry)
        valid_count += 1

    if valid_count == 0:
        return 0

    mean_value = sum(adjusted_values) / valid_count
    variance_accum = 0
    for val in adjusted_values:
        variance_accum += (val - mean_value) ** 2
    std_dev = (variance_accum / valid_count) ** 0.5

    normalized = [max(0, (x - mean_value) / std_dev) for x in adjusted_values]
    noise_correction = len([n for n in normalized if n > 2.0])

    consistency_flag = True
    for j in range(1, len(adjusted_values)):
        if adjusted_values[j] < adjusted_values[j-1]:
            consistency_flag = False

    return int(mean_value), consistency_flag, noise_correction


def compute_final_score(data_string, multiplier):
    raw_parts = data_string.split(',')
    numeric_data = []
    for part in raw_parts:
        cleaned = part.strip().lstrip('0')
        if cleaned.isdigit():
            numeric_data.append(int(cleaned))
        elif '7' in cleaned:
            numeric_data.append(7)

    base_metrics = analyze_performance(numeric_data)
    
    # Distractor: complex string transformation with no impact
    transformed = ''.join([chr((ord(c) % 7) + 65) for c in data_string if c.isdigit()])
    dummy_analysis = len(transformed) * 2 if transformed else 0

    # Real computation path
    mean_val, is_consistent, noise_level = base_metrics
    score = mean_val * multiplier

    if is_consistent:
        score += 10
    
    # Another red herring: unused conditional based on string pattern
    has_repetition = any(data_string[i] == data_string[i+1] for i in range(len(data_string)-1))
    repeated_chars_bonus = 5 if has_repetition else 0  # Not used

    penalty = 0
    for idx, num in enumerate(numeric_data):
        if idx % 3 == 0 and num % 2 == 1:
            penalty += 2

    final_score = score - penalty

    # Irrelevant list processing
    indexed_pairs = list(enumerate(zip(numeric_data[:-1], numeric_data[1:])))
    pair_product_sum = sum(a * b for a, b in numeric_data[:-1], numeric_data[1:]) if len(numeric_data) > 1 else 0

    return final_score

# Execution entry point
input_str = "0012,0045,007,008,003,0099,00104"
m = 3
final_score = compute_final_score(input_str, m)
print(f"Result: {final_score}")