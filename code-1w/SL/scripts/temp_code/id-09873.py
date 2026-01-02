from itertools import combinations

def analyze_sequence(data):
    count = 0
    for i in range(len(data)):
        if data[i] == 'A':
            for pair in combinations(data[i:], 2):
                if pair[0] == 'A' and pair[1] == 'C':
                    count += 1
    return count

def normalize(value, min_val, max_val):
    # Irrelevant normalization function (not used in final logic)
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def calculate_entropy(text):
    from collections import Counter
    freq = Counter(text)
    total = len(text)
    entropy = 0
    for char, cnt in freq.items():
        p = cnt / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def evaluate_performance(metrics, baseline):
    adjustment_factor = 0.85
    penalty = 0
    bonus = 0

    # Distractor variables
    temp_result = sum([v ** 0.5 for v in metrics.values() if v > 3])
    debug_info = {'temp_sum': temp_result, 'version': '2.1'}

    # Actual logic
    if metrics['accuracy'] >= baseline['accuracy']:
        bonus += 15
    if metrics['precision'] < baseline['precision']:
        penalty += 10
    if metrics['recall'] > baseline['recall']:
        bonus += 10

    stability = metrics['consistency']
    if stability > 90:
        bonus += 5
    elif stability < 70:
        penalty += 5

    raw_score = metrics['accuracy'] + bonus - penalty
    final_score = int(raw_score * adjustment_factor)

    # Dead code path (never executed due to constant condition)
    if False:
        fallback = __import__('math').ceil(raw_score * 0.9)
        final_score = fallback

    return final_score

# Main execution
input_seq = "AACGTACGAA"
occurrences = analyze_sequence(input_seq)
entropy_value = calculate_entropy(input_seq)

# Simulated performance metrics
metrics = {
    'accuracy': 88 + occurrences,         # 88 + 6 = 94
    'precision': 82,
    'recall': 78,
    'consistency': 92
}

baseline = {
    'accuracy': 90,
    'precision': 80,
    'recall': 75
}

intermediate_calc = list(map(lambda x: x * 2, [1, 2, 3]))  # Unused mapped list
useless_string_op = "analysis".upper().replace('S', 'X')   # Red herring operation

final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")