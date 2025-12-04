import itertools

def calculate_weighted_score(entries):
    # Apply weighting factors based on position
    weights = [0.8, 1.2, 0.9, 1.5, 1.0]
    
    # These factors don't affect the final result
    adjustment_factors = {'easy': 1.1, 'medium': 1.0, 'hard': 0.9}
    
    weighted_sum = 0
    valid_count = 0
    
    for idx, entry in enumerate(entries):
        # Only process valid entries (positive values)
        if entry > 0:
            # Apply position-based weighting
            weight = weights[idx % len(weights)]
            weighted_sum += entry * weight
            valid_count += 1
    
    # Calculate average if there are valid entries
    return weighted_sum / valid_count if valid_count > 0 else 0

# Student performance data
raw_scores = [15, 22, 0, 18, 24, 13, 0, 19]
complexity_levels = ['medium', 'hard', 'easy', 'medium', 'hard', 'easy', 'medium', 'hard']

# Process only attempts with non-zero scores
valid_attempts = [score for score in raw_scores if score > 0]

# Generate some distractor data
distractor_pairs = list(zip(raw_scores, complexity_levels))
filtered_distractors = [pair for pair in distractor_pairs if pair[0] > 10 and pair[1] != 'easy']

# This is not used in the final calculation
distractor_avg = sum([p[0] for p in filtered_distractors]) / len(filtered_distractors) if filtered_distractors else 0

# More distractor operations
attempt_indices = list(enumerate(raw_scores))
valid_indices = [idx for idx, score in attempt_indices if score > 0]

# Create entries for processing - only non-zero scores
valid_entries = [score for score in raw_scores if score > 0]

# Calculate final weighted score
final_score = calculate_weighted_score(valid_entries)
print(f"Result: {final_score}")