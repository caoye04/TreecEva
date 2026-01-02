def analyze_pattern(sequence):
    count_vowels = lambda s: sum(1 for c in s.lower() if c in 'aeiou')
    sequence_length = len(sequence)
    vowel_count = count_vowels(sequence)
    ratio = vowel_count / sequence_length if sequence_length > 0 else 0

    # Irrelevant distraction: character frequency map (not used later)
    freq_map = {}
    for char in sequence:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Misleading intermediate score
    temp_score = (vowel_count * 10) + (sequence_length // 2)
    normalized = round(ratio * 100, 2)

    return normalized


def process_results(data, importance_weights):
    base_values = []
    adjustment_factor = 0.85

    for item in data:
        raw_value = len(item) ** 2
        adjusted = raw_value * adjustment_factor
n        base_values.append(adjusted)

    # Dead computation path: unused list transformation
    inverted = [1.0 / x for x in base_values if x != 0]
    inverted_sum = sum(inverted)

    # Real processing begins here
    weighted_sum = 0
    total_weight = 0

    for i, val in enumerate(base_values):
        weight = importance_weights[i % len(importance_weights)]
        weighted_sum += val * weight
        total_weight += weight

    average_weighted = weighted_sum / total_weight if total_weight > 0 else 0

    # Apply non-linear scaling via lambda
    scale_fn = lambda x: x ** 0.5 if x > 0 else 0
    final_score = int(scale_fn(average_weighted) * 10)

    # Extra irrelevant state tracking
    log_entry = {
        "timestamp": "ignored",
        "source": "dummy",
        "size": len(base_values)
    }

    return final_score

# Main execution
input_strings = ['algorithm', 'function', 'variable', 'lambda', 'syntax']
weights = [0.9, 1.2, 0.7]

interim_results = []
for s in input_strings:
    metric = analyze_pattern(s)
    interim_results.append(metric)

# Unused transformed version (distraction)
rounded_metrics = [round(x, 1) for x in interim_results]
mapped_metrics = list(map(lambda x: x * 1.1, interim_results))

validation_data = input_strings  # Final input assignment
final_score = process_results(validation_data, weights)
print(f"Result: {final_score}")