from collections import defaultdict

# Simulate user engagement metrics across platform features
engagement_data = {
    'clicks': 145,
    'dwell_time_seconds': 320,
    'scroll_depth_percent': 78,
    'interactions': 12
}

# Weight mapping for scoring different engagement types
weights = defaultdict(float, {
    'clicks': 0.2,
    'dwell_time_seconds': 0.015,
    'scroll_depth_percent': 0.1,
    'interactions': 0.3
})

# Irrelevant auxiliary variable (minimal distraction)
temp_scaling = 1.0  # unused in final calculation

# Scoring logic using lambda for dynamic contribution calculation
compute_contribution = lambda value, weight: round(value * weight, 3)

def calculate_final_score(engagement, w):
    base_score = 0.0
    for key, value in engagement.items():
        if key in w:
            base_score += compute_contribution(value, w[key])
    
    # Apply bitwise adjustment based on even/odd status of total interactions
    total_interactions = engagement['interactions']
    if total_interactions & 1:  # odd?
        base_score ^= 5.5  # XOR flip on score if odd interactions
    else:
        base_score += 2.25
    
    return round(base_score, 3)

# Final computation
threshold_score = calculate_final_score(engagement_data, weights)

# Output result
print(f"Target result: {threshold_score}")