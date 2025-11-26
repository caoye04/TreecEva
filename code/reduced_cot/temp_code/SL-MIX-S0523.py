def analyze_text_patterns(text_data):
    # Irrelevant processing that doesn't affect final result
    word_list = text_data.split()
    char_counts = [len(word) for word in word_list]  # list comprehension
    total_chars = sum(char_counts)
    
    # Misleading calculations that look important
    avg_length = total_chars / len(word_list) if word_list else 0
    max_length = max(char_counts) if char_counts else 0
    
    # Dead code path that doesn't get executed
    if len(text_data) > 1000:
        bonus_points = 15
        # This branch never executes with current input
    
    # The actual relevant processing
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text_data if char in vowels)
    consonant_count = len(text_data) - vowel_count - text_data.count(' ')
    
    # More misleading intermediate results
    ratio = vowel_count / consonant_count if consonant_count > 0 else 0
    complexity_score = vowel_count * 2 + consonant_count // 3
    
    return vowel_count, consonant_count, complexity_score

# Main execution with distractions
input_text = "The quick brown fox jumps over the lazy dog"
vowels, consonants, complexity = analyze_text_patterns(input_text)

# Irrelevant variables that don't contribute to final result
temp_buffer = [vowels * 2, consonants // 2, complexity + 10]
shadow_counter = temp_buffer[0] + temp_buffer[1] - temp_buffer[2]

# Misleading calculations that look like they matter
redundancy_factor = len(input_text) % 7
quality_index = (vowels + consonants) // len(input_text.split())

# The actual relevant computations
processed_data = vowels * 3 - consonants // 2
adjustment_factor = quality_index * 2
redundancy_offset = redundancy_factor + 5

# Final calculation that gives the answer
final_count = processed_data + adjustment_factor - redundancy_offset

# Print the result
print(f"Result: {final_count}")