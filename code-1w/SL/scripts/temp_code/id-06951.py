def analyze_text_metrics(text_data):
    char_count = len(text_data)
    upper_case_count = sum(1 for c in text_data if c.isupper())
    lower_case_count = sum(1 for c in text_data if c.islower())
    digit_count = sum(1 for c in text_data if c.isdigit())
    space_count = text_data.count(' ')
    
    # Irrelevant statistical distraction
    avg_char_position = sum(ord(c) for c in text_data) / char_count if char_count else 0
    entropy_approx = 0.0
    for c in set(text_data):
        freq = text_data.count(c) / char_count
        entropy_approx -= freq * __import__('math').log2(freq) if freq > 0 else 0
    
    # Semi-relevant transformation (not used in final path but looks important)
    normalized_text = ''.join(c.lower() if c.isalpha() else ' ' for c in text_data)
    
    # Key metric extraction using enumerate and zip
    position_weights = [i + 1 for i in range(len(text_data))]
    weighted_sum = sum((ord(c) - 96) * w for i, c in enumerate(text_data.lower()) if c.isalpha() for w in [position_weights[i]])
    
    # Conditional logic with red herring branches
    adjustment_factor = 0
    if upper_case_count > lower_case_count:
        adjustment_factor += 10
    elif digit_count > space_count:
        adjustment_factor += 5
    else:
        adjustment_factor -= 3  # This branch actually triggers
    
    # Distractor: unused helper list
    stats_summary = [
        f"Chars: {char_count}",
        f"Uppercase: {upper_case_count}",
        f"Lowercase: {lower_case_count}",
        f"Digits: {digit_count}"
    ]
    
    # Real computation chain
    base_score = char_count * 2 + upper_case_count * 3 - space_count
    bonus = 0
    for i, (a, b) in enumerate(zip(text_data, text_data[1:])):
        if a.islower() and b.isupper():
            bonus += 2
        elif a.isdigit() and b == ' ':
            bonus += 1
    
    # Final determination with conditional expression
    final_score = base_score + bonus + (adjustment_factor if adjustment_factor > 0 else -adjustment_factor * 2)
    
    # Dead code - never executed but looks integrated
    if False:
        temp_result = __import__('math').sqrt(base_score)
        final_score = int(temp_result)
    
    return final_score

def calculate_final_score(input_str):
    if not input_str:
        return 0
    return analyze_text_metrics(input_str)

# Execution point
input_text = "Hello123WorLD test CASE 456"
result = calculate_final_score(input_text)
print(f"Target result: {result}")