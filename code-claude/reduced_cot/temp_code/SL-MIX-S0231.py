# Function to process student exam scores
def process_scores():
    # Raw student scores from the exam (out of 100)
    raw_scores = [78, 95, 65, 83, 42, 56, 91, 72, 88, 60]
    
    # Minimum passing score threshold
    pass_threshold = 50
    
    # Extract scores above the threshold
    valid_scores = [score for score in raw_scores if score >= pass_threshold]
    
    # Calculate average of valid scores
    avg_score = sum(valid_scores) / len(valid_scores)
    
    # Find sum of only the even valid scores
    filtered_sum = sum(filter(lambda x: x % 2 == 0, valid_scores))
    
    # Create a dictionary mapping score ranges to count
    score_distribution = {
        '50-69': len([s for s in valid_scores if 50 <= s < 70]),
        '70-89': len([s for s in valid_scores if 70 <= s < 90]),
        '90-100': len([s for s in valid_scores if 90 <= s <= 100])
    }
    
    return {
        'average': round(avg_score, 2),
        'even_sum': filtered_sum,
        'distribution': score_distribution
    }

# Execute the processing function
results = process_scores()
print(f"Result: {results['even_sum']}")