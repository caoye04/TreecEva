from itertools import combinations

def analyze_text_patterns(text_blocks):
    char_frequencies = {}
    total_chars = 0

    for block in text_blocks:
        cleaned = block.strip().lower()
        vowels = 'aeiou'
        vowel_count = 0
        consonant_count = 0

        for char in cleaned:
            if char.isalpha():
                total_chars += 1
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

                char_frequencies[char] = char_frequencies.get(char, 0) + 1

        # Irrelevant ratio (not used later)
        if consonant_count > 0:
            ratio_vc = vowel_count / consonant_count

    return char_frequencies, total_chars

def extract_ngrams(text_list, n=3):
    ngram_counts = {}
    for text in text_list:
        normalized = ''.join(filter(str.isalpha, text.lower()))
        for i in range(len(normalized) - n + 1):
            ngram = normalized[i:i+n]
            ngram_counts[ngram] = ngram_counts.get(ngram, 0) + 1
    # Dead code path - never used
    if False:
        return sorted(ngram_counts.keys())
    return ngram_counts

def calculate_final_score(freq_dict):
    score = 0.0
    weights = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    for char, count in freq_dict.items():
        if char in weights:
            score += count * weights[char]
        else:
            score += count * 0.5  # consonants add smaller value
    # Additional distraction: unused transformation
    temp_zipped = list(zip(['x','y','z'], [1,2,3]))
    adjusted_score = round(score * 1.07, 4)
    return adjusted_score

def main():
    raw_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Data analysis requires careful reasoning and validation.",
        "Language models must handle complexity with precision."
    ]

    # Step 1: Analyze character frequencies (core data)
    frequencies, total_length = analyze_text_patterns(raw_texts)

    # Step 2: Extract trigrams (distractor - not used in scoring)
    trigram_map = extract_ngrams(raw_texts, n=3)

    # Step 3: Filter only alphabetic chars for processing (redundant but adds logic)
    processed_data = {k: v for k, v in frequencies.items() if k.isalpha()}

    # Step 4: Compute weighted score based on letter type
    intermediate_sum = sum(processed_data.values())
    average_freq = intermediate_sum / len(processed_data) if processed_data else 0

    # Step 5: Calculate final score using vowel weighting scheme
    final_score = calculate_final_score(processed_data)

    # Step 6: Some irrelevant enumeration (adds cognitive load)
    indexed_items = []
    for idx, (letter, freq) in enumerate(processed_data.items()):
        if freq > average_freq:
            indexed_items.append((idx, letter.upper(), freq))

    # Step 7: Output result (only this matters)
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()