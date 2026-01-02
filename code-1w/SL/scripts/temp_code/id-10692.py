def evaluate_performance(reviews):
    base_score = sum(reviews) / len(reviews)
    adjusted_base = round(base_score * 1.1) if base_score >= 7 else round(base_score * 0.9)
    
    # Irrelevant metric (minor distraction)
    review_count = len(reviews)
    avg_char = "Average review is solid" if base_score > 6 else "Needs improvement"
    
    high_performers = [r for r in reviews if r >= 9]
    bonus_factor = len(high_performers) > 2
    performance_bonus = 5 if bonus_factor else 2
    
    final_score = adjusted_base + performance_bonus
    return final_score

# Main execution
decision_reviews = [8, 7, 9, 6, 9, 8, 9]
result = evaluate_performance(decision_reviews)
print(f"Result: {result}")