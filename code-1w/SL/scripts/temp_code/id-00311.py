def analyze_trends(data, threshold=5):
    trend_count = 0
    moving_avg = []
    temp_sum = 0
    
    for i, val in enumerate(data):
        temp_sum += val
        if i % 3 == 0 and i != 0:
            moving_avg.append(temp_sum / 3)
            temp_sum = 0
        if val > threshold:
            trend_count += 1

    if temp_sum != 0:
        moving_avg.append(temp_sum / ((i % 3) + 1))

    excess = sum(moving_avg) - len(moving_avg) * threshold
    return trend_count, excess


def normalize_values(raw_list):
    max_val = max(raw_list)
    min_val = min(raw_list)
    range_val = max_val - min_val
    normalized = [(x - min_val) / range_val for x in raw_list]
    return [round(x, 4) for x in normalized]


def filter_relevant(items, flags):
    selected = []
    for item, flag in zip(items, flags):
        if flag and item % 2 == 1:
            selected.append(item)
    return set(selected)


def evaluate_performance(feedback, scores):
    total = 0
    bonus = 0
    penalty = 0
    
    # Real logic begins
    score_map = {k: v for k, v in enumerate(scores)}
    feedback_keys = set(feedback.keys())
    common_indices = feedback_keys.intersection(set(score_map.keys()))
    
    for idx in common_indices:
        raw_score = score_map[idx]
        feedback_level = feedback[idx]
        
        if feedback_level == 'high':
            bonus += raw_score * 0.2
        elif feedback_level == 'low':
            penalty += raw_score * 0.1
        
        total += raw_score

    adjustment = bonus - penalty
    final_value = total + adjustment
    
    # Dead code - irrelevant
    debug_info = {}
    for k, v in feedback.items():
        debug_info[k] = len(v) * 2
    
    return int(round(final_value))

# Irrelevant data structures
raw_sensor_data = [12, 7, 3, 18, 9, 6]
trend_analysis = analyze_trends(raw_sensor_data)
normalized_readings = normalize_values([10, 20, 30, 40])

# Flags for filtering (unused in final logic)
item_flags = [True, False, True, True, False]
candidate_items = [5, 8, 11, 14, 17]
selected_group = filter_relevant(candidate_items, item_flags)

# Core data for the actual computation
base_scores = [85, 90, 78, 92]
feedback_map = {0: 'high', 1: 'medium', 2: 'low', 3: 'high'}

# Misleading intermediate calculation
shadow_total = sum(base_scores) * 0.95
buffer = [shadow_total * i for i in range(3)]

final_score = evaluate_performance(feedback_map, base_scores)
print(f"Result: {final_score}")