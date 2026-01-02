def evaluate_performance(raw_score, threshold=50):
    base_score = raw_score * 1.8
    adjustment_factor = 0.9 if raw_score >= threshold else 1.1
    adjusted_base = int(base_score * adjustment_factor)
    
    # Performance tier determination
    excellent = raw_score >= 85
    good = 70 <= raw_score < 85
    passed = raw_score >= threshold
    
    # Curve bonus logic based on class performance
    curve_bonus = 7 if excellent else (3 if good else 0)
    
    final_score = adjusted_base + curve_bonus if passed else base_score // 2
    
    # Irrelevant tracking variable (minimal distraction)
    status_label = "Passed" if passed else "Failed"
    
    return final_score

result = evaluate_performance(76)
print(f"Result: {result}")