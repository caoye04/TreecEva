def is_palindrome(word):
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]

def count_valid_words(text):
    # Split text into words
    words = text.split()
    count = 0
    skipped = 0
    processed = []
    
    for word in words:
        # Distraction: calculate word metrics
        word_length = len(word)
        uppercase_count = sum(1 for c in word if c.isupper())
        lowercase_ratio = sum(1 for c in word if c.islower()) / max(word_length, 1)
        
        # Check if word starts with vowel
        starts_with_vowel = word.lower().startswith(('a', 'e', 'i', 'o', 'u'))
        
        # Distraction: bitwise operation on ASCII values
        word_xor_value = 0
        for char in word:
            word_xor_value ^= ord(char)
        
        # Words that are palindromes and at least 4 characters long are valid
        if is_palindrome(word) and word_length >= 4:
            count += 1
            processed.append(word)
        elif word_length > 2 and word_xor_value % 2 == 0:
            skipped += 1
    
    # Distraction: calculate statistics on processed words
    avg_length = sum(len(w) for w in processed) / max(len(processed), 1)
    
    return count

text = "Madam radar level deed refer kayak solos stats racecar"
text_reversed = text[::-1]  # Distraction: reverse the text

# Distraction: check if text contains any numbers
has_numbers = any(char.isdigit() for char in text)

final_count = count_valid_words(text)
print(f"Result: {final_count}")