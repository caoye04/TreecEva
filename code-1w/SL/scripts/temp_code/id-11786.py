def analyze_text_complexity(text_block):
    words = text_block.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Distractor: character frequency map (not used later)
    char_freq = {}
    for char in text_block.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    long_words = [w for w in words if len(w.strip('.,!?"')) >= 6]
    complex_ratio = len(long_words) / len(words) if words else 0
    return avg_length, complex_ratio


def filter_relevant_entries(data_list):
    filtered = []
    total_chars = 0  # Red herring accumulator
    for entry in data_list:
        cleaned = entry.strip().lower()
        if 'error' not in cleaned and 'skip' not in cleaned:
            filtered.append(cleaned)
            total_chars += len(cleaned)  # Not used in final logic
    return filtered


def calculate_final_score(data):
    scores = []n    for item in data:
        # Simulate multi-step scoring
        temp_score = 0
        parts = item.split(' ')
        vowel_count = sum([1 for c in item if c in 'aeiou'])
        consonant_count = sum([1 for c in item if c.isalpha() and c not in 'aeiou'])
        
        # Irrelevant transformation
        reversed_parts = [p[::-1] for p in parts]
        
        # Core logic
        if len(parts) > 3:
            temp_score += 10
        if vowel_count > consonant_count:
            temp_score += 5
        elif vowel_count == consonant_count and vowel_count > 0:
            temp_score += 2
        
        # Use of set operation (required feature)
        unique_vowels = len(set([c for c in item if c in 'aeiou']))
        temp_score += unique_vowels * 3
        
        scores.append(temp_score)
    
    # Final aggregation
    final_value = sum(scores) // len(scores) if scores else 0
    
    # Dead code path (distractor)
    if final_value < 0:
        final_value = -final_value  # Never executed
    
    return final_value

# Main execution
raw_input = [
    "The quick brown fox jumps over lazy dog",
    "Error: invalid input detected here",
    "Programming with logic and care ensures success",
    "Skip this line due to noise", 
    "Beautiful code is both clear and efficient"
]

avg_len, _ = analyze_text_complexity(' '.join(raw_input))
processed_data = filter_relevant_entries(raw_input)
baseline_adjustment = int(avg_len * 2)  # Computed but unused

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")