def process_entry(entry):
    raw_value = entry * 1.75
    adjusted = raw_value + (raw_value > 100) * 5 - (raw_value < 50) * 3
    return int(adjusted)


def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= 2 * std_dev]


def transform_case(text):
    # Irrelevant function for distraction
    return ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text))


def calculate_final_score(entries):
    processed = [process_entry(e) for e in entries]
    cleaned = filter_outliers(processed)
    
    # Simulate weighting factors
    weights = [1.1 if x > 90 else 0.9 for x in cleaned]
    weighted = [cleaned[i] * weights[i] for i in range(len(cleaned))]
    
    # Dummy tracking variables (distractors)
    total_ops = 0
    temp_sum = 0
    for val in weighted:
        if val > 100:
            temp_sum += val * 0.95
        elif val < 80:
            temp_sum += val * 1.05
        else:
            temp_sum += val
        total_ops += 1
    
    # Actual computation path
    base_avg = sum(weighted) / len(weighted)
    bonus = 10 if len([w for w in weighted if w > 100]) >= 2 else 0
    penalty = 5 if len([w for w in weighted if w < 60]) > 0 else 0
    final_score = int(base_avg) + bonus - penalty
    
    # Unused but plausible intermediate
    normalized_score = round(final_score * (1 + (len(weighted) - 5) * 0.01), 2)
    
    return final_score

# Main execution
raw_data = [45, 67, 89, 102, 115, 40, 94]
results = [x * 2 for x in raw_data if x > 40]  # Pre-filter and scale

# Extra irrelevant computations
irrelevant_set = {x % 17 for x in raw_data}
shifted_values = [x << 1 for x in irrelevant_set]
dummy_lookup = {i: chr(65 + (i % 26)) for i in shifted_values if i < 100}

final_score = calculate_final_score(results)
print(f"Result: {final_score}")