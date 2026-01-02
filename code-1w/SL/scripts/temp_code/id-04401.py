def analyze_text(text_list):
    char_count_map = {}
    upper_case_tally = 0
    total_chars = 0

    for idx, text in enumerate(text_list):
        char_count_map[idx] = len(text)
        total_chars += len(text)
        if text and text[0].isupper():
            upper_case_tally += 1

    avg_length = total_chars / len(text_list) if text_list else 0
    return char_count_map, avg_length, upper_case_tally


def transform_data(raw_counts, multiplier=2):
    scaled_values = []
    temp_sum = 0

    for i, (key, count) in enumerate(zip(range(len(raw_counts)), raw_counts.values())):
        adjusted = (count * multiplier) + i
        temp_sum += adjusted
        scaled_values.append(adjusted)

    # Irrelevant transformation
    inverted = [1 / (x + 1) for x in scaled_values]
    normalized = [x / (temp_sum + 1e-5) for x in scaled_values]

    return scaled_values, normalized


def calculate_final_score(data):
    base = sum(data)
    penalty = 0

    for i, val in enumerate(data):
        if i % 2 == 1:
            penalty += val * 0.1

    score = base - penalty
    bonus = len(data) * 0.5

    # Dead code - never used
    debug_info = {'iterations': len(data), 'max_val': max(data) if data else 0}

    return int(score + bonus)

# Main execution
input_texts = [
    "Hello World",
    "Python Code",
    "Large Language Models",
    "Arithmetic and Logic",
    "Code Reasoning Task"
]

# Step 1: Analyze text inputs
counts_map, average_len, uppercase_start = analyze_text(input_texts)

# Step 2: Transform the character counts
raw_scores, norms = transform_data(counts_map, multiplier=3)

# Step 3: Calculate final score
final_score = calculate_final_score(raw_scores)

# Output result
print(f"Result: {final_score}")