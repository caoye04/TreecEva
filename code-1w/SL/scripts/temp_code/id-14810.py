def analyze_text_metrics(text_data):
    char_count = len(text_data)
    word_list = text_data.split()
    word_count = len(word_list)
    
    # Distractor: vowel counting (not used in final result)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in text_data.lower() if c in vowels)
    avg_vowels_per_word = vowel_count / word_count if word_count else 0

    # Distractor: unique consonants set (semi-relevant but not critical)
    consonants = {c for c in text_data.lower() if c.isalpha() and c not in vowels}
    unique_consonant_count = len(consonants)

    # Core logic: score based on length, repetition patterns, and word structure
    repeated_words = {w for w in word_list if word_list.count(w) > 1}
    repetition_penalty = len(repeated_words) * 2

    # Complexity metric: words longer than 5 letters
    complex_words = [w for w in word_list if len(w) > 5]
    complexity_bonus = len(complex_words) * 3

    # Conditional expression for style point (used later)
    style_modifier = 1.5 if '?' not in text_data and '!' not in text_data else 0.8

    # Intermediate scoring
    base_score = char_count + (word_count * 2)
    adjusted_score = base_score - repetition_penalty + complexity_bonus
    
    # Final computation with conditional adjustment
    final_score = int(adjusted_score * style_modifier)

    # Irrelevant debug print (dead code path)
    debug_info = f'Chars: {char_count}, Words: {word_count}'
    unused_flag = False
    if unused_flag:
        print(debug_info)

    return final_score

# Main execution
input_text = "The algorithm processes data and analyzes complex patterns to solve problems efficiently"
final_score = analyze_text_metrics(input_text)
print(f"Target result: {final_score}")