def analyze_text_metrics(text):
    char_count = len(text)
    upper_case_count = sum(1 for c in text if c.isupper())
    lower_case_count = sum(1 for c in text if c.islower())
    space_count = text.count(' ')
    unique_chars = len(set(text))

    # Distractor: irrelevant computation on vowels
    vowel_ratio = sum(1 for c in text.lower() if c in 'aeiou') / len(text) if text else 0

    return {
        'length': char_count,
        'upper': upper_case_count,
        'lower': lower_case_count,
        'spaces': space_count,
        'uniqueness': unique_chars / char_count if char_count > 0 else 0
    }


def compute_weighted_index(metrics):
    w1, w2, w3 = 0.3, 0.1, 0.2
    base = metrics['length'] * w1
    bonus = metrics['upper'] * w2
    penalty = metrics['spaces'] * 0.05
    diversity_factor = metrics['uniqueness'] * w3

    # Semi-relevant but not used later
    theoretical_max = 100 if metrics['length'] > 50 else 80

    return base + bonus + diversity_factor - penalty


def evaluate_performance(input_str):
    temp_result = input_str.replace('!', '').replace('.', '')
    processed = temp_result.strip().title()  # distractor transformation

    metrics = analyze_text_metrics(input_str)
    index_val = compute_weighted_index(metrics)

    # Conditional expression (required feature)
    adjustment = 10 if metrics['lower'] > metrics['upper'] else -5

    # Lambda function (required feature)
    scaler = lambda x: round(x * 1.5, 2) if x < 20 else round(x * 1.2, 2)
    adjusted_index = scaler(index_val)

    # Core logic step
    raw_score = adjusted_index + adjustment

    # Dead code path (distractor)
    if len(input_str) == 100:
        raw_score *= 0.9  # never reached in this case

    # Final calculation
    final_score = int(raw_score * 2) if raw_score > 0 else 0

    return final_score

# Execution entry point
input_data = "Hello World This Is A Complex Evaluation Benchmark For Code Reasoning Capabilities"
result_metrics = analyze_text_metrics(input_data)
temp_var_shadow = result_metrics['length'] * 0.1  # unused distraction

final_score = evaluate_performance(input_data)
print(f"Target result: {final_score}")