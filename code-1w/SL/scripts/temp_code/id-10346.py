def calculate_performance(base, delta, limit):
    adjustment = 0
    penalty = 0
    
    # Irrelevant computation - distractor
    temp_factor = (base * 0.1 + delta ** 2) % 7
    
    if delta > limit:
        adjustment = base * 0.25
        # Early distraction: complex-looking but unused logic
        secondary_adjust = (delta // limit) * 10 if limit != 0 else 0
        penalty = 15
    elif delta < -limit:
        adjustment = -base * 0.15
        # Dead code path with misleading calculation
        shadow_penalty = abs(delta) * 1.5
        penalty = 20
    else:
        adjustment = base * 0.05
        penalty = 5
        # Unused conditional expression
        fallback = 100 if base > 50 else 200

    # Semi-relevant transformation
    risk_factor = 1.2 if delta >= 0 else 0.8
    adjusted_base = base + adjustment
    
    # Core logic buried among distractions
    performance_index = (adjusted_base - penalty) * risk_factor
    
    # Conditional expression used meaningfully (required Python feature)
    final_tier = 'high' if performance_index > 80 else 'low'
    
    # Final score computed from relevant state only
    final_score = int(performance_index) if final_tier == 'high' else int(performance_index * 0.9)
    
    return final_score

# Initialization with meaningful names
baseline = 68
deviation = 9
threshold = 7

# Simulate intermediate tracking (distractor)
current_state = 'monitoring'
state_code = 2 if current_state == 'active' else 0

# Key execution point
final_score = calculate_performance(baseline, deviation, threshold)

# Output result as required
print(f"Result: {final_score}")