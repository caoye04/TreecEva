def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) / len(adjusted) if adjusted else 0

# Simulate employee performance evaluation
base_scores = [7, 8, 6, 9, 5, 4]
bonus_weights = [0.5, 0.8, 0.3, 1.0, 0.1, 0.0]

# Irrelevant computation: team average (not used in final logic)
team_avg = sum(base_scores) / len(base_scores)
deviation = [abs(x - team_avg) for x in base_scores]

efficiency = analyze_efficiency(base_scores)
productivity = efficiency * 1.5

# Dummy risk calculation with red herring variables
potential_risks = [2, 4, 6, 8]
baseline_threat = sum([r ** 0.5 for r in potential_risks]) / 10
risk_factor = 0.2 if baseline_threat > 1.0 else 0.5

# Unused data structure - distractor
class PerformanceRecord:
    def __init__(self, score):
        self.score = score

records = [PerformanceRecord(s) for s in base_scores]

# Core logic hidden among distractions
def evaluate_performance(prod, risk):
    if prod > 8:
        return int(prod * (1 - risk))
    elif prod > 6:
        return int(prod * (1 - risk * 0.5))
    else:
        return int(prod * 0.9)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Additional irrelevant state tracking
status_flag = "OPTIMAL" if final_score > 10 else "MONITOR"
log_entry = f"Status: {status_flag}, Score: {final_score}"

print(f"Result: {final_score}")