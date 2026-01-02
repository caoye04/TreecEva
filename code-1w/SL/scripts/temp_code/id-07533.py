from collections import defaultdict

# Simulate sensor fusion system (distractor context)
def analyze_readings(readings):
    stats = defaultdict(int)
    total = 0
    for val in readings:
        if val > 0:
            stats['positive'] += 1
            total += val
    avg = total / len(readings) if readings else 0
    return avg

def preprocess_metrics(raw):
    # Irrelevant transformation
    offset = 10
    adjusted = [x + offset for x in raw]
    shifted_avg = sum(adjusted) / len(adjusted)
    return [x - shifted_avg for x in adjusted]

def evaluate_performance(data, threshold):
    # Core logic with distractors
    base = threshold * 2
    temp_results = []
    
    for i, entry in enumerate(data):
        if i % 2 == 0:
            temp_results.append(entry ** 2)
        else:
            temp_results.append(entry // 3)
    
    # Linear search for first value above transformed threshold
    limit = base + 5
    found_index = -1
    for j in range(len(temp_results)):
        if temp_results[j] > limit:
            found_index = j
            break
    
    # Secondary computation path (partially irrelevant)
    helper_func = lambda x: x * 1.5 if x < 20 else x * 0.8
    mapped = [helper_func(v) for v in temp_results]
    
    # Actual answer derivation
    sum_even = sum(temp_results[k] for k in range(0, len(temp_results), 2))
    sum_odd = sum(temp_results[k] for k in range(1, len(temp_results), 2))
    diff = sum_even - sum_odd
    final_score = abs(diff) + (found_index if found_index != -1 else 10)
    
    # Dead code branch (distractor)
    if len(mapped) > 100:
        fallback = sum(mapped) / 100
        final_score = fallback
    
    return final_score

# Main execution
raw_input = [4, 9, 6, 15, 3, 12]
metric_data = preprocess_metrics(raw_input)
base_threshold = 7

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")