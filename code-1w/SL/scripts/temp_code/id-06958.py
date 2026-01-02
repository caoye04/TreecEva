def analyze_text_quality(text):
    if not text:
        return 0
    words = text.split()
    long_words = [w for w in words if len(w) > 5]
    unique_chars = len(set(text.replace(' ', '')))
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
    return (len(long_words) + unique_chars) / (avg_word_length + 1)


def validate_sequence(seq):
    valid_count = 0
    for item in seq:
        if isinstance(item, int) and item > 0:
            temp_flag = (item % 2 == 0)
            if temp_flag:
                valid_count += 1
    return valid_count > 3


def process_metrics(values):
    adjusted = []
    outlier_threshold = sum(values) / len(values) * 1.5
    for v in values:
        if v < outlier_threshold:
            adjusted.append(v ** 0.5)
        else:
            adjusted.append(0)  # Ignore outliers
    norm_factor = max(adjusted) if adjusted else 1
    return [x / norm_factor for x in adjusted] if norm_factor else []


def calculate_final_score(raw_data):
    # Extract relevant fields
    text_data = raw_data.get('content', '')
    numeric_values = raw_data.get('metrics', [])
    sequence_data = raw_data.get('sequence', [])

    # Irrelevant distraction: complex string analysis with unused result
    uppercase_ratio = sum(1 for c in text_data if c.isupper()) / len(text_data) if text_data else 0
    reversed_text = text_data[::-1]
    palindrome_check = reversed_text == text_data  # Not used later

    # Step 1: Text quality score
    text_score = analyze_text_quality(text_data)

    # Step 2: Validate sequence (boolean guard)
    is_valid_seq = validate_sequence(sequence_data)

    # Step 3: Process numeric metrics
    processed_metrics = process_metrics(numeric_values)
    metric_base = sum(processed_metrics) * 100

    # Distractor: unused intermediate calculation
    squared_sums = sum(x**2 for x in numeric_values)  # Dead end
    temp_result = [x for x in processed_metrics if x > 0.5]  # Semi-relevant but unused

    # Step 4: Conditional adjustment based on validation
    if is_valid_seq:
        adjustment = len(sequence_data) % 7
    else:
        adjustment = -3

    # Step 5: Combine scores with weighting
    raw_total = text_score * 10 + metric_base + adjustment

    # Step 6: Clamp and scale
    clamped = max(10, min(raw_total, 95))

    # Final transformation
    final_score = int(round(clamped + len(numeric_values) - len(sequence_data) // 4))

    return final_score

# Input data
input_data = {
    'content': 'The algorithm efficiently computes results using advanced logic and careful design principles',
    'metrics': [12, 18, 25, 8, 34, 45, 22],
    'sequence': [1, 4, 6, 8, 10, 12]
}

# Execution
result = calculate_final_score(input_data)
print(f"Result: {result}")