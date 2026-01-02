def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    outlier_count = 0

    for idx, entry in enumerate(raw_entries):
        if isinstance(entry, str):
            entry = entry.strip().lower()
            if entry.isdigit():
                val = int(entry)
            else:
                continue
        else:
            val = entry

        if val < 0 or val > 1000:
            outlier_count += 1
            continue

        adjusted_val = (val ** 0.5) * (idx % 7 + 1)
        temp_sum += adjusted_val
        cleaned.append(adjusted_val)

    scaling_factor = 1.0 if temp_sum == 0 else 100 / temp_sum
    normalized = [x * scaling_factor for x in cleaned]

    stats_tracker = {
        'count': len(normalized),
        'sum': sum(normalized),
        'max': max(normalized),
        'ignored': outlier_count
    }

    return normalized, stats_tracker


def filter_anomalies(data_list):
    # Irrelevant helper with dead logic
    threshold = sum(data_list) / len(data_list) * 1.5 if data_list else 0
    return [x for x in data_list if x <= threshold]


def calculate_entropy(values):
    # Distractor function not used in final computation
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)


def calculate_final_score(norm_data):
    base_score = 0
    penalty = 0

    for i, score in enumerate(norm_data):
        if i % 3 == 0:
            base_score += score * 2
        elif i % 5 == 0:
            base_score += score
        else:
            base_score += score * 0.5

        # Fake dependency
        if score > 20:
            penalty += 1

    # Final score ignores penalty (misleading)
    final = base_score  # No actual penalty applied

    # Extra noise
    debug_info = {'base': base_score, 'penalty_applied': 0}

    return final

# Main execution
raw_input = [400, '300', 'invalid', 900, '250', -50, 625, '800', 'xyz', 100]

processed_data, metrics = preprocess_records(raw_input)

# Unused intermediate steps
entropy_value = calculate_entropy(processed_data)
data_filtered = filter_anomalies(processed_data)

intermediate_result = list(map(lambda x: x + 10, processed_data[:4]))

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")