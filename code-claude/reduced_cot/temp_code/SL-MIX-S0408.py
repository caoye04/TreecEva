import itertools

# Analyzing student exam performance across multiple subjects
def calculate_statistics(scores):
    mean_score = sum(scores) / len(scores)
    variance = sum((x - mean_score) ** 2 for x in scores) / len(scores)
    return mean_score, variance

# Student exam scores for 5 subjects
math_scores = [85, 92, 78, 90, 88]
science_scores = [79, 94, 81, 87, 90]

# Weights for potential scoring systems (not used in final calculation)
weighting_schemes = [(0.3, 0.7), (0.4, 0.6), (0.5, 0.5), (0.6, 0.4)]

# Generate all possible combinations of subjects
all_subject_combinations = list(itertools.combinations(range(5), 3))

# Track the best subjects to keep
best_combination = None
best_variance = float('inf')
optimal_mean = 0

# Process each possible combination of 3 subjects
for combo in all_subject_combinations:
    # Extract scores for this combination
    math_subset = [math_scores[i] for i in combo]
    science_subset = [science_scores[i] for i in combo]
    
    # Calculate statistics
    math_mean, math_var = calculate_statistics(math_subset)
    science_mean, science_var = calculate_statistics(science_subset)
    
    # Find average variance as our metric
    avg_variance = (math_var + science_var) / 2
    
    # Check if this is better than our current best
    if avg_variance < best_variance:
        best_variance = avg_variance
        best_combination = combo
        optimal_mean = (math_mean + science_mean) / 2

# Extract the optimal scores to keep
scores_to_keep = [math_scores[i] + science_scores[i] for i in best_combination]

# Calculate the final optimal score
optimal_score = sum(scores_to_keep)

# Some additional calculations that don't affect the result
max_possible = sum(sorted(math_scores)[-3:]) + sum(sorted(science_scores)[-3:])
min_possible = sum(sorted(math_scores)[:3]) + sum(sorted(science_scores)[:3])
range_width = max_possible - min_possible

print(f"Result: {optimal_score}")