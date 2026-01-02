def analyze_efficiency(logs):
    total_ops = sum(logs)
    avg_op_time = total_ops / len(logs) if logs else 0
    efficiency = (total_ops / (avg_op_time + 1)) if avg_op_time > 0 else 0
    return efficiency

logs_data = [3, 5, 7, 2, 8, 6, 4]
efficiency_metric = analyze_efficiency(logs_data)

productivity = 0
risk_factors = {1, 3, 5, 7, 9, 11}
dummy_set = {x ** 2 for x in range(5)}  # Irrelevant computation
shadow_risk = set()

for i in range(1, 10):
    if i % 2 == 1:
        shadow_risk.add(i * 2)  # Distractor: not used later
    productivity += (i * efficiency_metric) // max(i, 3)

# Simulate auxiliary processing with no impact
temp_results = []
for val in logs_data:
    temp_results.append(val ** 0.5)
smoothing_factor = sum(temp_results) / len(temp_results)

# Core logic disguised among side calculations
baseline = 100
adjustment = 0
if efficiency_metric > 15:
    adjustment = 10
elif efficiency_metric > 10:
    adjustment = 5
else:
    adjustment = 0

scaled_productivity = int(productivity + adjustment)

# Risk filtering using set operations
exposure_set = {x for x in risk_factors if x < scaled_productivity}
risk_set = risk_factors - exposure_set  # Only this matters

# Dummy branching with dead code
status_flag = ""
if len(risk_set) > 3:
    status_flag = "HIGH_RISK"
    buffer = [i for i in range(len(risk_set))]  # Unused
else:
    status_flag = "LOW_RISK"
    temp_cache = set()  # Dead code path element

final_score = 0

# Critical statement
final_score = evaluate_performance(productivity, risk_set)

# Helper function defined after use (adds cognitive load)
def evaluate_performance(prod, risks):
    base = prod // 10
    penalty = len(risks) * 2
    bonus = 5 if base > 20 else 0
    # Additional irrelevant operation
    _ = [x for x in risks if x % 2 == 0]  # Not used
    return base - penalty + bonus + 7

print(f"Result: {final_score}")