import itertools

def analyze_document(text):
    # Document analysis metrics
    word_count = len(text.split())
    char_count = len(text)
    avg_word_length = char_count / max(1, word_count)
    
    # Parse document sections (unused in final calculation)
    sections = text.split('.')
    section_metrics = []
    for section in sections:
        words = section.strip().split()
        if len(words) > 0:
            section_metrics.append({
                'length': len(words),
                'avg_word_len': sum(len(w) for w in words) / len(words) if words else 0
            })
    
    return word_count, avg_word_length, section_metrics

def calculate_engagement(metrics):
    # Complex engagement formula (distractor)
    base_score = metrics[0] * 0.3 + metrics[1] * 0.7
    multiplier = 1.0
    if metrics[0] > 100:
        multiplier += 0.25
    if metrics[1] > 5.0:
        multiplier += 0.15
    
    return base_score * multiplier

def filter_keywords(words, min_length=4):
    # Filter words by criteria
    filtered = []
    ignored = []
    
    for word in words:
        if len(word) >= min_length and not word.isdigit():
            filtered.append(word)
        else:
            ignored.append(word)
    
    # Track unused metrics (distractor)
    ignored_ratio = len(ignored) / len(words) if words else 0
    longest_ignored = max([len(w) for w in ignored]) if ignored else 0
    
    return filtered

def calculate_priority(words, weights):
    if not words or not weights:
        return 0
    
    # Priority calculation
    initial_score = 0
    for i, word in enumerate(words[:5]):  # Only first 5 words matter
        position_factor = 6 - i  # Position weight decreases
        length_factor = min(len(word) / 2, 5)  # Cap length factor at 5
        initial_score += position_factor * length_factor
    
    # Apply weights (only first two weights matter)
    weighted_score = initial_score * weights[0]  # First weight is multiplicative
    weighted_score += weights[1]  # Second weight is additive
    
    # Distractor operations
    adjustment = 0
    for w in weights[2:]:  # These weights are ignored
        adjustment += w / 10
    
    # This looks important but doesn't affect the result
    combinations = list(itertools.combinations(words[:3], 2))
    combo_factor = len(combinations) * 0.1
    
    # Integer division and rounding
    final_score = int(weighted_score) // 3 * 3  # Integer division by 3, then multiply by 3
    
    return final_score

# Sample document
document = "The quick brown fox jumps over the lazy dog. This is a simple test document with keywords."

# Document analysis
word_count, avg_length, section_data = analyze_document(document)
engagement = calculate_engagement([word_count, avg_length])

# Process words
words = document.lower().replace('.', '').split()
filtered_words = filter_keywords(words)

# Weight configurations
primary_weights = [2.5, 15, 0.8, 1.2]  # Only first two matter
backup_weights = [1.8, 9, 0.5, 0.7]  # Distractor

# Conditional selection of weights
if word_count > 20:
    weights = primary_weights
else:
    weights = backup_weights

# Alternate calculation path (distractor)
if avg_length > 10:  # This condition is false
    special_factor = sum(len(w) for w in filtered_words if 'e' in w)
    priority_score = special_factor * 0.75
else:
    # This is the actual calculation path
    priority_score = calculate_priority(filtered_words, weights)

# Final adjustments (distractor)
combined_metrics = word_count + len(filtered_words)
if combined_metrics > 50:  # This condition is false
    priority_score += 10

print(f"Result: {priority_score}")