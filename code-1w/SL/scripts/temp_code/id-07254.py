from itertools import combinations

# Simulate employee productivity metrics across departments
def analyze_work_patterns(hours_logged, error_rate):
    base_efficiency = sum(h ** 0.8 for h in hours_logged)
    penalty = error_rate * 100
    adjusted_efficiency = max(base_efficiency - penalty, 0)
    
    # Irrelevant distraction: unused complexity
    peak_window = [i for i, h in enumerate(hours_logged) if h > 8]
    fragmentation_index = len(peak_window) / len(hours_logged) if hours_logged else 0
    
    return adjusted_efficiency

# Risk assessment using logical thresholds
def assess_stress_level(breaks_taken, workload):
    stress_factor = 0
    if breaks_taken < 3:
        stress_factor += 40
    if workload > 6:
        stress_factor += 35
    
    # Dead code path (never executed due to logic)
    if stress_factor > 100:
        stress_factor = 100
    
    return stress_factor / 100.0

# Core evaluation logic
def evaluate_performance(output_volume, risk):
    normalized_output = output_volume * (1 - risk)
    bonus_eligibility = normalized_output > 150
    
    # Misleading intermediate calculation (not used)
    hypothetical_max = output_volume * (1 + risk)
    decay_adjusted = hypothetical_max * 0.95
    
    # Actual scoring formula
    base_score = normalized_output * 0.8
    incentive = 25 if bonus_eligibility else 10
    final_value = base_score + incentive
    
    return int(final_value)

# Main simulation
hours_data = [7, 9, 6, 10, 8, 7, 9]
error_rate = 0.07
workload_intensity = 7
break_count = 2

# Compute derived metrics
productivity = analyze_work_patterns(hours_data, error_rate)
risk_raw = assess_stress_level(break_count, workload_intensity)

# Auxiliary distraction: unused combinatorial analysis
possible_shift_pairs = list(combinations(hours_data, 2))
high_hour_pairs = list(filter(lambda x: (x[0] + x[1]) > 15, possible_shift_pairs))
dummy_aggregate = sum(map(lambda x: x[0] * 0.1 + x[1] * 0.05, high_hour_pairs))

# Key state variables
risk_factor = max(risk_raw, 0.2)  # Enforce minimum risk floor

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Output result as required
print(f"Result: {final_score}")