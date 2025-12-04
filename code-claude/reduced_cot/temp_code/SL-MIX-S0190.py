def text_analysis(input_text):
    # Parse and analyze text data
    words = input_text.lower().split()
    
    # Track character frequencies (distractor)
    char_freq = {}
    for word in words:
        for char in word:
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Define importance weights
    weights = {'technical': 5, 'urgent': 8, 'critical': 10, 'normal': 2, 'low': 1}
    ignored_terms = {'the', 'and', 'or', 'if', 'but', 'on', 'in', 'at', 'to'}
    
    # Generate meaningless statistics (distractor)
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    vowel_count = sum(1 for word in words for char in word if char.lower() in 'aeiou')
    
    # Process words with misleading intermediate calculations
    processed = []
    skip_next = False
    for i, word in enumerate(words):
        if skip_next:
            skip_next = False
            continue
        
        # Apply complex but irrelevant transformations (distractor)
        if len(word) > 7:
            word = word[::-1]  # Reverse long words (distractor)
        elif len(word) % 2 == 0:
            word = word.upper()  # Convert even-length words to uppercase (distractor)
        
        # This condition is always false (dead code path)
        if word.startswith('xyz') and word.endswith('abc'):
            skip_next = True
            continue
            
        processed.append(word)
    
    # Filter words based on criteria
    filtered_words = [word for word in processed if word not in ignored_terms]
    
    # Calculate priority based on keyword matches
    def calculate_priority(word_list, weight_dict):
        # Misleading calculation (distractor)
        potential = sum(len(set(w)) for w in word_list)
        
        # Actual calculation that matters
        base_score = 0
        for word in word_list:
            if word in weight_dict:
                base_score += weight_dict[word]
        
        # More distracting calculations
        modifier = len(word_list) / 10
        adjusted = base_score * modifier
        
        # This is the key calculation
        return base_score + 15
    
    # Track sentiment (distractor)
    sentiment_words = {'good': 1, 'great': 2, 'excellent': 3, 'bad': -1, 'poor': -2, 'terrible': -3}
    sentiment_score = sum(sentiment_words.get(word, 0) for word in words)
    
    # Calculate the priority score
    priority_score = calculate_priority(filtered_words, weights)
    
    # Additional misleading calculations (distractor)
    complexity_index = (avg_word_length * vowel_count) / 100
    engagement_metric = (sentiment_score + complexity_index) * 2
    
    print(f"Result: {priority_score}")
    return priority_score

# Sample text for analysis
sample_text = "urgent technical issue needs attention but the priority is normal"
result = text_analysis(sample_text)