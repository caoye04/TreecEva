def evaluate_performance(output, risk):
    base = 100 if output >= 80 else 70
    adjustment = -10 if risk > 0.5 else 5
    
    # Distractor: efficiency metric not directly used in final score
    efficiency = (output / (risk + 1)) * 0.75
    bonus = 20 if output > 90 and risk <= 0.3 else 0
    
    # Semi-relevant intermediate: affects logic flow but indirectly
    stress_level = 'high' if risk > 0.6 else 'moderate' if risk > 0.3 else 'low'
    penalty = 15 if stress_level == 'high' else 0

    # Actual computation chain
    raw_score = base + adjustment + bonus - penalty
    
    # Conditional expression for scaling based on risk tolerance
    scaling_factor = 1.1 if risk <= 0.4 else 0.9
    scaled_score = raw_score * scaling_factor
    
    # List comprehension to simulate historical adjustment (only last value used)
    history = [base * (0.95 + i*0.05) for i in range(1, 4)]
    recency_boost = (history[-1] - base) if history[-1] > base else 0
    
    final_score = int(scaled_score + recency_boost)
    
    # Dead code path — never executed under current logic
    if output < 0:
        final_score += 100  # unreachable
    
    return final_score

# Simulated sensor readings
productivity = 85
risk_factor = 0.38

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")