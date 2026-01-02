def calculate_rating(engagements, feedback_list):
    base_score = len(engagements)
    adjustment = sum([len(f.strip()) for f in feedback_list if f.strip()])
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_data = [1, 2, 3]
    
    if base_score > 5:
        multiplier = 1.5
    else:
        multiplier = 1.2
    
    raw_score = (base_score * multiplier) + adjustment
    
    # Apply decay factor based on engagement quality
    quality_decay = 0.9 if 'low' in engagements else 1.0
    return int(raw_score * quality_decay)

# Simulate user engagement metrics
engagement = ['click', 'view', 'hover', 'scroll', 'click', 'low']
feedback = ['  Great!  ', 'Nice feature.', '', 'Works well']

final_score = calculate_rating(engagement, feedback)
print(f"Result: {final_score}")