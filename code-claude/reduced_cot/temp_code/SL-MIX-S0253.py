def analyze_text(text, target="python"):
    # Count occurrences of each character
    char_count = {}
    for char in text.lower():
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Extract word with most vowels
    words = text.lower().split()
    max_vowels = 0
    filtered_word = ""
    
    for word in words:
        # Calculate vowel count
        vowel_count = sum(1 for c in word if c in 'aeiou')
        
        # Track word with most vowels
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            filtered_word = word
    
    # Calculate bitwise operations on ASCII values
    ascii_sum = sum(ord(c) for c in filtered_word)
    ascii_xor = 0
    for c in filtered_word:
        ascii_xor ^= ord(c)
    
    # Find common characters between filtered word and target
    unique_chars = len(set(filtered_word) & set(target))
    
    # Calculate some statistics that aren't used in final result
    avg_length = sum(len(w) for w in words) / len(words) if words else 0
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    
    print(f"Target result: {unique_chars}")
    return unique_chars

text_sample = "Programming languages are fascinating and educational."
result = analyze_text(text_sample)
