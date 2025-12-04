from collections import Counter, defaultdict

def analyze_text(text):
    # Count character frequencies
    char_freq = Counter(text.lower())
    
    # Extract patterns of consecutive characters
    patterns = []
    for i in range(len(text) - 2):
        pattern = text[i:i+3].lower()
        if pattern.isalpha():
            patterns.append(pattern)
    
    # Count pattern occurrences
    pattern_counter = Counter(patterns)
    
    # Create dictionary of patterns by first letter (not used in final calculation)
    patterns_by_first = defaultdict(list)
    for p in patterns:
        patterns_by_first[p[0]].append(p)
    
    # Calculate some statistics (distraction)
    avg_pattern_length = sum(len(p) for p in patterns) / max(1, len(patterns))
    max_count = max(pattern_counter.values()) if pattern_counter else 0
    min_count = min(pattern_counter.values()) if pattern_counter else 0
    range_count = max_count - min_count
    
    # Find unique patterns
    unique_patterns = len(pattern_counter)
    
    # Calculate complexity score (distraction)
    complexity = (unique_patterns * 0.8) + (len(char_freq) * 0.2)
    normalized_complexity = min(100, complexity * 2)
    
    return unique_patterns, normalized_complexity

# Sample text for analysis
sample = "Programming problems require logical thinking and attention to detail."

# Process alternate text (distraction)
alternate = "Python is fun!"
alt_result, alt_complexity = analyze_text(alternate)

# Process main sample
result, complexity = analyze_text(sample)

print(f"Result: {result}")