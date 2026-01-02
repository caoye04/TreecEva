from itertools import combinations

def analyze_frequency(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def normalize_values(raw_vals):
    total = sum(raw_vals)
    return [val / total for val in raw_vals] if total > 0 else raw_vals

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) / std_dev < threshold]

def evaluate_performance(metrics, base):
    adjusted = [m * 1.1 for m in metrics]
    diff_set = set(adjusted) - set(base)
    high_performers = [x for x in diff_set if x > sum(base) / len(base)]
    
    # Irrelevant combination generation (distractor)
    combo_check = list(combinations(high_performers, 2))
    valid_pairs = 0
    for pair in combo_check:
        if pair[0] + pair[1] > 150:
            valid_pairs += 1
    
    # Actual logic path
    temp_result = 0
    for val in high_performers:
        if val > 80:
            temp_result += int(val // 10)
    
    # Secondary adjustment based on baseline length (semi-relevant)
    bonus = len(base) % 4
    final_score = temp_result + bonus
    
    # Dead code branch (distractor)
    if False:
        fallback = sum(normalize_values(metrics))
        final_score = int(fallback * 100)
    
    return final_score

# Main execution
raw_text = "PerformanceEvaluation2024"
token_stream = [ord(c) % 100 for c in raw_text]
freq_map = analyze_frequency(raw_text)
values_only = list(freq_map.values())

baseline_metrics = [75, 82, 77, 88, 73]
candidate_metrics = [85, 90, 76, 92, 81, 87]

filtered_candidates = filter_outliers(candidate_metrics)
normalized_baseline = normalize_values(baseline_metrics)

# Key statement
final_score = evaluate_performance(filtered_candidates, baseline_metrics)
print(f"Result: {final_score}")