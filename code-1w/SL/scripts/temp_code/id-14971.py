def process_feedback(feedback_list):
    word_count = {}
    total_chars = 0
    positive_keywords = ['good', 'excellent', 'great', 'outstanding']
    negative_keywords = ['bad', 'poor', 'terrible', 'awful']
    
    for review in feedback_list:
        words = review.lower().split()
        total_chars += sum(len(word) for word in words)
        
        for word in words:
            cleaned = word.strip('.,!?"')
            word_count[cleaned] = word_count.get(cleaned, 0) + 1
    
    keyword_bonus = 0
    for word in word_count:
        if word in positive_keywords:
            keyword_bonus += word_count[word] * 2
        elif word in negative_keywords:
            keyword_bonus -= word_count[word]
    
    avg_length = total_chars / len([w for r in feedback_list for w in r.split()]) if total_chars > 0 else 0
    rounded_avg = round(avg_length, 2)
    
    base_score = len(word_count) * 3
    final_score = base_score + keyword_bonus + int(rounded_avg)
    
    temp_value = rounded_avg  # Irrelevant variable (distractor)
    extra_flag = False     # Unused flag (minor interference)
    
    return final_score

reviews = [
    "The service was excellent and the staff were great",
    "Poor quality overall, bad experience, really terrible",
    "Great food, outstanding taste, excellent value for money"
]

result = process_feedback(reviews)
print(f"Target result: {result}")