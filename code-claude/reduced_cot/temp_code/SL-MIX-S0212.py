def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_string(text):
    return text[::-1]

def process_text(text):
    # Process text and count specific patterns
    word_list = text.split()
    
    # Calculate average word length for reference
    avg_length = sum(len(word) for word in word_list) / len(word_list) if word_list else 0
    
    # Count words with more vowels than consonants
    vowel_heavy = 0
    for word in word_list:
        if count_vowels(word) > (len(word) - count_vowels(word)):
            vowel_heavy += 1
    
    # Find palindromes (distractor calculation)
    palindrome_count = 0
    for word in word_list:
        if len(word) > 2 and word.lower() == reverse_string(word.lower()):
            palindrome_count += 1
    
    # Count words starting with capital letters
    capital_starters = sum(1 for word in word_list if word and word[0].isupper())
    
    # Calculate weighted score based on word positions (distractor calculation)
    position_score = 0
    for i, word in enumerate(word_list):
        if i % 3 == 0 and len(word) > 4:
            position_score += 2
    
    # Calculate final count: vowel-heavy words + capital starters - palindromes
    result = vowel_heavy + capital_starters
    
    return result

# Sample text for analysis
sample_text = "The Quick brown fox jumped Over the lazy Dog"

# Process the text and get the final count
final_count = process_text(sample_text)

print(f"Result: {final_count}")