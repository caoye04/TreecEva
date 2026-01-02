def evaluate_performance(skills, feedback):
    # Normalize skill levels (relevant)
    normalized = [max(0, min(100, s)) for s in skills]
    
    # Calculate base proficiency (relevant)
    total_proficiency = sum(n * 0.3 for n in normalized)
    
    # Analyze feedback sentiment (partially relevant)
    positive_terms = ['good', 'excellent', 'improved', 'great']
    negative_terms = ['poor', 'bad', 'declined', 'weak']
    
    feedback_lower = feedback.lower()
    word_list = feedback_lower.split()
    
    pos_count = sum(1 for word in word_list if word.strip('.,!') in positive_terms)
    neg_count = sum(1 for word in word_list if word.strip('.,!') in negative_terms)
    
    # Distractor: Character frequency analysis (semi-relevant)
    char_freq = {}
    for char in feedback_lower:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    unique_letters = len(char_freq)
    
    # Distractor: Unused statistical measures
    avg_word_length = sum(len(w) for w in word_list) / len(word_list) if word_list else 0
    longest_word = max(word_list, key=len) if word_list else ''
    vowel_density = sum(1 for c in feedback_lower if c in 'aeiou') / len(feedback_lower) if feedback_lower else 0
    
    # Feedback impact score (relevant)
    sentiment_balance = pos_count - neg_count
    feedback_influence = min(20, max(-20, sentiment_balance * 5))
    
    # Secondary distractor: unused transformation
    transformed_skills = []
    for i, skill in enumerate(normalized):
        if i % 2 == 0:
            transformed_skills.append(skill * 1.1)
        else:
            transformed_skills.append(skill * 0.9)
    
    # Final performance score computation (key logic)
    base_offset = 50
    final_score = base_offset + (total_proficiency * 0.4) + feedback_influence
    
    # Irrelevant rounding variation
    final_score = round(final_score, 2)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
skill_levels = [85, 90, 78, 92, 88]
feedback_string = "Excellent effort and improved focus, but attention to detail declined slightly."

# Execute function
evaluate_performance(skill_levels, feedback_string)