from collections import defaultdict, Counter

def analyze_text_patterns(text_block):
    words = text_block.lower().split()
    word_freq = Counter(words)
    
    # Distractor: character analysis (not used in final result)
    char_count = defaultdict(int)
    for word in words:
        for char in word:
            char_count[char] += 1
    
    # Relevant: compute average word length
    total_length = sum(len(word) for word in words)
    avg_word_length = total_length / len(words) if words else 0
    
    # Distractor: find palindromes (not used)
    palindromes = [word for word in set(words) if word == word[::-1] and len(word) > 1]
    
    return word_freq, avg_word_length

def transform_keys(raw_freq, shift_factor):
    shifted = {}
    for k, v in raw_freq.items():
        new_key = ''.join(chr((ord(c) - ord('a') + shift_factor) % 26 + ord('a')) for c in k)
        shifted[new_key] = v * 2  # arbitrary transformation
    # Dead code path
    if False:
        shifted = {k.upper(): v for k, v in shifted.items()}
    return shifted

def calculate_final_score(data_dict):
    score = 0
    for idx, (key, value) in enumerate(data_dict.items()):
        if idx % 2 == 0:
            score += value * (idx + 1)
        else:
            score -= value
    # Additional logic
    temp_result = [score ^ i for i in range(3)]  # irrelevant computation
    return abs(score)

def main():
    input_text = "The quick brown fox jumps over the lazy dog multiple times daily"
    
    # Step 1: Analyze text
    frequency_map, average_len = analyze_text_patterns(input_text)
    
    # Distractor: manipulate average length in unused way
    normalized_avg = round(average_len * 1.5, 2)
    adjustment = normalized_avg if normalized_avg > 5 else 0
    
    # Step 2: Transform keys
    shifted_map = transform_keys(frequency_map, shift_factor=3)
    
    # Distractor: zipping unrelated sequences
    indices = list(range(len(shifted_map)))
    paired_data = list(zip(indices, shifted_map.values()))
    
    # Step 3: Prepare for scoring
    processed_data = defaultdict(int)
    for i, (k, v) in enumerate(shifted_map.items()):
        if i % 3 != 0:  # thin filtering
            processed_data[k] = v + i

    # Key statement
    final_score = calculate_final_score(processed_data)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()