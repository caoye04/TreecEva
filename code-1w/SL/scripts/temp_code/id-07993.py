def evaluate_performance(output, risk):
    base_score = 100 if output > 80 else 70
    penalty = 0
    
    # Distractor: irrelevant calculation for maintenance cycles
    maintenance_cycles = (output * 2 + 17) % 13
    adjustment_factor = 0.9 if maintenance_cycles > 5 else 1.1
    
    # Real logic begins
    if risk == 'high':
        penalty += 30
    elif risk == 'medium':
        penalty += 15
    
    # Conditional expression used
    bonus = 10 if output > 90 and risk != 'high' else 5
    
    # Distractor: unused intermediate computation
    projected_growth = (output * adjustment_factor) + bonus - penalty
    volatility_index = (output - 85) ** 2 / (penalty + 1)
    
    # Core scoring logic
    raw_score = base_score - penalty + bonus
    
    # Another distractor: dead code path due to fixed condition
    if False:
        raw_score = int(raw_score * 0.8)
    
    return int(raw_score)

# Simulated sensor readings and assessments
productivity = (37 * 2 + 16)  # Yields 90
risk_assessment = ['medium', 'high', 'low'][1]

# Mapping for risk level
risk_level_map = {'low': 'low', 'med': 'medium', 'high': 'high'}
risk_factor = risk_level_map.get('med', 'low') if productivity < 85 else 'medium'

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result
print(f"Result: {final_score}")