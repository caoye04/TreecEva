from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:
                count += 1
    return count

def filter_outliers(data, limit=50):
    # Irrelevant filtering (not used in final logic)
    return [x for x in data if x <= limit]

def compute_entropy(values):
    # Distractor function: computes entropy but not used
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log
    return -sum(p * log(p) for p in probs if p > 0)

def process_results(results, threshold):
    # Main relevant logic
    passed = [r for r in results if r >= threshold]
    failed = [r for r in results if r < threshold]
    
    temp_sum = sum(passed) * 0.8  # Weighted contribution
    bonus = 0
    
    # Meaningful nested logic with interdependency
    if len(passed) > 3:
        bonus += 10
        combos = list(combinations(passed, 2))
        stable_pairs = 0
        for a, b in combos:
            if abs(a - b) <= 5:
                stable_pairs += 1
        if stable_pairs >= 4:
            bonus += 7
    
    # Secondary path: distractor with partial relevance
    avg_failed = sum(failed) / len(failed) if failed else 0
    penalty = 0
    if avg_failed > 0:
        penalty = int(avg_failed / 5)
    
    # Core answer computation
    base_score = len(passed) * 15
    final_score = base_score + bonus - penalty
    
    # Dead code branch (never reached due to logic above)
    if len(results) == 100:
        final_score *= 1.1
    
    return final_score

# Simulated dataset
raw_data = [68, 72, 65, 80, 90, 45, 30, 85, 77, 82]
noise_filter = filter_outliers(raw_data, 40)  # Unused result
entropy_value = compute_entropy([10, 20, 30])  # Computed but irrelevant
pattern_count = analyze_patterns([2, 5, 3, 4, 1])  # Side analysis

assessment_data = [78, 85, 90, 65, 80, 72, 88, 74]
passing_threshold = 70

# Key execution point
final_score = process_results(assessment_data, passing_threshold)
print(f"Target result: {final_score}")