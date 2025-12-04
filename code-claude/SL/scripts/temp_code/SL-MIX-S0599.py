from collections import Counter

def calculate_relevance(text, keywords):
    # Calculate text relevance based on keyword frequency
    word_count = Counter(text.lower().split())
    relevance = sum(word_count[keyword.lower()] for keyword in keywords)
    return relevance

def calculate_priority(text, weight):
    # Priority calculation for document processing system
    keywords = ['urgent', 'important', 'critical']
    secondary_keywords = ['review', 'process', 'approve']
    
    # Extract metrics from text
    word_count = len(text.split())
    char_density = len(text) / (word_count if word_count > 0 else 1)
    
    # Calculate relevance scores
    primary_relevance = calculate_relevance(text, keywords)
    secondary_relevance = calculate_relevance(text, secondary_keywords)
    
    # Calculate priority metrics
    base_score = primary_relevance * 3 + secondary_relevance
    complexity_factor = (char_density / 5) if char_density > 5 else 1
    
    # These metrics don't affect final result but appear relevant
    urgency_level = min(5, primary_relevance * 2)
    processing_time = word_count * 0.05
    
    # Calculate adjusted weights (distraction - not used in final calculation)
    adjusted_weight = weight * 1.5 if urgency_level > 3 else weight
    
    # Calculate priority score
    priority_score = int(base_score * weight)
    
    # Log metrics for debugging (distraction)
    metrics = {
        'word_count': word_count,
        'char_density': char_density,
        'urgency': urgency_level,
        'processing_time': processing_time
    }
    
    return priority_score

# Document to process
document_text = "This is an urgent document that requires critical review. Please process this important request as soon as possible."

# Various weighting factors (some are distractions)
base_weight = 2
time_factor = 1.5
urgency_multiplier = 2
keyword_weight = 3

# Calculate document score with different approaches
alternative_score = lambda t, w: len(t.split()) * w // 10
density_score = len(document_text) / len(document_text.split()) * base_weight

# Calculate the final priority score
priority_score = calculate_priority(document_text, keyword_weight)

# Generate report
report_id = hash(document_text) % 1000
processed = True

print(f"Result: {priority_score}")