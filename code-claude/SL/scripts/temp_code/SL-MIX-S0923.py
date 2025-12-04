from collections import Counter
import itertools

def analyze_text(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.lower().replace(' ', '')
    
    # Count letter frequencies
    letter_counts = Counter(cleaned_text)
    
    # Find the most common letter
    most_common = letter_counts.most_common(1)[0][0]
    
    # Calculate some statistics (not all are used)
    total_chars = len(cleaned_text)
    unique_chars = len(letter_counts)
    entropy_factor = unique_chars / (total_chars if total_chars > 0 else 1)
    
    # Generate some pairs for analysis (distraction)
    char_pairs = list(itertools.combinations(letter_counts.keys(), 2))
    pair_count = len(char_pairs)
    
    # Find distribution pattern (unused calculation)
    distribution_pattern = sum([ord(c) % 5 for c in cleaned_text])
    
    # Get the highest frequency count
    top_frequency = max(letter_counts.values())
    
    # Calculate a weighted score (distraction)
    weighted_score = sum(count * (ord(char) % 10) for char, count in letter_counts.items())
    
    # Calculate character variance (distraction)
    char_positions = {}
    for i, char in enumerate(cleaned_text):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)
    
    position_variance = sum(len(positions) for positions in char_positions.values())
    
    return top_frequency, most_common, weighted_score

# Sample text for analysis
sample_text = "Hello Python Programming"

# Analyze the text
top_frequency, most_common, weighted_score = analyze_text(sample_text)

# Display results
print(f"Result: {top_frequency}")