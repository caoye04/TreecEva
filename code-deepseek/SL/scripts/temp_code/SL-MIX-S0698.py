def calculate_scores(data_points):
    irrelevant_total = sum([x * 2 for x in range(10)])  # Dead computation
    scores = []
    temp_buffer = []
    
    for i, value in enumerate(data_points):
        base_score = value ** 2 % 17
        if i % 3 == 0:
            modifier = (i + 5) // 2
            adjusted = base_score + modifier
        elif i % 3 == 1:
            modifier = i * 3 - 7
            adjusted = base_score - modifier
        else:
            modifier = (i + 2) * 2
            adjusted = base_score * 2 + modifier
        
        temp_buffer.append(adjusted)  # Misleading intermediate
        processed = adjusted % 13 if adjusted > 0 else abs(adjusted) % 11
        scores.append(processed)
    
    misleading_avg = sum(temp_buffer) / len(temp_buffer)  # Distractor
    return scores

def filter_scores(score_list):
    threshold = 8
    filtered = list(filter(lambda x: x >= threshold, score_list))
    
    # Irrelevant set operations
    temp_set = set([x for x in range(15)])
    another_set = set(score_list)
    union_set = temp_set.union(another_set)  # Dead code path
    
    return filtered

def result_filter(filtered_data):
    if not filtered_data:
        return -1
    
    # Multiple irrelevant calculations
    dummy_sum = sum([ord(c) for c in "distractor"])  # Dead computation
    dummy_product = len(filtered_data) * 3.14159
    
    # Actual relevant logic
    result = max(filtered_data) - min(filtered_data)
    result *= len([x for x in filtered_data if x % 2 == 0])
    
    # More distractions
    string_check = "python".upper().replace('P', 'X')  # Irrelevant string ops
    
    return result

# Main execution
input_data = [4, 12, 7, 15, 9, 3, 11, 6, 18, 2]
calculated_scores = calculate_scores(input_data)
filtered_scores = filter_scores(calculated_scores)
final_output = result_filter(filtered_scores)

print(f"Target result: {final_output}")