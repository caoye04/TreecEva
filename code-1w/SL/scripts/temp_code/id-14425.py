def analyze_text_patterns(text):
    char_count = {}
    for c in text:
        char_count[c] = char_count.get(c, 0) + 1
    return char_count

# Irrelevant helper function (distractor)
def compute_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 4)

# Semi-relevant preprocessing step
def extract_features(seq):
    freq_map = analyze_text_patterns(seq)
    frequencies = list(freq_map.values())
    avg_freq = sum(frequencies) / len(frequencies) if frequencies else 0
    # Dummy transformation
    transformed = list(map(lambda x: x ** 0.5 + 1, frequencies))
    return avg_freq, len(transformed)

# Core logic with distractors
def evaluate_performance(weights, data):
    baseline = 100
    adjustment = 0
    
    # Simulate multi-step scoring logic
    raw_sum = sum(data)
    normalized = [x / raw_sum for x in data if x > 0]

    # Slice analysis (relevant)
    mid_section = normalized[1:-1]
    slice_avg = sum(mid_section) / len(mid_section) if mid_section else 0

    # Weight application
    weighted_total = 0
    for i, w in enumerate(weights):
        if i < len(normalized):
            weighted_total += w * normalized[i]

    # Dummy state tracking (distractor)
    history_log = []
    for step in range(3):
        temp_val = (baseline + step * 2) % 7
        history_log.append(temp_val)  # unused later

    # Multiple assignments (irrelevant)
    temp_a, temp_b = 5, 10
    temp_a, temp_b = temp_b, temp_a + 1  # swapping distraction

    # Actual score computation
    base_score = baseline * slice_avg
    penalty = len([x for x in weights if x < 0.1]) * 5
    bonus = len(weights) - len(data) if len(weights) > len(data) else 0

    adjustment = (weighted_total * 10) + bonus - penalty
    final_score = base_score + adjustment

    return int(final_score)

# Main execution
metric_weights = [0.3, 0.5, 0.1, 0.15, 0.08]
raw_data = [25, 10, 30, 15]

# Preprocessing side work (semi-relevant)
input_string = "aabbcdeffg"
avg_feat, trans_length = extract_features(input_string)

# Actual target computation
final_score = evaluate_performance(metric_weights, raw_data)

print(f"Result: {final_score}")