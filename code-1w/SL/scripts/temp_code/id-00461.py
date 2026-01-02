def evaluate_performance(output, risk):
    base_score = 100
    adjustment = 0

    # Lambda for efficiency bonus
    efficiency_bonus = lambda out: out * 0.1 if out > 80 else out * 0.05

    # Set operations to simulate skill overlap
    core_skills = {'analysis', 'coding', 'design'}
    advanced_skills = {'automation', 'coding', 'optimization'}
    skill_overlap = len(core_skills & advanced_skills)

    # Simulated performance bands
    if output >= 90:
        adjustment += 20
    elif output >= 70:
        adjustment += 10
    else:
        adjustment -= 5

    # Risk penalty using dictionary mapping
    risk_map = {'low': 0.95, 'medium': 0.85, 'high': 0.65}
    risk_penalty = risk_map.get(risk, 0.75)

    # Dummy tracking variables (distractors)
    review_cycles = 3
    escalation_risk = review_cycles > 2 and risk == 'high'
    contingency_buffer = 10 if escalation_risk else 5

    # Irrelevant data structure manipulation
    stats_summary = {}
    stats_summary['output'] = output
    stats_summary['adjusted_output'] = output + adjustment
    stats_summary['penalized_output'] = stats_summary['adjusted_output'] * risk_penalty

    # Unused nested loop (dead code path - mild interference)
    temp_sum = 0
    for i in range(2):
        for j in range(3):
            temp_sum += i * j  # Not used later

    # Core calculation
    raw_score = base_score + efficiency_bonus(output) + adjustment
    final_score = int(raw_score * risk_penalty)

    return final_score

# Input values
productivity = 85
risk_factor = 'medium'

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)

# Output result
print(f"Result: {final_score}")