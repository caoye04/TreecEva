def analyze_text_quality(text):
    char_count = len(text)
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    space_count = text.count(' ')
    
    # Distractor: irrelevant transformation
    reversed_text = text[::-1]
    palindrome_check = reversed_text == text  # Not used later

    # Compute ratios (some will be used later)
    upper_ratio = upper_count / char_count if char_count > 0 else 0
    lower_ratio = lower_count / char_count if char_count > 0 else 0
    
    # Intermediate metric - partially relevant
    case_balance = abs(upper_ratio - lower_ratio)

    # Dummy statistics with no impact
    digit_count = sum(1 for c in text if c.isdigit())
    special_char_count = char_count - upper_count - lower_count - space_count - digit_count
    
    # Hidden red herring: unused weighted score
    if digit_count > 0:
        fake_weighted = (upper_count * 2 + lower_count) / digit_count
    else:
        fake_weighted = 0  # Dead end

    return {
        'length': char_count,
        'uppercase': upper_count,
        'lowercase': lower_count,
        'balance': case_balance,
        'spaces': space_count
    }


def calculate_final_score(entries):
    scores = []
    total_chars = 0
    total_balance = 0.0

    for entry in entries:
        stats = analyze_text_quality(entry)
        
        # Relevant computation branch
        adjusted_length = stats['length'] - stats['spaces']
        if adjusted_length > 0:
            normalized_upper = stats['uppercase'] / adjusted_length
            normalized_lower = stats['lowercase'] / adjusted_length
        else:
            normalized_upper = 0
            normalized_lower = 0

        # Secondary distractor: unused complexity
        entropy_approx = 0
        if normalized_upper > 0 and normalized_lower > 0:
            import math
            entropy_approx = -(normalized_upper * math.log2(normalized_upper) + 
                             normalized_lower * math.log2(normalized_lower))

        # Core logic contributing to final score
        balance_factor = 1 - stats['balance']
        length_bonus = 1 if stats['length'] > 50 else 0.5
        
        entry_score = (balance_factor * 100) + (length_bonus * 10)
        scores.append(entry_score)
        total_chars += stats['length']
        total_balance += stats['balance']

    # Final aggregation
    avg_score = sum(scores) / len(scores) if scores else 0
    adjustment = (total_chars / 100) if total_chars > 0 else 0
    
    # Key line: this is where final_score is assigned
    final_score = avg_score + adjustment - (total_balance * 5)
    
    # Superfluous post-processing
    capped_score = min(final_score, 150)
    floored_score = max(capped_score, 0)
    
    return final_score

# Input data
data = [
    "The Quick Brown Fox Jumps Over The Lazy Dog",
    "HELLO world 2023!",
    "Python Code Optimization Task",
    "ANALYZE THIS UPPER CASE STRING NOW",
    "mixedCaseWithNumbers456"
]

# Execution point of interest
final_score = calculate_final_score(data)
print(f"Result: {final_score}")