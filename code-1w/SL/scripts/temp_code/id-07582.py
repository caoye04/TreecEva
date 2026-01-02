def analyze_frequency(text_blocks):
    char_freq = {}
    for block in text_blocks:
        cleaned = ''.join([ch.lower() for ch in block if ch.isalpha()])
        for char in cleaned:
            char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq


def filter_relevant(freq_map, threshold):
    filtered = {k: v for k, v in freq_map.items() if v >= threshold}
    sorted_keys = sorted(filtered.keys())
    temp_result = 0
    for key in sorted_keys:
        temp_result += ord(key) % 7
    return filtered


def transform_data(raw_counts):
    transformed = [v ** 2 - k for k, v in enumerate(raw_counts.values())]
    offset = sum(transformed) % len(transformed) if transformed else 1
    adjusted = [val + offset for val in transformed]
    return adjusted


def compute_modular_weight(seq):
    total = 0
    for i, val in enumerate(seq):
        total += (val * (i + 1)) % 13
    checksum = sum(seq) % 10
    dummy_var = [x for x in seq if x % 2 == 0]  # irrelevant list comprehension
    return total % checksum if checksum != 0 else total


def calculate_final_score(data_list):
    base_sum = sum(data_list)
    penalty = 0
    for idx, value in enumerate(data_list):
        if value > 50 and idx % 2 == 0:
            penalty += value // 10
    bonus = len(data_list) * 2 if base_sum > 100 else 0
    return base_sum - penalty + bonus

# Main execution
input_texts = [
    "AlphaBetaGamma123",
    "DeltaEpsilonZeta!",
    "ThetaLambdaSigma?"
]

freq_analysis = analyze_frequency(input_texts)
distraction_map = {chr(i): i for i in range(97, 100)}  # unused distraction

filtered_chars = filter_relevant(freq_analysis, 2)
transformed_values = transform_data(filtered_chars)

# Simulate intermediate diagnostic check
consistency_check = 0
for v in transformed_values:
    consistency_check += (v * 3) % 5

mod_weight = compute_modular_weight(transformed_values)
processed_data = [mod_weight, len(transformed_values), sum(transformed_values[:2])] + transformed_values

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")