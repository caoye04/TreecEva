def analyze_pattern(sequence):
    if not sequence:
        return 0
    count = 0
    temp_sum = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            count += 1
            temp_sum += sequence[i]
    adjustment = len(sequence) % 4
    return count + adjustment


def validate_entry(record):
    # Irrelevant validation logic (not used in final result)
    if not isinstance(record, dict):
        return False
    required_fields = ['id', 'status', 'value']
    return all(f in record for f in required_fields)


def preprocess_data(raw):
    # Some preprocessing that looks important but only a part is used
    cleaned = [x for x in raw if isinstance(x, int) and x > 0]  # list comprehension
    shifted = [x >> 1 for x in cleaned if x % 2 == 0]  # bitwise shift, partially irrelevant
    return cleaned[:len(cleaned)//2 + 1]  # only first half-plus-one used


def calculate_threshold_metrics(data, thres):
    above = sum(1 for x in data if x > thres)  # using generator expression
    below = len(data) - above
    ratio = above / below if below else 0
    return ratio * 100


def calculate_final_score(dataset, limits):
    processed = preprocess_data(dataset)
    
    # Key computation branch
    base_score = 0
    for val in processed:
        if val % 3 == 0:
            base_score += val
        elif val % 5 == 0:
            base_score += val // 2
    
    # Distractor: complex but unused structure
    stats_summary = {
        'max_val': max(processed) if processed else 0,
        'min_val': min(processed) if processed else 0,
        'range': max(processed) - min(processed) if processed else 0,
        'pattern_strength': analyze_pattern(processed)
    }
    
    # Another red herring calculation
    outlier_count = 0
    for v in processed:
        if v > limits[1] or v < limits[0]:
            outlier_count += 1
    suppression_factor = outlier_count * 0.1

    # Actual score adjustment
    metric = calculate_threshold_metrics(processed, limits[1])
    if metric > 50:
        base_score += 10
    elif metric > 25:
        base_score += 5

    # Final adjustment based on length (only this affects final_score directly)
    length_bonus = len(processed) if len(processed) % 2 == 1 else 0
    final_score = base_score + length_bonus - 7  # key deterministic transformation

    # Dead code path - never executed under normal inputs
    if False:
        fallback = sum(processed) // 10
        final_score = fallback

    return final_score

# Main execution
raw_data = [15, -3, 0, 9, 10, 12, 8, 20, 7]
thresholds = [5, 11]
data_input = preprocess_data(raw_data)
final_score = calculate_final_score(raw_data, thresholds)
print(f"Result: {final_score}")