def evaluate_performance(feedback):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_count = 0
    temp_result = 0
    
    # Irrelevant string transformation (distractor)
    processed_feedback = [f.strip().lower() for f in feedback if len(f) > 0]
    feedback_text = ' '.join(processed_feedback)
    word_count = len(feedback_text.split())
    
    # Misleading statistical computation (dead path)
    avg_length = sum(len(f) for f in processed_feedback) / len(processed_feedback) if processed_feedback else 0
    long_entries = [f for f in processed_feedback if len(f) > avg_length]
    
    # Real logic begins: count positive vs negative keywords
    pos_keywords = ['excellent', 'great', 'good', 'outstanding', 'impressive']
    neg_keywords = ['poor', 'bad', 'terrible', 'lacking', 'weak']
    
    pos_matches = 0
    neg_matches = 0
    for entry in processed_feedback:
        words = entry.split()
        for word in words:
            cleaned_word = word.strip('.,!?"')
            if cleaned_word in pos_keywords:
                pos_matches += 1
            elif cleaned_word in neg_keywords:
                neg_matches += 1
    
    # Core scoring logic (depends on keyword balance)
    base_score = pos_matches * 10 - neg_matches * 15
    
    # Conditional bonus based on feedback diversity (string uniqueness)
    unique_words = set(feedback_text.split())
    diversity_ratio = len(unique_words) / word_count if word_count > 0 else 0
    if diversity_ratio > 0.7:
        bonus_multiplier += 0.3
    elif diversity_ratio > 0.5:
        bonus_multiplier += 0.1
    
    # Unrelated list processing (distractor)
    char_frequencies = {}
    for c in feedback_text:
        if c.isalpha():
            char_frequencies[c] = char_frequencies.get(c, 0) + 1
    top_chars = sorted(char_frequencies.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Apply multiplier only if no severe penalties
    if neg_matches < 3:
        temp_result = base_score * bonus_multiplier
    else:
        temp_result = base_score * 0.5  # harsh penalty
    
    # Final adjustment based on length of feedback (semi-relevant)
    length_bonus = len(feedback) * 2 if len(feedback) >= 4 else 0
    final_score = int(temp_result + length_bonus)

    # Irrelevant formatting operation
    report_lines = [f"Entry {i+1}: {f}" for i, f in enumerate(feedback)]
    summary = f"Performance Report:\nScores: {final_score}\nEntries: {len(feedback)}"

    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_list = [
    "  Great effort shown in the analysis  ",
    "Impressive attention to detail",
    "Good structure and flow",
    "excellent use of examples",
    "some parts were weak in reasoning",
    "poor time management observed"
]

# Execution point
final_score = evaluate_performance(feedback_list)