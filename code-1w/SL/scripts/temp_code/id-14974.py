def evaluate_performance(output, risk):
    base_efficiency = 85
    adjustment = 0
    
    # Irrelevant computation: simulating environmental factors
    env_noise = [0.1 * i for i in range(10)]
    avg_noise = sum(env_noise) / len(env_noise)
    calibrated_noise = avg_noise * 1.5 if len(env_noise) > 5 else 0
    
    # Real logic begins: efficiency adjustment based on output
    if output > 90:
        adjustment += 12
    elif output > 75:
        adjustment += 6
    else:
        adjustment -= 5
    
    # Risk penalty calculation
    risk_level = 'high' if risk > 0.7 else 'moderate' if risk > 0.3 else 'low'
    penalty_map = {'high': -10, 'moderate': -3, 'low': 0}
    risk_penalty = penalty_map[risk_level]
    
    # Distractor: unused function call
    def calculate_stress_index(val):
        return val * 2.5 + 4
    
    stress = calculate_stress_index(output)  # Computed but not used
    
    # Intermediate score with noise (noise has no real effect due to constant offset)
    intermediate = base_efficiency + adjustment + calibrated_noise
    
    # Final nonlinear scaling
    if intermediate > 90:
        final_score = intermediate * 0.95
    else:
        final_score = intermediate + 2.5
    
    # Dead code branch: never executed under normal inputs
    if output < 0 or risk < 0:
        final_score = 0
    
    # Key statement
    final_score = evaluate_performance(productivity, risk_factor)

# Inputs
productivity = 88
risk_factor = 0.65

# Initialize final_score before function assigns it
final_score = 0

def evaluate_performance(output, risk):
    base_efficiency = 85
    adjustment = 0

    if output > 90:
        adjustment += 12
    elif output > 75:
        adjustment += 6
    else:
        adjustment -= 5

    risk_level = 'high' if risk > 0.7 else 'moderate' if risk > 0.3 else 'low'
    penalty_map = {'high': -10, 'moderate': -3, 'low': 0}
    risk_penalty = penalty_map[risk_level]

    intermediate = base_efficiency + adjustment + risk_penalty

    if intermediate > 90:
        final_score_local = intermediate * 0.95
    else:
        final_score_local = intermediate + 2.5

    return final_score_local

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")