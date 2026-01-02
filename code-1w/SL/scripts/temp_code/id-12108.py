from itertools import combinations

def analyze_text_patterns(text):
    words = text.lower().split()
    word_pairs = list(combinations(words, 2))
    pair_frequency = {}
    for pair in word_pairs:
        if pair[0] != pair[1]:
            pair_frequency[pair] = pair_frequency.get(pair, 0) + 1
    
    repeated_pairs = [p for p, cnt in pair_frequency.items() if cnt > 1]
    return len(repeated_pairs)

def calculate_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log(prob, 2)
    return round(entropy, 4)

def preprocess_metrics(raw_data, offset=0.5):
    adjusted = [x + offset for x in raw_data]
    normalized = [x / max(adjusted) for x in adjusted]
    return [int(x * 100) for x in normalized]

def filter_outliers(data, factor=1.5):
    if len(data) == 0:
        return data
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def evaluate_performance(metrics, threshold):
    temp_result = 0
    bonus = 0
    penalty = 0
    
    # Simulated historical baseline (irrelevant to final result)
    baseline_ref = [78, 85, 88, 90, 82]
    avg_baseline = sum(baseline_ref) / len(baseline_ref)
    
    for val in metrics:
        if val > threshold + 5:
            bonus += 2
        elif val < threshold - 10:
            penalty += 1
        
    # Secondary adjustment based on pattern analysis (unused)
    aux_adjust = analyze_text_patterns("clear signal detected signal repeat")
    
    # Core logic
    above_threshold = [m for m in metrics if m >= threshold]
    if len(above_threshold) >= 3:
        temp_result += 15
    if sum(m > threshold for m in metrics) == len(metrics):
        temp_result += 10
    
    # Entropy-based weighting (only used to compute intermediate var)
    entropy_value = calculate_entropy(metrics)
    diversity_factor = int(entropy_value * 10)
    
    # Final decision path
    if diversity_factor > 30:
        temp_result += 5
    else:
        temp_result += 3
    
    # Apply bonus/penalty
    final_adjustment = bonus - penalty
    temp_result += final_adjustment
    
    # Irrelevant string transformation (distractor)
    status_msg = "Performance: Optimal" if temp_result > 20 else "Review Needed"
    char_count = len(status_msg.replace(" ", ""))
    
    final_score = temp_result + 5  # Final assignment
    
    return final_score

# Main execution
raw_input = [88, 92, 76, 85, 94]
processed = preprocess_metrics(raw_input)
filtered = filter_outliers(processed, 2.0)
evaluation_threshold = 80
final_score = evaluate_performance(filtered, evaluation_threshold)
print(f"Target result: {final_score}")