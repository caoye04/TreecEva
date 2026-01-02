def analyze_text_patterns(input_text):
    char_count = {}
    for char in input_text:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1

    frequencies = list(char_count.values())
    avg_freq = sum(frequencies) / len(frequencies) if frequencies else 0

    above_avg = [freq for freq in frequencies if freq > avg_freq]
    stability_index = len(above_avg) / len(frequencies) if frequencies else 0

    return stability_index, char_count


def transform_dataset(raw_entries):
    normalized = []
    total_length = 0
    for entry in raw_entries:
        stripped = entry.strip().replace("_", " ")
        word_list = stripped.split()
        capitalized = [word.capitalize() for word in word_list]
        normalized.append(' '.join(capitalized))
        total_length += len(stripped)
    
    average_entry_length = total_length / len(raw_entries) if raw_entries else 0
    return normalized, average_entry_length


def filter_relevant_items(items, thresholds):
    valid_items = []
    scores = []
    noise_counter = 0
    for i, (item, threshold) in enumerate(zip(items, thresholds)):
        item_value = sum([ord(c) for c in item])
        if item_value > threshold * 100:
            valid_items.append(item)
            scores.append(item_value)
        else:
            noise_counter += 1
    
    if noise_counter > 5:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.1
    
    final_scores = [s * adjustment_factor for s in scores]
    return final_scores


def calculate_final_score(data):
    base_score = sum(data) / len(data) if data else 0
    penalty = 0
    for val in data:
        if val < 1000:
            penalty += 5
    adjusted_score = base_score - penalty
    bonus = len(data) * 0.5
    return int(adjusted_score + bonus)

# Main execution block
raw_input = [
    "hello_world", "python_code", "ai_benchmark", "language_model",
    "reasoning_chain", "data_processing", "complex_logic", "code_analysis",
    "string_methods", "enumerate_zip"
]

threshold_values = [7, 8, 6, 9, 5, 8, 7, 6, 5, 10]

# Step 1: Analyze text patterns (not directly used but part of distraction)
stability, char_map = analyze_text_patterns(''.join(raw_input))

# Step 2: Transform dataset
cleaned_data, avg_len = transform_dataset(raw_input)

# Step 3: Filter relevant items based on thresholds
intermediate_results = filter_relevant_items(cleaned_data, threshold_values)

# Irrelevant computation - distractor
entropy_proxy = 0
for k, v in char_map.items():
    if v > 2:
        entropy_proxy += ord(k) % 7

# Step 4: Calculate final score
final_score = calculate_final_score(intermediate_results)

# Output result
print(f"Result: {final_score}")