def analyze_text_patterns(input_text):
    # Irrelevant preprocessing: count vowels (not used in final result)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in input_text.lower() if c in vowels)

    # Split text into words and compute various stats
    words = input_text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]

    # Compute average length, median length (semi-relevant)
    avg_length = sum(word_lengths) / len(word_lengths)
    sorted_lengths = sorted(word_lengths)
    n = len(sorted_lengths)
    median_length = (sorted_lengths[n//2] + sorted_lengths[(n-1)//2]) / 2

    # Use enumerate and zip to pair indices with lengths (actual use begins here)
    indexed_pairs = list(enumerate(zip(words, word_lengths)))

    # Extract only words longer than average (rounded)
    threshold = int(avg_length) + 1
    long_words = [word for word, length in zip(words, word_lengths) if length > threshold]

    # Misleading distraction: reverse sorting and take top 3 by length (unused)
    reversed_sorted = sorted(word_lengths, reverse=True)
    top_three_sum = sum(reversed_sorted[:3])

    # Actual relevant logic: count how many long words start with same letter as last word
    last_word_first_letter = words[-1][0].lower()
    matching_count = sum(1 for w in long_words if w[0].lower() == last_word_first_letter)

    # Return both irrelevant and relevant data (only one will be used later)
    return {
        'vowel_count': vowel_count,
        'avg_length': avg_length,
        'matching_long_words': matching_count,
        'median_length': median_length,
        'top_three_sum': top_three_sum  # dead end
    }


def calculate_final_score(data_dict):
    base = data_dict['matching_long_words'] * 7
    adjustment = int(data_dict['avg_length'])
    bonus = 0
    
    # Conditional bonus based on median (irrelevant since median >= 4 always true here)
    if data_dict['median_length'] >= 4:
        bonus += 3
        temp_val = data_dict['vowel_count'] % 5  # unused
        for i in range(bonus):
            temp_val += i ** 2  # red herring loop

    # Distractor: nested loop over dummy range
    penalty = 0
    for i in range(2):
        for j in range(3):
            penalty += (i + j) % 2

    # Final score calculation — only base and adjustment matter
    final_score = base + adjustment - penalty
    return final_score

# Main execution
text = "The quick brown fox jumps over the lazy dog near the riverbank"

# Preprocess and extract features
analysis_result = analyze_text_patterns(text)

# Key statement: compute final score from processed data
final_score = calculate_final_score(analysis_result)

print(f"Result: {final_score}")