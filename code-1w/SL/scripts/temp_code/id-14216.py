def preprocess_data(raw):
    normalized = [x / max(raw) for x in raw]
    filtered = [x for x in normalized if x > 0.1]
    return filtered


def calculate_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def calculate_final_score(dataset, importance_weights):
    # Step 1: Normalize and filter data
    processed = preprocess_data(dataset)
    
    # Irrelevant computation: simulate noise reduction (not used later)
    smoothed = [processed[i] * 0.9 + 0.1 for i in range(len(processed))]
    avg_smoothed = sum(smoothed) / len(smoothed) if smoothed else 0
    
    # Step 2: Apply weights using slicing and dictionary lookup
    weighted_values = {}
    for i, weight in enumerate(importance_weights):
        key = f'item_{i}'
        weighted_values[key] = processed[i % len(processed)] * weight
    
    # Misleading intermediate: unused aggregation
    temp_sum = sum(v for v in weighted_values.values() if v < 1.0)
    temp_max = max(weighted_values.values())
    
    # Step 3: Use only specific items based on condition
    selected_keys = [k for k in weighted_values.keys() if int(k.split('_')[1]) % 2 == 0]
    selected_scores = [weighted_values[k] for k in selected_keys]
    
    # Step 4: Compute score using conditional logic and bitwise check
    base_score = sum(selected_scores)
    adjustment = 0
    if len(selected_scores) & 1:  # Bitwise odd-check
        adjustment = calculate_entropy(selected_scores)
    else:
        adjustment = len(selected_scores) // 2
    
    # Final computation
    final_score = base_score + adjustment
    
    # Dead code: irrelevant formatting
    result_str = f"Score={final_score:.3f}"
    debug_info = {"count": len(selected_scores), "adjustment": adjustment}
    
    return final_score

# Main execution
raw_data = [12, 18, 24, 7, 35, 14]
weights = [0.8, 1.2, 0.5, 1.6, 0.9]

intermediate = [x ** 0.5 for x in raw_data]  # Unused preprocessing
meta_info = {'version': '2.1', 'mode': 'standard'}

final_score = calculate_final_score(raw_data, weights)
print(f"Result: {final_score}")