def analyze_text_patterns(text_block):
    # Split text into words and compute various statistics
    words = text_block.split()
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if words else 0

    # Character frequency analysis (some distraction)
    char_freq = {}
    for char in ''.join(words):
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Extract only letters a-e frequency (semi-relevant)
    rare_count = sum(count for char, count in char_freq.items() if char in 'abcde')

    # Compute pattern score using lambda
    weight_func = lambda x: x * 1.5 if x > 4 else x * 0.8
    length_score = sum(weight_func(length) for length in word_lengths)

    # Red herring: counting uppercase (not used later)
    uppercase_count = sum(1 for char in text_block if char.isupper())

    # Return core metrics
    return {
        'avg_word_length': avg_length,
        'total_words': len(words),
        'length_score': length_score,
        'rare_char_density': rare_count / len(words) if len(words) > 0 else 0
    }


def calculate_overall_score(result_dict):
    # Apply weighted combination
    base = result_dict['avg_word_length'] * 2.5
    bonus = result_dict['total_words'] * 0.7
    penalty = result_dict['rare_char_density'] * 1.2
    raw = base + bonus - penalty
    
    # Normalize through sigmoid-like scaling (not strictly necessary but adds logic step)
    normalized = raw * 0.9 if raw > 10 else raw * 1.1
    
    # Final adjustment based on threshold
    return int(normalized + result_dict['length_score'] * 0.05)

# Main execution
input_text = "Dynamic programming solves complex problems by breaking them into simpler subproblems"

# Intermediate analysis with distraction variables
analysis_result = analyze_text_patterns(input_text)

# Unused data structures to increase cognitive load
unused_histogram = {i: 0 for i in range(1, 10)}
for w in input_text.split():
    wl = len(w)
    if wl < 10:
        unused_histogram[wl] += 1

# Simulated secondary metric (dead code path)
secondary_metric = 0
if len(input_text) % 2 == 0:
    for k in analysis_result:
        secondary_metric += len(k)  # Irrelevant accumulation

# Core calculation point
final_score = calculate_overall_score(analysis_result)

# Print result as required
print(f"Target result: {final_score}")