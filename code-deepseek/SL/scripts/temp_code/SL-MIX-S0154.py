import itertools

def compute_quality_metric(measurements):
    # Distractor: misleading intermediate calculation
    temp_sum = sum(measurements) * 2  # Irrelevant multiplication
    
    # Main logic: find unique pairs and compute average difference
    unique_pairs = list(itertools.combinations(set(measurements), 2))
    
    # Distractor: dead code path
    if len(unique_pairs) > 10:
        redundant_check = min(measurements) // 2  # Never executed
    
    # Core calculation: average absolute difference
    differences = [abs(pair[0] - pair[1]) for pair in unique_pairs]
    
    # Distractor: misleading variable
    max_diff = max(differences) + 5  # Irrelevant offset
    
    # Final computation with modular arithmetic
    base_score = sum(differences) // len(differences) if differences else 0
    quality_modifier = base_score % 7
    
    # Distractor: unused operation
    potential_bonus = (quality_modifier * 3) - 2
    
    return base_score + quality_modifier

# Main execution with distracting variables
data_points = [15, 22, 8, 22, 31, 15, 8]

# Distractor: misleading intermediate variable
preliminary_analysis = len(data_points) * 4

# Distractor: unused set operation
all_unique = set(data_points)
redundant_max = max(all_unique) if all_unique else 0

# Key computation
final_score = compute_quality_metric(data_points)

# Distractor: post-processing that doesn't affect final_score
final_check = final_score * 1.5

print(f"Result: {final_score}")