import itertools

# Simulated user feedback analysis system for a learning platform
def analyze_engagement(ratings):
    weighted_sum = 0
    total_weight = 0
    decay_factor = 0.9
    
    for i, rating in enumerate(ratings):
        weight = decay_factor ** i
        weighted_sum += rating * weight
        total_weight += weight
    
    return weighted_sum / total_weight if total_weight else 0

# Irrelevant helper - distractor function (dead code path)
def calculate_momentum(values):
    momentum = 1.0
    for v in values:
        momentum *= (1 + v / 10)  # Not used anywhere
    return momentum

# Core logic: map feedback to performance tiers
def classify_tier(score):
    if score >= 8:
        return 'Expert'
    elif score >= 6:
        return 'Proficient'
    elif score >= 4:
        return 'Developing'
    else:
        return 'Beginner'

# Unused but plausible transformation - red herring
transformation_matrix = [[1, -1], [0, 1]]

def transform_sequence(seq):
    # This function is defined but not used in critical path
    return [a - b for a, b in zip(seq[::2], seq[1::2])]

# Another decoy function with misleading name
def compute_robust_mean(data):
    sorted_data = sorted(data)
    trim_count = max(1, len(data) // 10)
    trimmed = sorted_data[trim_count:-trim_count] if len(sorted_data) > 2 else sorted_data
    return sum(trimmed) / len(trimmed) if trimmed else 0

# Main aggregation logic with multiple concepts
feedback_levels = [7, 8, 6, 9, 5, 7, 8, 6, 7, 5, 4, 8, 9]

def aggregate_performance(feedbacks):
    # Step 1: Smoothed engagement score using decayed average
    base_score = analyze_engagement(feedbacks)
    
    # Step 2: Count transitions between performance levels
    tier_sequence = [classify_tier(f) for f in feedbacks]
    improvement_count = 0
    
    prev_tier = tier_sequence[0]
    for current_tier in tier_sequence[1:]:
        if (prev_tier == 'Developing' and current_tier == 'Proficient') or\
           (prev_tier == 'Proficient' and current_tier == 'Expert'):
            improvement_count += 1
        prev_tier = current_tier
    
    # Step 3: Apply combinatorial bonus for improvement streaks
    streak_bonus = 0
    current_streak = 0
    for i in range(1, len(tier_sequence)):
        if tier_sequence[i] != tier_sequence[i-1]:
            current_streak += 1
            if current_streak >= 3:
                streak_bonus += 0.5
        else:
            current_streak = 0
    
    # Step 4: Adjust score with streak and improvement factors
    adjustment_factor = 1 + (improvement_count * 0.05) + streak_bonus * 0.1
    adjusted_score = base_score * adjustment_factor
    
    # Step 5: Apply nonlinear compression for high scores
    if adjusted_score > 8:
        adjusted_score = 8 + (adjusted_score - 8) ** 0.5
    
    # Step 6: Normalize using harmonic-like mean over sliding windows (distractor calculation)
    window_scores = []
    for i in range(len(feedbacks) - 2):
        w = feedbacks[i:i+3]
        harmonic = 3 / sum(1/(x + 1e-8) for x in w)  # Avoid division by zero
        window_scores.append(harmonic)
    
    # Step 7: Final integration - only base dynamics matter
    final_component = adjusted_score
    
    # Irrelevant list comprehension with side effect that does nothing
    _ = [f"User rated {x}" for x in feedbacks if x > 10]  # No such users
    
    # Critical assignment
    final_score = round(final_component * 100) / 100  # Precision to 2 decimals
    return final_score

# Dead code assignments - red herrings
baseline_metrics = { 'avg': sum(feedback_levels)/len(feedback_levels), 'peak': max(feedback_levels) }
projected_growths = list(itertools.accumulate([0.1, -0.05, 0.2, 0.15], lambda x, y: x*(1+y)))

# Unused enumeration example - distractor
enumerated_feedback = list(enumerate(feedback_levels, start=1))
decorrelated_pairs = list(zip(feedback_levels[::2], feedback_levels[1::2]))

# Key execution point
final_score = aggregate_performance(feedback_levels)
print(f"Target result: {final_score}")