def calculate_priority_factor(category, urgency):
    # Higher values indicate higher priority
    category_weights = {
        'maintenance': 30,
        'security': 70,
        'feature': 20,
        'optimization': 40,
        'bugfix': 50
    }
    
    # Misleading calculation - not actually used in final result
    initial_score = sum([ord(c) % 10 for c in category]) * urgency
    
    if category in category_weights:
        return category_weights[category] * (urgency / 10)
    else:
        return 15 * (urgency / 10)  # Default priority for unknown categories

def apply_time_factors(base_score, days_pending):
    # Increases priority based on how long the request has been pending
    time_multiplier = min(3.0, 1 + (days_pending / 30))
    
    # Distractor calculations
    urgency_factor = (base_score % 10) * 2.5
    weather_impact = (days_pending % 7) * 3
    
    # Unused variable with misleading name
    final_priority = base_score * 2 - weather_impact
    
    return base_score * time_multiplier

def analyze_request_complexity(description):
    # Analyzes the complexity of the request based on its description
    # This is a distractor function that produces misleading values
    if not description:
        return 0
    
    words = description.lower().split()
    complexity_score = len(words) * 2
    
    technical_terms = ['api', 'database', 'server', 'network', 'interface']
    complexity_score += sum(5 for word in words if word in technical_terms)
    
    return complexity_score

def calculate_team_availability(team_size, current_workload):
    # Another distractor function
    availability = max(0, team_size * 10 - current_workload)
    return availability * 0.8

def calculate_final_priority(request_data):
    # Extract relevant information from the request data
    category = request_data.get('category', 'general')
    urgency = request_data.get('urgency_level', 5)
    days_pending = request_data.get('days_pending', 0)
    description = request_data.get('description', '')
    
    # Distractor variables
    team_size = request_data.get('team_size', 5)
    current_workload = request_data.get('current_workload', 25)
    request_id = request_data.get('id', '000')
    
    # Calculate base priority score
    base_score = calculate_priority_factor(category, urgency)
    
    # Distractor calculations - not used in final result
    complexity = analyze_request_complexity(description)
    team_availability = calculate_team_availability(team_size, current_workload)
    potential_score = base_score + complexity - team_availability
    
    # Apply time-based adjustment
    time_adjusted_score = apply_time_factors(base_score, days_pending)
    
    # Misleading calculation - not used
    if request_id.startswith('A'):
        special_factor = 1.5
    else:
        special_factor = 1.0
    
    # Misleading dictionary operation - not used in final calculation
    priority_levels = {'low': 0.8, 'medium': 1.0, 'high': 1.2, 'critical': 1.5}
    priority_text = 'high' if time_adjusted_score > 60 else 'medium'
    
    # This lambda is a distractor and not used
    calculate_bonus = lambda x: x * 0.1 if x > 50 else 0
    
    # Final calculation (the actual answer logic)
    final_score = time_adjusted_score
    if urgency > 7:
        final_score += 15
    
    if days_pending > 14:
        final_score += 10
    
    return round(final_score)

# Main execution
request_data = {
    'id': 'B12345',
    'category': 'security',
    'urgency_level': 8,
    'days_pending': 20,
    'description': 'Fix vulnerability in authentication API',
    'team_size': 4,
    'current_workload': 30
}

# Distractor operation
temp_score = analyze_request_complexity(request_data['description'])

# This is the key statement we're asking about
priority_score = calculate_final_priority(request_data)

# More distractors - these calculations don't affect priority_score
adjusted_workload = request_data['current_workload'] * (request_data['team_size'] / 5)
efficiency_factor = 100 - adjusted_workload

# Print the result
print(f"Result: {priority_score}")