from collections import defaultdict

# Simulate employee performance evaluation with distraction variables
def analyze_employee_data(data):
    stats = defaultdict(int)
    temp_result = 0
    intermediate_sum = 0
    phantom_counter = 0  # Distractor: not used in final logic

    for entry in data:
        hours = entry['hours_worked']
        errors = entry['errors']
        overtime = entry.get('overtime', 0)
        
        # Productivity score with diminishing returns
        if hours > 40:
            base_productivity = 40 + (hours - 40) * 0.5
        else:
            base_productivity = hours
        
        # Risk factor increases with errors and overtime
        risk_factor = errors * 2 + overtime // 2
        
        # Distraction computation: irrelevant efficiency metric
        theoretical_efficiency = (hours * 100) / (errors + 1) if hours > 0 else 0
        phantom_counter += theoretical_efficiency  # Dead-end accumulation

        # Track real metrics
        stats['total_productivity'] += base_productivity
        stats['total_risk'] += risk_factor
        intermediate_sum += base_productivity * (10 - min(risk_factor, 10))  # Semi-relevant

    return dict(stats), intermediate_sum

# Evaluate overall team performance
def evaluate_performance(prod, risk):
    adjustment = 0
    if prod > 100:
        if risk < 30:
            adjustment = 15
        elif risk < 50:
            adjustment = 5
        else:
            adjustment = -10
    else:
        adjustment = -5
    
    raw_score = prod - risk
    final_score = raw_score + adjustment
    
    # Extra layer: conditional scaling (not always triggered)
    scaling_factor = 1.1 if prod > 120 and risk < 40 else 1.0
    final_score = int(final_score * scaling_factor)
    
    return final_score

# Main execution
if __name__ == "__main__":
    team_data = [
        {'hours_worked': 45, 'errors': 3, 'overtime': 8},
        {'hours_worked': 38, 'errors': 1, 'overtime': 2},
        {'hours_worked': 42, 'errors': 5, 'overtime': 6},
        {'hours_worked': 48, 'errors': 2, 'overtime': 10},
        {'hours_worked': 35, 'errors': 4, 'overtime': 0}
    ]

    # Irrelevant preprocessing step
    processed_data = [d for d in team_data if d['hours_worked'] >= 35]
    filtered_count = len(processed_data)

    metrics, dummy_sum = analyze_employee_data(team_data)
    
    total_hours_estimate = sum(d['hours_worked'] for d in team_data) + 5  # Off-by-purpose distraction
    
    productivity = metrics['total_productivity']
    risk_factor = metrics['total_risk']
    
    # Key statement
    final_score = evaluate_performance(productivity, risk_factor)
    
    # Print result as required
    print(f"Result: {final_score}")