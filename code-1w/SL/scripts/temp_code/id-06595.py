def analyze_text_properties(text):
    char_count = len(text)
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    space_count = sum(1 for c in text if c.isspace())
    
    # Distractor: irrelevant linguistic metrics
    avg_word_length = char_count / (text.count(' ') + 1) if text else 0
    palindrome_check = text == text[::-1]  # Not used later
    
    return {
        'chars': char_count,
        'uppers': upper_count,
        'lowers': lower_count,
        'digits': digit_count,
        'spaces': space_count,
        'ratio': upper_count / lower_count if lower_count > 0 else 0
    }


def filter_relevant_entries(logs):
    filtered = []
    for log in logs:
        if 'ERROR' in log and 'retry' not in log:
            filtered.append(log.upper())
    return filtered


def compute_final_score(data):
    stats = analyze_text_properties(data)
    
    # Semi-relevant transformation
    base_score = stats['uppers'] * 3 + stats['digits'] * 5
    
    # Conditional expression (required python feature)
    penalty = 10 if stats['lowers'] > stats['uppers'] * 2 else 5
    
    # Additional distractor logic
    temp_modifier = 0
    for i in range(min(3, stats['digits'])):
        temp_modifier += i * 2  # Slight red herring, not critical
    
    # Nested condition with early exit (distractor)
    if stats['spaces'] == 0:
        return -1  # Unlikely case
    elif stats['chars'] < 10:
        base_score += 20
    else:
        multiplier = 2 if stats['ratio'] > 0.5 else 1
        base_score *= multiplier
    
    # Core logic path
    adjustment = stats['digits'] - stats['spaces']
    final_score = base_score - penalty + adjustment
    
    # Dead code branch (distractor)
    if False:
        final_score = sum(range(final_score % 10))
    
    return final_score

# Simulated input data
raw_logs = [
    'error: invalid input',
    'WARNING: retry attempt failed',
    'ERROR: no response from server',
    'INFO: system running normally'
]

filtered_data = filter_relevant_entries(raw_logs)
processed_text = ''.join(filtered_data)

# Key execution point
final_score = compute_final_score(processed_text)
print(f"Target result: {final_score}")