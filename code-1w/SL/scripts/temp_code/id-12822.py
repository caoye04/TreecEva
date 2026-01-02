def apply_bonus_scores():
    base_scores = [85, 90, 78, 92, 88]
    adjustments = [1.05, 0.98, 1.03, 1.00, 1.02]
    
    # Calculate weighted scores using list comprehension and zip
    weighted_scores = [int(score * adj) for score, adj in zip(base_scores, adjustments)]
    
    # Apply extra credit for scores above 89
    extra_credit = 5
    final_scores = []
    for s in weighted_scores:
        if s > 89:
            s += extra_credit
        final_scores.append(s)
    
    # Irrelevant tracking variable (minor distraction)
    processed_count = len(final_scores)
    
    total_score = sum(final_scores)
    return total_score

result = apply_bonus_scores()
print(f"Result: {result}")