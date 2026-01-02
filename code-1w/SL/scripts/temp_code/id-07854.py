def main():
    # Performance metrics for different tasks (normalized scores)
    performances = [0.85, 0.92, 0.78, 0.96, 0.88]
    
    # Weight assigned to each task based on importance
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Irrelevant distraction: unused baseline threshold
    threshold = 0.8
    
    # Lambda function to scale scores above threshold (not used in final calculation)
    boost = lambda x: x * 1.1 if x > threshold else x
    
    # Apply weighting using zip and enumerate for element-wise computation
    weighted_sum = 0.0
    for i, (score, weight) in enumerate(zip(performances, weights)):
        weighted_sum += score * weight
    
    # Another irrelevant variable (distractor)
    adjusted_performances = [boost(s) for s in performances]
    
    # Function to calculate total weighted score
    def calculate_total(scores, wts):
        return sum(s * w for s, w in zip(scores, wts))
    
    final_score = calculate_total(performances, weights)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()