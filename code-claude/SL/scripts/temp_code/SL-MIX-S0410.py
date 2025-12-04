import itertools

def process_text(text, filter_length=0):
    # Convert text to lowercase for processing
    normalized = text.lower()
    
    # Split into words and filter punctuation
    raw_words = normalized.split()
    words = [word.strip('.,!?;:()"') for word in raw_words]
    
    # Some analysis metrics that aren't used for the final result
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    max_length = max(len(word) for word in words) if words else 0
    
    # Filter words based on criteria - this is the key operation
    if filter_length > 0:
        return [word for word in words if len(word) >= filter_length]
    else:
        return words

# Sample text from a nature article
text = "The mountain ecosystem supports diverse flora and fauna. Animals adapt to high altitudes through various mechanisms. Plants develop specialized features to survive harsh conditions."

# Process with different parameters
all_words = process_text(text)
long_words = process_text(text, 8)
medium_words = process_text(text, 6)

# Create pairs of words for analysis (distractor operation)
pair_combinations = list(itertools.combinations(long_words, 2))

# Count words starting with specific letters
a_words = [word for word in all_words if word.startswith('a')]
t_words = [word for word in all_words if word.startswith('t')]

# Apply conditional logic to select filter criteria
if len(long_words) > 5:
    filter_value = 9
elif len(medium_words) > 10:
    filter_value = 7
else:
    filter_value = 5

# This is the key statement that determines the answer
filtered_words = process_text(text, filter_value)
final_count = len(filtered_words)

# Additional calculations that don't affect the result
conditional_sum = sum(1 for word in all_words if 'a' in word)
total_chars = sum(len(word) for word in filtered_words)

print(f"Result: {final_count}")