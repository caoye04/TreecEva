def calculate_final_score(scores, penalty):
    adjusted = [s ** 0.5 for s in scores]  # Apply square root transformation
    cutoff = 7.0
    filtered = [s for s in adjusted if s > cutoff]
    base_score = sum(filtered) / len(filtered) if filtered else 0
    
    # Irrelevant distraction: string processing (minimal interference)
    status_msg = "Processing complete"
    status_short = status_msg[:9].lower() + '...'
    
    # Conditional expression influencing final result
    final_score = base_score * (1 - penalty) if base_score > 8 else base_score * (1 - penalty / 2)
    return final_score

# Main execution
raw_scores = [64, 81, 100, 49, 36]
penalty_factor = 0.1
final_score = calculate_final_score(raw_scores, penalty_factor)
print(f"Result: {final_score}")