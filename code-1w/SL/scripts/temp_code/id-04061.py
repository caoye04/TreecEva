from collections import defaultdict

def analyze_efficiency(metrics):
    efficiency = 0
    adjustments = defaultdict(int)
    for val in metrics:
        if val > 80:
            efficiency += 1.5
            adjustments['high'] += 1
        elif val > 50:
            efficiency += 0.8
            adjustments['medium'] += 1
        else:
            adjustments['low'] += 1
    noise = sum([adjustments[k]**2 for k in adjustments])  # Distractor computation
    return efficiency

def assess_stability(readings):
    stability = 100.0
    temp_correction = 0
    for r in readings:
        if r < 10 or r > 90:
            stability -= 5.2
            temp_correction += 1
    final_penalty = temp_correction * 0.3  # Unused distraction
    return stability

def evaluate_risk(exposure_levels):
    risk_counter = defaultdict(int)
    total_risk = 0
    for level in exposure_levels:
        if level > 75:
            risk_counter['critical'] += 1
        elif level > 50:
            risk_counter['elevated'] += 1
    # Complex but partially irrelevant aggregation
    for key, count in risk_counter.items():
        if key == 'critical':
            total_risk += count * 3
        elif key == 'elevated':
            total_risk += count * 1.5
    return total_risk

def evaluate_performance(output_log, risk_data):
    base_effort = analyze_efficiency(output_log)
    system_stability = assess_stability(output_log)
    risk_level = evaluate_risk(risk_data)
    
    # Core logic with some surrounding distractions
    scaling_factor = 1.0
    if base_effort > 10:
        scaling_factor *= 1.2
    elif system_stability < 70:
        scaling_factor *= 0.8

    preliminary_score = base_effort * (100 - risk_level)  # Key intermediate step
    adjustment_set = {1, 2, 3, 4}
    outlier_check = len(adjustment_set & {3, 4, 5})  # Semi-relevant set operation
    
    if outlier_check > 1:
        preliminary_score += 5
    
    # Final score calculation — actual answer determined here
    final_score = int(preliminary_score / 10)  # Deterministic integer result
    
    # Dead code path — adds interference
    if False:
        fallback = system_stability - risk_level
        final_score = fallback
    
    return final_score

# Input data
productivity = [85, 70, 90, 60, 95, 40, 88]
risk_profile = [60, 80, 40, 90, 70]

# Execution point of interest
final_score = evaluate_performance(productivity, risk_profile)
print(f"Result: {final_score}")