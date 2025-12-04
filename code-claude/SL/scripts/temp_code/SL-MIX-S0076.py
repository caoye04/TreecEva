def text_analyzer(text_content, keywords=None):
    # Process text for analysis
    if keywords is None:
        keywords = ["python", "algorithm", "data", "function"]
    
    word_count = len(text_content.split())
    char_count = sum(not c.isspace() for c in text_content)
    
    # Calculate irrelevant metrics
    complexity_factor = (char_count / max(1, word_count)) * 0.8
    redundancy_index = len(set(text_content.lower().split())) / max(1, word_count)
    
    return {
        "words": word_count,
        "chars": char_count,
        "complexity": complexity_factor,
        "redundancy": redundancy_index
    }

def calculate_keyword_impact(text, keywords):
    # Count keyword occurrences with position weighting
    text_lower = text.lower()
    words = text_lower.split()
    
    # Distracting calculations
    entropy_value = sum(ord(c) % 7 for c in text) / 100
    pattern_strength = len([w for w in words if len(w) > 5]) / max(1, len(words))
    
    # Actual keyword processing
    total_impact = 0
    for keyword in keywords:
        if keyword in text_lower:
            # Position matters - earlier mentions have higher weight
            positions = [i for i, word in enumerate(words) if keyword in word]
            if positions:
                # This is the key calculation
                pos_weight = sum(0.9 ** pos for pos in positions)
                total_impact += pos_weight
            
            # Misleading calculation
            frequency = text_lower.count(keyword)
            distribution_factor = frequency * entropy_value
    
    # More distraction
    semantic_density = pattern_strength * entropy_value
    if semantic_density > 0.5:
        total_impact = total_impact * 1.0  # No actual change
    
    return total_impact

def apply_transformations(base_value):
    # Series of transformations to confuse
    transformed = base_value * 2
    transformed = transformed + 10
    
    # Dead code path
    if transformed < 0:
        transformed = abs(transformed) * 0.5
    
    transformed = transformed / 2
    transformed = transformed - 5
    
    # Another dead branch
    if base_value == 0:
        return 0
    
    return transformed

def calculate_final_score(text_content, keyword_weights):
    # Analyze basic text properties
    text_metrics = text_analyzer(text_content)
    
    # Distraction: unused lambda functions
    normalize = lambda x, min_val, max_val: (x - min_val) / (max_val - min_val) if max_val > min_val else 0
    sigmoid = lambda x: 1 / (1 + 2.71828 ** -x)
    
    # Calculate base score from text properties
    base_score = text_metrics["words"] * 0.1
    
    # Misleading calculation path
    potential_multiplier = text_metrics["complexity"] * 5
    adjusted_redundancy = 1 - text_metrics["redundancy"]
    unused_score = base_score * potential_multiplier * adjusted_redundancy
    
    # Extract keywords from weights dictionary
    keywords = list(keyword_weights.keys())
    
    # Calculate keyword impact
    keyword_impact = calculate_keyword_impact(text_content, keywords)
    
    # Apply keyword weights
    weighted_impact = 0
    for keyword, weight in keyword_weights.items():
        if keyword in text_content.lower():
            weighted_impact += weight
    
    # Combine metrics for final score
    combined_score = base_score + keyword_impact * 2
    
    # Apply final transformations
    final_score = apply_transformations(combined_score)
    
    return final_score

# Sample text for analysis
text_content = "Python is a powerful programming language for data analysis. Python functions make algorithms easier to implement."

# Keyword weights dictionary
keyword_weights = {
    "python": 2.5,
    "algorithm": 1.8,
    "data": 1.5,
    "function": 1.2
}

# Calculate the document score
document_score = calculate_final_score(text_content, keyword_weights)

# Check the result with a break early approach
if document_score > 100:
    print("High quality document!")
    document_score = 100  # Cap the score
elif document_score < 0:
    print("Document needs revision.")
    document_score = 0  # Minimum score

print(f"Result: {document_score}")