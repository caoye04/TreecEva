from collections import defaultdict

# Simulate employee performance evaluation with distraction metrics
productivity = [85, 90, 78, 92, 88]
absenteeism_days = [2, 1, 5, 0, 3]  # Distractor: not used in final logic
task_completion = {i: val >= 80 for i, val in enumerate(productivity)}

# Initialize tracking structures
performance_tally = defaultdict(int)
bonus_eligibility = []
penalty_flag = False

for i, score in enumerate(productivity):
    performance_tally[i] += score * 1.1
    if score < 80:
        performance_tally[i] -= 5
    else:
        bonus_eligibility.append(i)

# Secondary loop with misleading computation
risk_factor = 0
for days in absenteeism_days:
    if days > 4:
        risk_factor += 10
    elif days > 2:
        risk_factor += 5  # This path is taken but contributes little
    else:
        risk_factor += 1  # Most entries fall here, inflating risk_factor slightly

# Dead code path (never executed due to data)
dummy_tracker = []
for x in range(len(absenteeism_days)):
    if absenteeism_days[x] > 10:  # Impossible condition
        dummy_tracker.append(x)

# Conditional expression with actual relevance
base_risk = risk_factor if sum(productivity) > 400 else 0
adjusted_risk = base_risk * 0.8

# Core evaluation function with nested logic
def evaluate_performance(prod_scores, adjusted_risk):
    base_performance = sum(score for score in prod_scores if score >= 80)
    penalty_reduction = 0
    
    for score in prod_scores:
        if score < 75:
            penalty_reduction += 10
        elif score < 85:
            penalty_reduction += 5
    
    # Intermediate distractor calculation
    avg_absence = sum(absenteeism_days) / len(absenteeism_days)  # Computed but unused
    hypothetical_max = len(prod_scores) * 100
    efficiency_ratio = (sum(prod_scores) / hypothetical_max) * 100
    
    # Final formula incorporating adjusted risk as dampener
    raw_score = base_performance - penalty_reduction - adjusted_risk
    return int(raw_score + 0.5)  # Round to nearest integer

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")