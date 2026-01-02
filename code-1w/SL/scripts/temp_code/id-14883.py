from collections import defaultdict
import math

def preprocess_input(raw_tokens):
    token_counts = defaultdict(int)
    for token in raw_tokens:
        cleaned = token.strip().lower()
        if len(cleaned) > 0:
            token_counts[cleaned] += 1

    frequency_list = [count for count in token_counts.values()]
    avg_frequency = sum(frequency_list) / len(frequency_list) if frequency_list else 0

    # Irrelevant computation - does not affect final result
    entropy = 0.0
    for count in frequency_list:
        prob = count / sum(frequency_list)
        if prob > 0:
            entropy -= prob * math.log(prob)

    return dict(token_counts), avg_frequency

def transform_values(count_dict, multiplier):
    transformed = {}
    temp_buffer = []

    for key, value in count_dict.items():
        shifted = value * multiplier + 2
        if 'a' in key:
            shifted = int(shifted * 1.5)
        elif 'e' in key:
            shifted = max(shifted - 1, 0)
        transformed[key] = shifted
        temp_buffer.append(shifted * 0.5)  # Unused buffer

    # Dead code path (never accessed in this execution)
    if False:
        for val in temp_buffer:
            transformed[f'dup_{val}'] = int(val)

    return transformed

def calculate_final_score(data_map):
    base_vals = [v for v in data_map.values() if v > 0]
    adjustment_factor = len(base_vals) % 7

    intermediate_sum = 0
    for val in base_vals:
        if val % 2 == 0:
            intermediate_sum += val ** 2
        else:
            intermediate_sum += val * 3

    # Distractor: complex but unused calculation
    secondary_score = 0
    for i, v in enumerate(base_vals):
        secondary_score += v * (i + 1)
    secondary_score = math.sqrt(secondary_score) if secondary_score > 0 else 0

    final_score = intermediate_sum - adjustment_factor * 3
    return final_score

# Main execution
raw_input = ["Apple", "Banana", "Avocado", "Cherry", "elderberry", "apricot"]

counts, average_freq = preprocess_input(raw_input)
adjusted_counts = transform_values(counts, multiplier=3)

# Key statement
final_score = calculate_final_score(adjusted_counts)

print(f"Result: {final_score}")