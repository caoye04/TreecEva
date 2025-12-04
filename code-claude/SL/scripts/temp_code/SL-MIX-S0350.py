# Text processing function to analyze word patterns
def count_special_words(text, min_length):
    # Split text into words and remove punctuation
    words = text.replace(',', '').replace('.', '').split()
    
    # Some basic text statistics
    total_words = len(words)
    avg_length = sum(len(w) for w in words) / total_words if total_words > 0 else 0
    
    # Filter words based on criteria: longer than min_length and all lowercase
    filtered_count = len(list(filter(lambda w: len(w) > min_length and w.islower(), words)))
    
    # Calculate ratio (not needed for main task)
    ratio = filtered_count / total_words if total_words > 0 else 0
    
    return filtered_count

# Sample text for analysis
sample = "Python is GREAT for text processing. lambda functions make it efficient."
result = count_special_words(sample, 3)
print(f"Result: {result}")