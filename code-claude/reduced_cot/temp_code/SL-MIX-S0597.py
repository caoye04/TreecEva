from collections import Counter, defaultdict

# Text analysis function to find keyword relevance
def analyze_text(text, keywords, weights):
    # Process input text
    text = text.lower().replace(',', ' ').replace('.', ' ')
    words = text.split()
    
    # Count word frequencies (not directly used for result)
    word_freq = Counter(words)
    most_common = word_freq.most_common(3)  # Get 3 most common words
    
    # Create sets for intersection analysis
    text_set = set(words)
    keyword_set = set(keywords)
    
    # Track various metrics
    total_words = len(words)
    unique_words = len(text_set)
    
    # Calculate keyword density (distractor calculation)
    density = sum(word_freq[kw] for kw in keywords if kw in word_freq) / total_words if total_words > 0 else 0
    
    # Store different metrics in dictionary
    metrics = defaultdict(int)
    metrics['density'] = round(density * 100, 2)  # Convert to percentage
    metrics['unique_ratio'] = unique_words / total_words if total_words > 0 else 0
    
    # Apply weight factors
    base_score = 10
    multiplier = 2 if metrics['density'] > 5 else 3
    
    # This is the key calculation for our answer
    common_count = len(text_set & keyword_set) * multiplier
    
    # Additional calculations that don't affect the result
    relevance = base_score * metrics['density'] / 100
    adjusted_score = relevance + (metrics['unique_ratio'] * 5)
    
    # Slicing operations on the text (not used in final result)
    first_chars = ''.join([word[0] for word in words[:5] if len(word) > 0])
    
    return common_count

# Sample inputs
sample_text = "Python programming is both fun and practical. Python offers many libraries."
keywords = ["python", "programming", "libraries", "code", "developer"]
weight_factors = {"relevance": 0.7, "density": 0.3}

# Run analysis
result = analyze_text(sample_text, keywords, weight_factors)
print(f"Result: {result}")