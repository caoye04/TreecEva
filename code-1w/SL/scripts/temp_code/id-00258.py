def evaluate_performance():
    base_scores = [85, 90, 78, 92, 88]
    adjustments = [3, -2, 5, -1, 0]
    
    # Calculate performance with adjustment
    performance = [base + adj for base, adj in zip(base_scores, adjustments)]
    
    # Apply threshold filter using slicing to exclude marginal performers
    filtered_performance = [score for score in performance if score >= 85]
    
    # Compute total score after filtering
    total_score = sum(filtered_performance)
    
    return total_score

result = evaluate_performance()
print(f"Result: {result}")