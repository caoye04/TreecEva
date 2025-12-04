import itertools

# Text processing function for analyzing word matches
def analyze_text_similarity(source_text, target_text):
    # Split texts into words and remove punctuation
    source_words = [word.strip('.,!?;:"()') for word in source_text.split()]
    target_words = [word.strip('.,!?;:"()') for word in target_text.split()]
    
    # Filter out empty strings
    filtered_words = [word for word in source_words if word]
    
    # Count words with special characters
    special_char_count = len([word for word in filtered_words if not word.isalnum()])
    
    # Find length of shorter list to avoid index errors
    compare_length = min(len(filtered_words), len(target_words))
    
    # Truncate lists to equal length for comparison
    filtered_words = filtered_words[:compare_length]
    target_words = target_words[:compare_length]
    
    # Count matching words (case-insensitive)
    matching_count = sum(1 for i, (word1, word2) in enumerate(zip(filtered_words, target_words)) if word1.lower() == word2.lower())
    
    # Calculate similarity score (not used in final result)
    similarity = matching_count / compare_length if compare_length > 0 else 0
    
    return matching_count

# Example texts
source = "The quick brown fox jumps over the lazy dog"
target = "The quick brown fox jumped over the sleepy dog"

# Calculate and print the result
result = analyze_text_similarity(source, target)
print(f"Result: {result}")