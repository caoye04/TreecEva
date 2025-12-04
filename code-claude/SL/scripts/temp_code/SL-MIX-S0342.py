# Function to find common characters between words in a text
def analyze_text(text):
    words = text.lower().split()
    
    if not words:
        return 0
    
    # Extract first two words for analysis
    word1 = words[0]
    word2 = words[1] if len(words) > 1 else ""
    
    # Calculate letter frequency in first word
    letter_count = {}
    for i, char in enumerate(word1):
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    # Find common characters between first two words
    common_chars = len(set(word1) & set(word2))
    
    # Calculate total characters in both words
    total_chars = len(word1) + len(word2)
    
    return common_chars

# Sample text for analysis
text = "Python programming is fun"
result = analyze_text(text)
print(f"Result: {result}")