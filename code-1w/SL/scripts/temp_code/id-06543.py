from itertools import combinations

def analyze_trends(data_points):
    trends = []
    for i in range(1, len(data_points)):
        if data_points[i] > data_points[i-1]:
            trends.append('up')
        elif data_points[i] < data_points[i-1]:
            trends.append('down')
        else:
            trends.append('flat')
    return trends

def generate_pairs(elements):
    # Irrelevant helper function (dead code path)
    return list(combinations(elements, 2))
def preprocess_feedback(raw_feedback):
    cleaned = {}
    temp_values = []
    
    for k, v in raw_feedback.items():
        if isinstance(v, str):
            cleaned[k] = len(v.strip())
        elif isinstance(v, (int, float)):
            temp_values.append(v)
            cleaned[k] = int(abs(v) % 7)  # Distraction: non-linear mapping
    
    # Dummy computation with no effect on final result
    avg_temp = sum(temp_values) / len(temp_values) if temp_values else 0
    adjustment_factor = round(avg_temp * 0.1)

    return cleaned

def evaluate_performance(feedback_map, min_threshold):
    count_above = 0
    internal_sum = 0
    
    for key, value in feedback_map.items():
        if 'review' in key:
            sliced_part = key[-2:]  # slicing operation
            index_val = int(sliced_part) if sliced_part.isdigit() else 0
            if index_val % 2 == 0 and value > min_threshold:
                count_above += 1
            internal_sum += value

    # Actual logic determining final_score
    base_score = internal_sum // (count_above or 1)
    bonus = 3 if count_above >= 3 else 0
    final_score = base_score + bonus
    
    # Unused variables to increase cognitive load
    dummy_stats = {
        'max_val': max(feedback_map.values(), default=0),
        'key_count': len([k for k in feedback_map.keys() if k.startswith('review')]),
        'pairs': generate_pairs(list(feedback_map.keys()))  # calls dead function
    }
    
    return final_score

# Main execution
raw_data = [10, 12, 11, 15]
trend_analysis = analyze_trends(raw_data)

feedback_dict = {
    'review_01': ' excellent work ',
    'review_02': 8,
    'notes_extra': 'ignore this',
    'review_03': 5,
    'review_04': 9,
    'meta_info': 42,
    'review_05': 6
}

processed = preprocess_feedback(feedback_dict)
threshold = 5
critical_point = 'evaluate_performance'
final_score = evaluate_performance(processed, threshold)

print(f"Result: {final_score}")