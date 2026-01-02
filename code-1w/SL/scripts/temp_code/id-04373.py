from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_efficiency(base_rate, overtime_multiplier):
    return base_rate * overtime_multiplier ** 2

# Auxiliary function to compute risk-adjusted output
def adjust_for_risk(raw_output, incidents):
    penalty = sum([i * 0.1 for i in incidents])
    return raw_output * (0.95 - penalty)

# Main evaluation logic
def evaluate_performance(output_levels, risk_indicators):
    # Intermediate transformation using lambda and conditional expression
    normalized = list(map(lambda x: x / max(output_levels) if max(output_levels) != 0 else 0, output_levels))
    
    # Apply risk adjustment
    adjusted_outputs = []
    for i, val in enumerate(normalized):
        window = risk_indicators[max(0, i-1):i+2]
        adjusted_val = val * (0.9 - len(window) * 0.01)
        adjusted_outputs.append(adjusted_val)
    
    # Aggregate final score
    aggregate = sum(adjusted_outputs)
    
    # Distractor computation: analyze team diversity (not used in final score)
    roles = ['engineer', 'analyst', 'manager', 'designer']
    role_pairs = list(combinations(roles, 2))
    pair_count = len(role_pairs)  # Irrelevant metric
    
    # Secondary distractor: simulate workload distribution
    workload = 0
    for shift in range(3):
        for hour in range(8):
            if hour % 3 == 0:
                workload += 1
    
    # Final scaling based on efficiency heuristic
    efficiency_ratio = aggregate / (len(output_levels) or 1)
    final_score = int(efficiency_ratio * 1000)
    
    return final_score

# Input data
productivity = [85, 90, 78, 92, 88]
risk_factor = [0.1, 0.15, 0.1, 0.2, 0.12]

# Additional irrelevant variables
baseline_metrics = {"threshold": 0.75, "scaling": 1.2}
archive_data = [analyze_department_efficiency(50, 1.1) for _ in range(4)]

# Key execution point
temp_result = adjust_for_risk(sum(productivity), [1, 0, 1])
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")