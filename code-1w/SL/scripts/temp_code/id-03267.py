import itertools

def analyze_sequence(pattern):
    count = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1]:
            count += 1
    return count

def filter_relevant_entries(records, min_val):
    filtered = []
    temp_sum = 0
    for r in records:
        if r >= min_val:
            filtered.append(r)
            temp_sum += r  # distractor: not used later
    return filtered

def compute_weighted_average(data):
    weights = [i+1 for i in range(len(data))]
    weighted = sum(d * w for d, w in zip(data, weights))
    total_weight = sum(weights)
    return round(weighted / total_weight, 4)

def evaluate_performance(metrics, limit):
    segment_a = metrics[1:6]
    segment_b = metrics[3:8]
    
    trend_a = analyze_sequence(segment_a)
    trend_b = analyze_sequence(segment_b)
    
    common_elements = list(set(segment_a) & set(segment_b))
    overlap_sum = sum(common_elements)  # semi-relevant but unused in final logic
    
    adjusted_metrics = filter_relevant_entries(metrics, min_val=limit)
    base_avg = compute_weighted_average(adjusted_metrics)
    
    # Misleading transformation block (distractor)
    transformed = []
    for x in adjusted_metrics:
        if x % 2 == 0:
            transformed.append(x ** 0.5)
        else:
            transformed.append(x // 3)
    dummy_avg = sum(transformed) / len(transformed) if transformed else 0
    
    # Critical decision path
    score = 0
    if base_avg > limit:
        score += 15
    if len(common_elements) >= 2:
        score += 8
    if trend_a >= 3 or trend_b >= 3:
        score += 12
    
    noise_factor = 0
    for combo in itertools.combinations([1, 2, 3], 2):
        noise_factor += combo[0]  # irrelevant computation
    
    final_score = score + 5  # core answer contribution
    return final_score

# Main execution
raw_data = [4, 7, 6, 8, 9, 5, 10, 3, 11]
metric_data = raw_data[::2]  # slicing: [4, 6, 9, 10, 11]
threshold = 7
temp_result = compute_weighted_average(raw_data)  # red herring call
unused_flag = any(x < 0 for x in metric_data)  # dead logic
interim_list = [x for x in metric_data if x > 5]  # intermediate structure

final_score = evaluate_performance(metric_data, threshold)
print(f"Result: {final_score}")