def preprocess_entry(entry):
    # Irrelevant transformation
    temp = [x * 1.5 for x in entry if x > 0]
    normalized = [val / (sum(temp) + 1e-8) for val in temp]
    return normalized


def calculate_entropy(values):
    # Distractor function: not used in final computation
    import math
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return entropy


def calculate_final_score(records, importance_weights):
    total_weighted_sum = 0.0
    base_offset = 10
    adjustment_factor = 0.95
    
    # Real logic starts here
    aggregated = []
    for i, record in enumerate(records):
        row_sum = 0
        for j, val in enumerate(record):
            # Apply weight based on position using enumerate and zip concept
            if i < len(importance_weights) and j < len(importance_weights[i]):
                weighted_val = val * importance_weights[i][j]
                row_sum += weighted_val
        
        # Add dummy scaling (not actually affecting final result directly)
        scaled_row = row_sum * adjustment_factor
        aggregated.append(scaled_row)
    
    # Secondary processing with zip
    shifted = [x + base_offset for x in aggregated]
    multiplier_sequence = [2, 1, 3]
    
    # Use zip to pair elements (some are unused)
    paired_data = []
    for s, m in zip(shifted, multiplier_sequence * 2):
        paired_data.append(s * m)
    
    # Core result derivation
    raw_total = sum(aggregated)  # Only this matters
    bonus = len([x for x in records if sum(x) > 5])  # Conditional bonus
    final_score = int(raw_total + bonus)
    
    # Dead code path (never executed under current input)
    if len(records) > 100:
        fallback = 0
        for item in records:
            fallback += max(item)
        final_score = fallback
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    data = [
        [3, 1, 4],
        [2, 7, 1],
        [6, 0, 3]
    ]
    
    weights = [
        [0.5, 1.0, 0.8],
        [1.0, 0.9, 0.3],
        [0.7, 0.0, 0.6]
    ]
    
    # Preprocessing (distractor)
    processed_data = []
    for entry in data:
        processed_entry = preprocess_entry(entry)
        processed_data.append(processed_entry)
    
    # Actual target computation
    final_score = calculate_final_score(data, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")