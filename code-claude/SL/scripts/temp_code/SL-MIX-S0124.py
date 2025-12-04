def analyze_text(input_text):
    # Remove any punctuation and normalize the text
    cleaned_text = ""
    for char in input_text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
    
    # Count words in the text
    word_count = len(cleaned_text.split())
    
    # Calculate average word length
    words = cleaned_text.split()
    total_length = sum(len(word) for word in words)
    avg_length = total_length / word_count if word_count > 0 else 0
    
    # Count unique letters used
    unique_letters = len(set(cleaned_text.lower()))
    
    # Print detailed analysis
    print(f"Word count: {word_count}")
    print(f"Average word length: {avg_length:.2f}")
    print(f"Unique letters used: {unique_letters}")
    
    return unique_letters

# Sample text for analysis
sample = "The quick brown fox jumps over the lazy dog"

# Run the analysis
result = analyze_text(sample)
print(f"Result: {result}")