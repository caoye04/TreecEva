from collections import Counter

def analyze_word_frequency(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in text)
    words = cleaned_text.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Calculate statistics
    total_words = len(words)
    unique_words = len(word_counts)
    
    # Find most common words and their frequencies
    most_common = word_counts.most_common(3)
    top_word, top_count = most_common[0] if most_common else ('', 0)
    
    # Calculate density metrics
    avg_frequency = total_words / unique_words if unique_words else 0
    max_frequency = top_count if most_common else 0
    
    # Determine threshold settings
    use_alternative = unique_words > 10 and max_frequency > 5
    density_factor = 0.75 if use_alternative else 0.5
    
    # Set base density value
    base_density = 100
    
    # Calculate adjusted density
    adjusted_density = base_density * density_factor
    
    # Calculate maximum density
    max_density = max_frequency * (avg_frequency / 2)
    
    # Determine optimal threshold for word significance
    optimal_threshold = max_density / (2 if use_alternative else 1)
    
    # Calculate alternate metrics (not used in final result)
    alternate_score = (total_words * 0.1) + (unique_words * 0.3)
    potential_threshold = alternate_score / 10
    
    print(f"Result: {optimal_threshold}")
    return optimal_threshold

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
result = analyze_word_frequency(sample_text)