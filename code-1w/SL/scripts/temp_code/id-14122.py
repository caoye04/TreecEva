def analyze_efficiency(metrics):
    if not metrics:
        return 0
    avg = sum(metrics) / len(metrics)
    adjusted_avg = avg * 0.9 if avg > 75 else avg * 1.1
    return round(adjusted_avg)

productivity = [80, 92, 78, 85, 90]
overhead_costs = [1500, 1600, 1480]  # Irrelevant data
baseline = 82

# Simulate risk assessment with red herring computations
risk_factor = 0
for val in productivity:
    if val < baseline:
        risk_factor += 1
risk_factor = max(risk_factor, 1)  # Ensure non-zero

# Distractor: unused helper function
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Distractor: dead computation path
useless_sum = 0
for i in range(len(overhead_costs)):
    useless_sum += overhead_costs[i] * 0.05  # Not connected to logic

# Conditional expression and slicing used here
recent_perf = productivity[-3:]  
efficiency_rating = analyze_efficiency(recent_perf) if len(productivity) >= 3 else analyze_efficiency(productivity)

# Core logic with set operation (tracking unique improvement events)
improvement_flags = [productivity[i] > productivity[i-1] for i in range(1, len(productivity))]
unique_improvements = len(set(improvement_flags))  # Set operation as required

# Final evaluation using multiple concepts
penalty = 5 if unique_improvements == 1 else 0
intermediate_score = efficiency_rating - penalty

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# But we define it now to make code valid
def evaluate_performance(performances, risk):
    base = sum(p for p in performances if p >= 80)
    adjustment = -10 if risk >= 2 else 0
    return base + adjustment + unique_improvements

print(f"Result: {final_score}")