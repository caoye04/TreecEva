from collections import Counter

# Student submission scoring system
def calculate_stats(submissions):
    # Track valid and invalid submissions
    valid_submissions = 0
    invalid_count = 0
    total_score = 0
    
    # Process each submission
    for idx, submission in enumerate(submissions):
        # Skip processing for invalid submissions
        if submission < 0 or submission > 100:
            invalid_count += 1
            continue
        
        # Apply bonus for early submissions (first 3)
        bonus = 5 if idx < 3 else 0
        
        # Calculate adjusted score with bonus
        adjusted_score = min(100, submission + bonus)
        
        # Track statistics
        total_score += adjusted_score
        valid_submissions += 1
    
    # Calculate distribution of scores
    score_distribution = Counter([s for s in submissions if 0 <= s <= 100])
    most_common_score, frequency = score_distribution.most_common(1)[0] if score_distribution else (0, 0)
    
    # Calculate penalty factor based on invalid submissions
    penalty_factor = 0.95 ** invalid_count
    
    # Determine weight factor based on submission frequency
    if frequency >= 3:
        weight_factor = 1.1  # Bonus for consistency
    else:
        weight_factor = 0.9  # Penalty for inconsistency
    
    # These variables aren't used in the final calculation
    average_raw = sum(s for s in submissions if 0 <= s <= 100) / valid_submissions if valid_submissions > 0 else 0
    median_value = sorted([s for s in submissions if 0 <= s <= 100])[valid_submissions//2] if valid_submissions > 0 else 0
    
    # Calculate effective score (the answer we're looking for)
    if valid_submissions > 0:
        effective_score = round(((total_score / valid_submissions) * weight_factor), 2)
    else:
        effective_score = 0
        
    return effective_score, penalty_factor, most_common_score

# Test data
submissions = [85, 72, 90, -5, 68, 95, 110, 90, 90]

# Calculate and display results
effective_score, penalty, most_common = calculate_stats(submissions)
print(f"Result: {effective_score}")