from collections import defaultdict

# Simulate employee performance analytics with mixed logical and arithmetic reasoning
def analyze_employee_data(hours_worked, errors_made, projects_completed):
    base_efficiency = sum(hours_worked) / len(hours_worked) if hours_worked else 0
    error_rate = sum(errors_made) / sum(projects_completed) if sum(projects_completed) > 0 else 0.5

    # Distractor: irrelevant computation for average_projects
    avg_projects = sum(projects_completed) / len(projects_completed)
    temp_adj = avg_projects * 0.1  # Unused adjustment

    productivity = []
    for i, (hours, proj) in enumerate(zip(hours_worked, projects_completed)):
        efficiency = (proj * 100) / max(hours, 1)
        bonus = 1.2 if proj > 2 else 1.0
        adjusted_efficiency = efficiency * bonus
        productivity.append(adjusted_efficiency)

    total_productivity = sum(productivity)
    normalized_productivity = total_productivity / len(productivity) if productivity else 0

    # Logical and comparison operations with nesting
    risk_factor = 0
    for i, err in enumerate(errors_made):
        if err > 1:
            if i % 2 == 0:
                risk_factor += err * 1.5
            else:
                risk_factor += err * 0.8
        else:
            risk_factor += err * 0.5

    # Dead code path (never executed due to logic above)
    if len(errors_made) > 100:
        risk_factor = 0  # Impossible condition - red herring

    # Conditional expression (python idiom)
    risk_factor = risk_factor if risk_factor < 20 else 20

    return normalized_productivity, risk_factor


def evaluate_performance(productivity, risk_factor):
    # Complex scoring logic combining arithmetic and boolean logic
    performance_tier = 'A' if productivity >= 80 else ('B' if productivity >= 60 else 'C')
    penalty = 10 if risk_factor > 10 else (5 if risk_factor > 5 else 0)
    
    # Multiple assignment and distractor variables
    base_score, adjustment = 100, 0
    multiplier = 1.1 if performance_tier == 'A' and risk_factor <= 5 else 0.9
    
    # Intermediate irrelevant calculation
    hypothetical_max = base_score * multiplier * 1.05  # Not used
    
    raw_score = (base_score + adjustment) * multiplier - penalty
    final_score = int(raw_score)  # Final deterministic integer result
    
    # Additional distraction: unused dictionary tracking
    score_breakdown = defaultdict(int)
    score_breakdown['base'] = base_score
    score_breakdown['penalty'] = penalty
    score_breakdown['final'] = final_score
    
    return final_score

# Input data
hours_worked = [8, 7, 9, 6]
errors_made = [2, 1, 3, 0]
projects_completed = [3, 2, 4, 1]

# Main execution flow
temp_result = analyze_employee_data(hours_worked, errors_made, projects_completed)
productivity, risk_factor = temp_result

final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")