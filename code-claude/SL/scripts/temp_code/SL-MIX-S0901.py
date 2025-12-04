def calculate_optimal(weights):
    # Calculate optimal weight using the filtered values
    if not weights:
        return 0
    return sum(weights) / len(weights)

# Athlete performance tracking system
athletes = [
    ('Kim', 72.5, 8.7),   # (name, weight, performance_score)
    ('Alex', 81.2, 7.9),
    ('Jamie', 68.0, 9.2),
    ('Taylor', 75.8, 8.1),
    ('Morgan', 79.4, 8.5)
]

# Performance threshold (used for filtering)
min_score = 8.0
max_score = 9.5

# Track additional statistics (not directly used in final result)
total_participants = len(athletes)
average_score = sum(athlete[2] for athlete in athletes) / total_participants

# Filter athletes based on performance score
qualified_athletes = []
for idx, athlete in enumerate(athletes):
    name, weight, score = athlete
    if min_score <= score <= max_score:
        qualified_athletes.append((idx, name, weight, score))
    # Track disqualified athletes (not used for final calculation)
    else:
        disqualification_reason = "score too low" if score < min_score else "score too high"

# Process qualified athletes
all_weights = []
all_scores = []

# Use enumerate and zip for processing
for i, (idx, name, weight, score) in enumerate(qualified_athletes):
    performance_factor = score / 10.0
    adjusted_weight = weight * performance_factor
    all_weights.append(adjusted_weight)
    all_scores.append(score)
    
    # Calculate some statistics (not used directly in final answer)
    weight_difference = adjusted_weight - weight
    percentage_change = (weight_difference / weight) * 100

# Calculate some additional metrics (not directly used in final result)
try:
    max_score_achieved = max(all_scores)
    min_weight_adjusted = min(all_weights) if all_weights else 0
except ValueError:
    max_score_achieved = 0
    min_weight_adjusted = 0

# Apply a secondary filter to get more accurate results
weight_threshold = 65.0
filtered_weights = [w for w in all_weights if w > weight_threshold]

# Some additional computations that don't affect the final result
potential_weights = [(w + 2.5) for w in filtered_weights]
potential_average = sum(potential_weights) / len(potential_weights) if potential_weights else 0

# Calculate the optimal weight from filtered values
optimal_weight = calculate_optimal(filtered_weights)

print(f"Result: {optimal_weight}")