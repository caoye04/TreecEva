import itertools

# Function to analyze text statistics
def analyze_text(text):
    # Remove spaces and convert to lowercase
    processed_text = text.lower().replace(" ", "")
    
    # Count letter frequencies
    letter_counts = {}
    for char in processed_text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Find most common character
    character_frequency = max(letter_counts.values())
    
    # Calculate average word length (not used in final result)
    words = text.split()
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return character_frequency

# Sample text from a book review
sample_text = "The book was excellent and engaging from start to finish"
result = analyze_text(sample_text)
print(f"Result: {result}")