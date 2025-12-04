def count_occurrences(text, pattern):
    # Helper function to count occurrences of a pattern in text
    count = 0
    start_pos = 0
    while True:
        pos = text.find(pattern, start_pos)
        if pos == -1:
            break
        count += 1
        start_pos = pos + 1
    
    # This is never used but looks important
    frequency = count / max(1, len(text))
    return count

def extract_metadata(text):
    # Extract fake metadata that won't be used
    metadata = {}
    if 'title:' in text.lower():
        title_pos = text.lower().find('title:')
        metadata['title'] = text[title_pos+6:].split('\n')[0].strip()
    if 'author:' in text.lower():
        author_pos = text.lower().find('author:')
        metadata['author'] = text[author_pos+7:].split('\n')[0].strip()
    return metadata

def calculate_sentiment(text):
    # Fake sentiment calculation
    positive_words = ['good', 'great', 'excellent', 'best', 'amazing']
    negative_words = ['bad', 'poor', 'terrible', 'worst', 'awful']
    
    text_lower = text.lower()
    positive_score = sum(text_lower.count(word) for word in positive_words)
    negative_score = sum(text_lower.count(word) for word in negative_words)
    
    # Distraction calculation that looks important
    sentiment_value = (positive_score - negative_score) / max(1, len(text.split()))
    return positive_score - negative_score

def calculate_priority(document_text, keyword_weights):
    # This is the main function that calculates the priority score
    base_score = 0
    document_lower = document_text.lower()
    
    # Extract words and clean them
    words = document_lower.replace('.', ' ').replace(',', ' ').split()
    unique_words = set(words)
    
    # Calculate word frequency (distraction)
    word_freq = {}
    for word in words:
        if len(word) > 2:  # Only count words with length > 2
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Calculate average word length (distraction)
    avg_word_length = sum(len(word) for word in words) / max(1, len(words))
    
    # Extract potential keywords based on length (distraction)
    potential_keywords = [word for word in unique_words if len(word) > 5]
    
    # Calculate keyword presence score (actual calculation)
    keyword_score = 0
    for keyword, weight in keyword_weights.items():
        # Count occurrences using our helper function
        occurrences = count_occurrences(document_lower, keyword)
        keyword_score += occurrences * weight
    
    # Calculate sentiment (distraction)
    sentiment = calculate_sentiment(document_text)
    
    # Extract metadata (distraction)
    metadata = extract_metadata(document_text)
    metadata_bonus = 5 if 'title' in metadata else 0
    
    # Calculate complexity score (distraction)
    complexity_score = avg_word_length * 2.5
    
    # This is the key calculation
    base_score = len(unique_words) // 10
    priority_score = base_score + keyword_score
    
    # This looks important but isn't used
    adjusted_score = priority_score * (1 + 0.1 * sentiment)
    
    # Add misleading final adjustment
    final_boost = sum(ord(c) % 3 for c in document_text[:10])
    
    return priority_score

# Sample document
document_text = "The project deadline is approaching quickly. Team members need to prioritize their tasks effectively. The most important items should be completed first. Please review the documentation carefully."

# Keyword weights
keyword_weights = {
    'deadline': 5,
    'important': 8,
    'prioritize': 7,
    'urgent': 9,
    'critical': 10,
    'review': 4,
    'immediately': 8
}

# Distraction variables and calculations
possible_scores = []
for i in range(3):
    temp_text = document_text[:-(i*10)] if i > 0 else document_text
    temp_score = len(temp_text.split()) + i*5
    possible_scores.append(temp_score)

# Another distraction
max_possible = max(keyword_weights.values()) * sum(1 for word in document_text.split())

# Calculate the priority score
priority_score = calculate_priority(document_text, keyword_weights)

# More distractions after the key calculation
alternative_score = len(document_text) // 10
if 'urgent' in document_text.lower():
    alternative_score += 15

# This looks like it might modify the priority score but doesn't
if priority_score > 30:
    adjusted_priority = priority_score * 1.1
elif priority_score < 10:
    adjusted_priority = priority_score * 0.9
else:
    adjusted_priority = priority_score

print(f"Result: {priority_score}")