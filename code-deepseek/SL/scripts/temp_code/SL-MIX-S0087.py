from collections import Counter

def analyze_text_frequency(text_data):
    # Distractor: Irrelevant character processing
    temp_chars = [chr((ord(c) + 3) % 128) for c in text_data if c.isalpha()]
    shifted_text = ''.join(temp_chars)
    
    # Main logic: Character frequency analysis
    char_counts = Counter(text_data.lower())
    vowels = 'aeiou'
    vowel_counts = {v: char_counts.get(v, 0) for v in vowels}
    
    # Distractor: Misleading intermediate calculation
    total_chars = sum(char_counts.values())
    irrelevant_sum = sum(ord(c) for c in text_data[:5]) % 100
    
    # Core computation: Vowel-to-consonant ratio analysis
    consonant_count = sum(char_counts[c] for c in char_counts if c.isalpha() and c not in vowels)
    vowel_total = sum(vowel_counts.values())
    
    # Distractor: Unused bitwise operations
    bit_check = vowel_total & consonant_count
    shift_check = (vowel_total << 2) | consonant_count
    
    # Main result processing
    if vowel_total > 0 and consonant_count > 0:
        ratio_analysis = (vowel_total * 100) / consonant_count
        processed_results = [ratio_analysis, vowel_total, consonant_count]
    else:
        processed_results = [0, 0, 0]
    
    # Final assignment
    final_analysis = processed_results[-1]
    print(f"Target result: {final_analysis}")
    return final_analysis

# Test execution
test_text = "ProgrammingEvaluationBenchmarkComplexReasoning"
result = analyze_text_frequency(test_text)
