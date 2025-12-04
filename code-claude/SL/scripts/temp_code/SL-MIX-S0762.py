from collections import Counter, defaultdict

def analyze_text_patterns(text, min_length=3):
    # Process text and extract patterns (unused function)
    words = text.lower().split()
    patterns = defaultdict(int)
    for word in words:
        if len(word) >= min_length:
            for i in range(len(word) - min_length + 1):
                pattern = word[i:i+min_length]
                patterns[pattern] += 1
    return dict(sorted(patterns.items(), key=lambda x: x[1], reverse=True)[:10])

def calculate_sentiment(text):
    # Simplified sentiment calculation (misleading function)
    positive = sum(1 for word in text.lower().split() if word in ['good', 'great', 'excellent'])
    negative = sum(1 for word in text.lower().split() if word in ['bad', 'poor', 'terrible'])
    return positive - negative

def calculate_priority(word_frequencies, document, threshold):
    # This is the key function that determines the priority score
    total_words = sum(word_frequencies.values())
    unique_words = len(word_frequencies)
    
    # Extract document metadata (distractor)
    doc_lines = document.split('\n')
    doc_sections = [line for line in doc_lines if line.startswith('#')]
    section_count = len(doc_sections)
    
    # Calculate base score using word frequency metrics
    if total_words > 0:
        average_freq = total_words / unique_words
    else:
        average_freq = 0
    
    # Apply various transformations (some relevant, some not)
    complexity_factor = len([w for w in word_frequencies if len(w) > 5]) / max(1, unique_words)
    diversity_score = unique_words / max(1, total_words) * 100
    
    # Misleading calculations that don't affect final result
    potential_score = (diversity_score * 1.5) + (complexity_factor * 25) - (section_count * 2)
    adjusted_score = potential_score + calculate_sentiment(document) * 3
    
    # The actual priority calculation
    if average_freq > threshold:
        base_priority = (average_freq - threshold) * 10
    else:
        base_priority = average_freq * 5
    
    # Final priority calculation (the key part)
    priority_score = int(base_priority + (diversity_score / 10))
    
    # More distractor code
    if section_count > 0 and False:  # Never executes
        priority_score += section_count * 2
    
    return priority_score

# Sample document content
doc_content = """# Introduction
This document describes the text analysis approach.
# Methodology
We use frequency analysis and pattern matching.
# Results
The results show interesting patterns in word usage.
"""

# Process document (distractor code)
processed_text = doc_content.lower().replace('.', ' ').replace(',', ' ')
word_list = [w for w in processed_text.split() if len(w) > 2]
word_freq = Counter(word_list)

# Another distractor - pattern analysis
patterns = analyze_text_patterns(doc_content)
pattern_strength = sum(patterns.values()) / len(patterns) if patterns else 0

# Variables for priority calculation
threshold_value = 1.2  # Threshold for frequency significance
base_multiplier = 2.5  # Unused multiplier
section_weight = 1.8   # Unused weight

# Calculate misleading metrics
text_density = len(word_list) / len(doc_content.split())
doc_complexity = sum(len(word) for word in word_list) / len(word_list)

# This is the key statement
priority_score = calculate_priority(word_freq, doc_content, threshold_value)

# More distractor calculations that don't affect the answer
final_score = priority_score
if pattern_strength > 3:
    final_score += pattern_strength * 0.5
if doc_complexity > 5:
    final_score *= 1.1

print(f"Result: {priority_score}")