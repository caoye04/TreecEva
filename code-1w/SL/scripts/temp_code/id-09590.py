def preprocess_data(raw):
    cleaned = [x for x in raw if isinstance(x, (int, float)) and x >= 0]
    offset = sum(cleaned) // len(cleaned) if cleaned else 0
    adjusted = [x - offset + 3 for x in cleaned]
    return adjusted

def filter_outliers(values, limit):
    if not values:
        return []
    mean_val = sum(values) / len(values)
    deviate = [abs(x - mean_val) for x in values]
    cutoff = sum(deviate) / len(deviate) * 2.0
    filtered = [values[i] for i in range(len(values)) if deviate[i] <= limit]
    return filtered

def compute_entropy(arr):
    from math import log2
    if len(arr) == 0:
        return 0.0
    freq_set = {}
    for item in arr:
        freq_set[item] = freq_set.get(item, 0) + 1
    total = len(arr)
    entropy = 0.0
    for count in freq_set.values():
        p = count / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 4)

def calculate_final_score(dataset, thresh):
    stage_one = preprocess_data(dataset)
    
    temp_sum = 0
    temp_count = 0
    for val in stage_one:
        if val % 2 == 0:
            temp_sum += val * 1.5
        else:
            temp_sum += val * 0.8
        temp_count += 1
    
    # Dummy tracking variables (distractors)
    debug_snapshot = {"size": len(stage_one), "max_val": max(stage_one) if stage_one else 0}
    scaling_factor = debug_snapshot["max_val"] // 5 if debug_snapshot["max_val"] > 5 else 1
    
    intermediate_list = [x for x in stage_one if x > scaling_factor]
    
    # Unused sorting operation (misleading)
    sorted_intermediate = sorted(intermediate_list, reverse=True)
    alternate_path = set(sorted_intermediate) | {0, 1}  # Irrelevant set union
    
    stage_two = filter_outliers(intermediate_list, thresh)
    
    # Secondary distractor: complex but unused logic
    shadow_copy = stage_two.copy()
    for i in range(len(shadow_copy)):
        shadow_copy[i] = (shadow_copy[i] + 7) * 0.1
    
    base_score = sum(stage_two)
    entropy_metric = compute_entropy(stage_two)
    
    # Final computation
    final_score = int(base_score + (entropy_metric * 100))
    
    # Critical print statement
    print(f"Result: {final_score}")
    return final_score

# Input data with mixed types and noise
raw_data = [12, -5, 'ignore', 15, 12, 18, 3, 7, None, 3, 15, 12, 0, 9]
threshold = 10
final_score = calculate_final_score(raw_data, threshold)