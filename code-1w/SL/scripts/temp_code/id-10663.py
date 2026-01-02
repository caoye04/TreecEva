def analyze_sequence(raw_values):
    # Irrelevant transformation
    temp_buffer = [x ** 2 for x in raw_values if x % 2 == 0]
    shifted_data = [x >> 1 for x in raw_values]
    
    # Core processing with slicing and filtering
    filtered = [x for x in raw_values if x > 0]
    midpoint = len(filtered) // 2
    left_half = filtered[:midpoint]
    right_half = filtered[midpoint:]
    
    # Misleading aggregation
    avg_left = sum(left_half) / len(left_half) if left_half else 0
    max_right = max(right_half) if right_half else 0
    
    # Actual relevant computation
    normalized = [abs(x - avg_left) for x in right_half]
    return normalized


def calculate_final_score(data):
    # Dummy tracking variables (distractors)
    iteration_count = 0
    cumulative_shift = 0
    
    score = 0
    for i, val in enumerate(data):
        iteration_count += 1
        cumulative_shift += (val & 3)  # Bitwise distraction
        if i % 2 == 0:
            score += val * 1.5
        else:
            score -= val * 0.5
    
    # Additional red herring logic
    if cumulative_shift > 10:
        score = score * 0.9
    
    # Final adjustment based on logical condition
    is_balanced = len(data) >= 3 and data[0] + data[-1] == 2 * data[len(data)//2]
    bonus = 10 if is_balanced else 0
    
    return int(score + bonus)

# Main execution
raw_input = [8, -4, 12, 0, 6, 18, -2]

# Dead code path (irrelevant function call)
unused_result = [x.lower() for x in ['A', 'B', 'C']]

processed = analyze_sequence(raw_input)
final_score = calculate_final_score(processed)
print(f"Result: {final_score}")