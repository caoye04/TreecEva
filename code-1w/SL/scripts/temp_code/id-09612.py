def calculate_final_score(data, threshold):
    # Preprocessing: filter and transform
    filtered_data = [x for x in data if x > threshold]
    squared_values = [x ** 2 for x in filtered_data]
    
    # Distractor: irrelevant transformation
    inverted = [1 / (x + 1) for x in data]  # Not used later
    temp_sum = sum(inverted[:3]) if len(inverted) > 3 else 0  # Dead-end computation

    # Actual logic chain
    if len(filtered_data) < 3:
        base_score = sum(filtered_data) * 1.5
    else:
        base_score = sum(squared_values) / len(filtered_data)

    # Conditional expression (required Python feature)
    adjustment = 10 if all(x % 2 == 0 for x in filtered_data) else 7
    
    # Secondary distractor: complex but unused structure
    stats = {
        'mean': sum(data) / len(data),
        'max': max(data),
        'ignored_flag': any(x < 0 for x in data)
    }

    # Further processing with nesting and dependency
    penalty = 0
    for i, val in enumerate(filtered_data):
        if i % 2 == 1:
            for j in range(2):
                penalty += (val // 10)  # Minor cumulative effect

    # Final composition
    final_score = base_score + adjustment - penalty
    
    # Irrelevant sort (suggested paradigm)
    sorted_squares = sorted(squared_values, reverse=True)  # Used nowhere

    return final_score

# Main execution
raw_input = [4, 7, 6, 9, 12]
threshold = 5

# Unused variables to increase cognitive load
baseline = sum(raw_input) / len(raw_input)
deviation = [x - baseline for x in raw_input]

final_score = calculate_final_score(raw_input, threshold)
print(f"Result: {final_score}")