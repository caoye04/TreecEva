def analyze_sequence(seq, threshold):
    above_threshold = [x for x in seq if x > threshold]
    squared_sum = sum(x ** 2 for x in above_threshold)
    return squared_sum if above_threshold else 0


def normalize_values(data):
    max_val = max(data) if data else 1
    return [round(x / max_val, 3) for x in data]


def compute_performance(raw_data):
    processed = [x * 1.5 + 2 for x in raw_data]  # preliminary transformation
    filtered = [x for x in processed if x >= 10]
    temp_result = analyze_sequence(filtered, 15)
    
    # Irrelevant normalization (distractor)
    normalized = normalize_values(raw_data)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    dummy_offset = int(avg_normalized * 3)  # unused in final logic
    
    # Conditional expression with enumerate and zip
    adjustments = []
    for i, (a, b) in enumerate(zip(processed, normalized)):
        if i % 2 == 0 and a > 12:
            adjustments.append(1.1 if b > 0.5 else 0.9)
        else:
            adjustments.append(1.0)
    
    # Real computation path
    base_score = sum(filtered) // len(filtered) if filtered else 0
    penalty = 0
    for i, val in enumerate(filtered):
        if i > 0 and val < filtered[i-1]:
            penalty += 1
    
    # Final score calculation
    scaling_factor = 2.5 if temp_result > 500 else 1.8
    final_score = int(base_score * scaling_factor - penalty * 3)
    
    # Dead code branch (distractor)
    if dummy_offset > 100:
        final_score += 50  # unreachable under current inputs
    
    return final_score

# Input data
benchmark_data = [4, 7, 9, 12, 15, 14, 18, 20, 19]

# Execution point of interest
final_score = compute_performance(benchmark_data)
print(f"Result: {final_score}")