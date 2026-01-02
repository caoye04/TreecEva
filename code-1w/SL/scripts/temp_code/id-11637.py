def calculate_rank_score():
    # Simulate ranking of participants in a coding contest
    participants = ['Alice', 'Bob', 'Charlie', 'Diana']
    scores = [88, 92, 75, 85]
    ranks = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    
    # Assign weights based on rank position (higher rank -> higher weight)
    weights = [1.5, 1.2, 1.0, 0.8]
    
    # Irrelevant distraction: unused variable
    max_possible_score = max(scores)
    
    # Compute weighted ranks using list comprehension and enumerate
    weighted_ranks = [weights[rank] * scores[i] for i, rank in enumerate(ranks)]
    
    # Final aggregation
    total_score = sum(weighted_ranks)
    
    # Print result as required
    print(f"Result: {total_score}")
    
    return total_score

# Execute function
calculate_rank_score()