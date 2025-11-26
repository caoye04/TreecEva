def compute_quality_score(data_sequence, quality_threshold):
    # Irrelevant data processing that doesn't affect final result
    temp_buffer = [x * 2 for x in data_sequence if x > 0]
    processed_data = [val // 3 for val in temp_buffer]
    
    # Misleading intermediate calculations
    dummy_sum = sum(processed_data) + len(data_sequence)
    misleading_factor = (dummy_sum % 7) * 2.5
    
    # Actual relevant processing with enumerate
    valid_indices = []
    for idx, value in enumerate(data_sequence):
        if value >= quality_threshold:
            valid_indices.append(idx)
    
    # Distractor operations that look important but aren't
    offset_data = [x + misleading_factor for x in processed_data]
    normalized_values = [v / 2.0 for v in offset_data]
    
    # Key computation using zip
    pairs = list(zip(valid_indices, data_sequence))
    weighted_sum = 0
    for index, value in pairs:
        weighted_sum += value * (index + 1)
    
    # Final calculation with intentional complexity
    base_score = weighted_sum // len(pairs) if pairs else 0
    adjustment_factor = (len(valid_indices) * 3) - (misleading_factor // 2)
    
    # Dead code path that never executes
    if base_score < 0:
        irrelevant_var = base_score * 2 + 100
    
    return base_score + adjustment_factor

def analyze_data_stream(input_data):
    # Unused helper function that serves as distraction
    sorted_data = sorted(input_data)
    median_val = sorted_data[len(sorted_data) // 2] if sorted_data else 0
    return median_val * 0.75

# Main execution with multiple distractors
data_stream = [12, 8, 15, 6, 20, 3, 18, 9]
threshold_value = 10

# Misleading variable that looks important
preliminary_analysis = analyze_data_stream(data_stream)
redundant_calc = sum(data_stream) * preliminary_analysis

# The key function call
final_metric = compute_quality_score(data_stream, threshold_value)

# Final print statement
print(f"Result: {final_metric}")