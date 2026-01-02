def analyze_efficiency(metrics):
    efficiency_list = [x * 2 for x in metrics if x > 5]
    adjusted = sum(efficiency_list) // len(efficiency_list) if efficiency_list else 0
    return adjusted * 3

productivity = [4, 7, 9, 3, 8, 6]
overhead_cost = [x ** 2 for x in productivity if x < 5]
baseline = sum(overhead_cost)

# Simulate risk exposure using set operations
detected_risks = {1, 3, 4, 7, 9, 10}
known_issues = {2, 3, 5, 7, 8}
minor_flags = {1, 2, 3}
risk_set = detected_risks - known_issues  # Only unmitigated risks
risk_set = risk_set.union(minor_flags.intersection(detected_risks))

# Dummy calculation to increase cognitive load
shadow_metric = len([x for x in productivity if x % 2 == 0]) * 7
buffer_zone = (len(detected_risks) + len(known_issues)) // 2

# Core logic disguised among other operations
def evaluate_performance(data, risk_profile):
    base = sum(x for x in data if x >= 6)
    penalty = len(risk_profile) * 2
    bonus = 5 if len(data) > 4 else 0
    intermediate = base - penalty + bonus
    
    # Additional distraction: unused conditional branch
    if sum(data) > 30:
        intermediate += 3  # This does not actually affect final result due to override below
    
    adjustment_factor = 1
    if len(risk_profile) < 4:
        adjustment_factor = 2
    
    intermediate = base - penalty + bonus  # Override prior modification; previous if-block was misleading
    
    return intermediate * adjustment_factor

# Secondary distraction: function call with no side effects
temp_result = analyze_efficiency(productivity)

# Key statement
final_score = evaluate_performance(productivity, risk_set)

print(f"Result: {final_score}")