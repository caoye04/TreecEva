import itertools

# Function to analyze text patterns
def analyze_text(text):
    # Count words in the text
    word_count = len(text.split())
    
    # Find the first word
    word = text.split()[0]
    
    # Count characters in the first word
    char_count = len(word)
    
    # Find unique letters in the first word (case insensitive)
    unique_letters = len(set(word.lower()))
    
    # Calculate a simple metric
    metric = word_count + char_count
    
    return unique_letters, metric

# Sample text for analysis
sample = "Programming requires logical thinking"

# Perform the analysis
unique_count, total_metric = analyze_text(sample)

# Display results
print(f"Result: {unique_count}")