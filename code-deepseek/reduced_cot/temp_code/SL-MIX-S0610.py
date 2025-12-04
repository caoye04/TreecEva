import collections

def analyze_text_patterns(text):
    # Distractor: Character frequency analysis (not directly used in final result)
    char_counter = collections.Counter(text.lower())
    vowel_count = sum(char_counter[v] for v in 'aeiou')
    
    # Misleading intermediate calculation
    consonant_ratio = len([c for c in text if c.isalpha() and c.lower() not in 'aeiou']) / max(1, vowel_count)
    
    # Relevant computation: Word length analysis
    words = text.split()
    word_lengths = [len(word) for word in words]
    
    # Dead code path - never executed
    if len(words) > 20:
        bonus_points = 15
    else:
        bonus_points = 0
    
    # Main logic: Score based on average word length and unique characters
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    unique_chars = len(set(text.lower()))
    
    # Irrelevant bitwise operation
    bit_mask = (len(text) << 2) & 0xFF
    
    return round(avg_word_length * 10 + unique_chars * 2, 2)

def process_text_analysis(input_text):
    # Multiple irrelevant computations
    text_length = len(input_text)
    space_count = input_text.count(' ')
    
    # Distractor: Case conversion analysis
    upper_ratio = sum(1 for c in input_text if c.isupper()) / max(1, text_length)
    
    # Call to actual analysis function
    base_score = analyze_text_patterns(input_text)
    
    # More misleading calculations
    word_count = len(input_text.split())
    density_factor = word_count / max(1, text_length) * 100
    
    # Final relevant computation
    final_score = base_score - (density_factor / 10)
    
    # Unused variable
    complexity_index = (upper_ratio * 50) + (space_count * 3)
    
    return round(final_score, 2)

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog while running through the forest"

# Irrelevant preprocessing (never affects result)
temp_text = sample_text.replace('the', 'THE')
capital_count = sum(1 for c in temp_text if c.isupper())

# Main execution
result = process_text_analysis(sample_text)
print(f"Target result: {result}")