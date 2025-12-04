from collections import Counter

def analyze_text(input_text):
    # Clean and normalize the text
    cleaned_text = input_text.lower().strip()
    
    # Split text into words
    words = cleaned_text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Some basic statistics
    total_words = len(words)
    unique_words = len(word_counts)
    average_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Find the difference between most and least frequent words
    frequency_difference = max(word_counts.values()) - min(word_counts.values())
    
    # Calculate a text complexity score (not relevant to our main task)
    complexity_score = unique_words / total_words * 10 if total_words > 0 else 0
    
    return frequency_difference

# Sample text for analysis
sample_text = "the quick brown fox jumps over the lazy dog the fox was quick"

# Get the result
result = analyze_text(sample_text)
print(f"Result: {result}")