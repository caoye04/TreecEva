def calculate_document_priority(words, keywords):
    # Dictionary to track keyword occurrences and positions
    keyword_data = {}
    priority_scores = {}
    irrelevant_stats = {}
    
    # Track some document statistics (not used for priority calculation)
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    unique_chars = len(set(''.join(words)))
    irrelevant_stats['avg_length'] = avg_word_length
    irrelevant_stats['unique_chars'] = unique_chars
    
    # Process words and find keywords
    for i, word in enumerate(words):
        word_lower = word.lower()
        
        # Track position data for all words (mostly unused)
        position_value = len(words) - i
        
        if word_lower in keywords:
            # Store keyword occurrence data
            if word_lower not in keyword_data:
                keyword_data[word_lower] = {'count': 0, 'positions': []}
            
            keyword_data[word_lower]['count'] += 1
            keyword_data[word_lower]['positions'].append(i)
    
    # Calculate priority scores for each keyword
    for keyword, data in keyword_data.items():
        # Position weight - earlier occurrences get higher weight
        position_weight = sum([len(words) - pos for pos in data['positions']])
        
        # Frequency weight - more occurrences increase priority
        frequency_weight = data['count'] * 5
        
        # Keyword length factor - longer keywords might be more specific
        length_factor = len(keyword) / 4
        
        # Calculate priority score with some bitwise operations for complexity
        base_score = position_weight + frequency_weight
        complexity_factor = (base_score & 0xF) | 0x10
        adjusted_score = (base_score + complexity_factor) * length_factor
        
        # Store in priority scores dictionary
        priority_scores[keyword] = int(adjusted_score)
    
    # Some additional calculations that don't affect the result
    word_diversity = len(set(word.lower() for word in words)) / len(words) if words else 0
    keyword_density = sum(data['count'] for data in keyword_data.values()) / len(words) if words else 0
    irrelevant_stats['diversity'] = word_diversity
    irrelevant_stats['keyword_density'] = keyword_density
    
    # Calculate total priority score
    total_priority = sum(priority_scores.values())
    
    # Additional processing that doesn't affect the result
    normalized_score = total_priority / (len(words) + 1)
    irrelevant_stats['normalized_score'] = normalized_score
    
    return total_priority, priority_scores, irrelevant_stats

# Sample document and keywords
document = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
keyword_list = ['quick', 'fox', 'lazy']

# Process document
total_priority, keyword_priorities, stats = calculate_document_priority(document, keyword_list)

# Display results
print(f"Keyword priorities: {keyword_priorities}")
print(f"Document statistics: {stats}")
print(f"Result: {total_priority}")