from itertools import chain

def process_text_data(text_corpus):
    words = text_corpus.lower().split()
    prefix_map = {}
    
    # Distractor: processing vowels (unused in final result)
    vowel_counts = {}
    vowels = 'aeiou'
    for word in words:
        vowel_count = sum(1 for char in word if char in vowels)
        vowel_counts[word] = vowel_count
    
    # Main logic: count words by prefix
    for word in words:
        if len(word) >= 3:
            prefix = word[:3]
            prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
    
    # Distractor: calculate average length (unused)
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Process word lengths with filtering
    length_counts = {}
    for word in words:
        word_len = len(word)
        if word_len >= 4:
            length_counts[word_len] = length_counts.get(word_len, 0) + 1
    
    # Distractor: process consonant counts (unused)
    consonant_totals = {}
    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        consonant_totals[word] = consonant_count
    
    processed_words = prefix_map
    target_prefix = 'pro'
    scaling_factor = 3
    
    # Final computation
    final_count = processed_words.get(target_prefix, 0) * scaling_factor
    print(f"Target result: {final_count}")
    return final_count

# Execute with sample data
text_sample = "programming problems provide practical projects for professional progress processing"
process_text_data(text_sample)