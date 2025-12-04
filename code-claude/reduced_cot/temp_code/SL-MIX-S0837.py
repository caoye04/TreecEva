def calculate_priority(word_data, threshold):
    # Sort words by frequency and calculate priority score
    sorted_words = sorted(word_data.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize tracking variables
    base_value = 25
    multiplier = 1.5
    priority_sum = 0
    
    # Track some additional metrics (not directly used in final calculation)
    avg_length = sum(len(word) for word, _ in sorted_words) / len(sorted_words) if sorted_words else 0
    unique_letters = set(''.join(word for word, _ in sorted_words))
    letter_factor = len(unique_letters) / 26  # Proportion of alphabet used
    
    # Process only words above threshold with position weighting
    for i, (word, count) in enumerate(sorted_words[:5]):
        if count >= threshold:
            # Calculate word significance based on position and count
            position_weight = max(0, 1 - (i * 0.15))  # Decreasing weight by position
            word_value = int(count * position_weight * multiplier)
            
            # Apply length adjustment (distraction - not actually used)
            length_adjustment = len(word) / avg_length if avg_length > 0 else 1
            adjusted_value = word_value * length_adjustment
            
            # Only the word_value affects the final sum
            priority_sum += word_value
    
    # Calculate final priority score with base value
    priority_score = base_value + priority_sum
    
    # Apply a scaling factor based on threshold (distraction - not used)
    scaling = threshold / 10 if threshold > 0 else 1
    scaled_score = priority_score * scaling
    
    return priority_score

# Text analysis scenario
text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
words = text.lower().replace('.', '').split()

# Count word frequencies
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Some preprocessing operations (partially relevant)
filtered_words = [word for word in words if len(word) > 2]
unique_word_count = len(set(words))
common_threshold = 1

# Calculate various thresholds (only one is used)
max_count = max(word_counts.values()) if word_counts else 0
avg_count = sum(word_counts.values()) / len(word_counts) if word_counts else 0
threshold_value = 2  # This is the one actually used

# Process data with different approaches (distraction)
for i, word in enumerate(filtered_words[:3]):
    temp_score = len(word) * word_counts.get(word, 0)
    # This doesn't affect the final result

# Calculate the priority score
priority_score = calculate_priority(word_counts, threshold_value)

# Output the result
print(f"Result: {priority_score}")