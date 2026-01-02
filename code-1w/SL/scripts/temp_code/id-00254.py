def apply_corrections():
    base_scores = [85, 90, 78, 92, 88]
    adjustments = [2, -3, 5, 0, -1]
    total_score = 0
    
    for idx, (score, adj) in enumerate(zip(base_scores, adjustments)):
        corrected = score + adj
        if corrected >= 90:
            total_score += corrected // 10
    
    return total_score

result = apply_corrections()
print(f"Result: {result}")