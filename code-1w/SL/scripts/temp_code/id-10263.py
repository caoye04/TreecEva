def evaluate_performance():
    raw_scores = [85, 90, 78, 92, 88]
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    
    # Normalize scores to a 0-10 scale
    normalized_scores = [score / 10 for score in raw_scores]
    
    # Apply difficulty adjustment using simple function
    adjusted_ratings = [round(ns - 0.5, 1) for ns in normalized_scores]
    
    # Determine which candidates passed threshold
    passing_indices = [i for i, ar in enumerate(adjusted_ratings) if ar >= 8.0]
    passing_names = [names[i] for i in passing_indices]
    
    # Irrelevant distraction: unused list operation
    reversed_names = [name[::-1] for name in names]
    
    # Core computation
    final_score = max(adjusted_ratings) * len(passing_names)
    
    # Print result as required
    print(f"Result: {final_score}")

evaluate_performance()