from itertools import combinations

# Simulate employee performance metrics across departments
def calculate_efficiency(base, hours, errors):
    return (base * hours) / (errors + 1)

productivity = [85, 90, 78, 92, 88]
risk_factor = [0.8, 1.1, 0.9, 1.3, 1.0]
bonus_pool = 5000
allocation = {}

# Irrelevant intermediate calculations (distractors)
temp_scores = [p * 1.05 for p in productivity if p > 80]
adjusted_risk = [min(r, 1.2) for r in risk_factor]
dummy_pairs = list(combinations(temp_scores[:3], 2))

# State tracking with unused counters
update_count = 0
sync_flag = False
for i in range(len(productivity)):
    if i % 2 == 0:
        update_count += 1
        sync_flag = not sync_flag

# Core logic hidden among side computations
raw_metrics = []
for idx, (p, r) in enumerate(zip(productivity, risk_factor)):
    efficiency = calculate_efficiency(p, 8, idx + 1)
    adjusted_p = p * (1 - (r - 0.8) * 0.25)  # Performance penalty based on risk
    raw_metrics.append(efficiency * 0.6 + adjusted_p * 0.4)

# Additional distraction: simulate budget reallocation
remaining_budget = bonus_pool
for share in [0.2, 0.25, 0.15, 0.3, 0.1]:
    amount = bonus_pool * share
    remaining_budget -= amount
    allocation[f'dept_{share*100:.0f}'] = amount

# Misleading normalization step (not used in final result)
normalized_metrics = [m / sum(raw_metrics) * 100 for m in raw_metrics]

# Key computation embedded late
aggregated = sum(raw_metrics) / len(raw_metrics)
volatility = sum(abs(raw_metrics[i] - raw_metrics[i+1]) for i in range(len(raw_metrics)-1))

# Final evaluation using core accumulated values
def evaluate_performance(metrics, risks):
    base_perf = sum(metrics)
    risk_penalty = sum(r > 1.0 for r in risks) * 3.5
    return base_perf - risk_penalty

final_score = evaluate_performance(raw_metrics, risk_factor)
print(f"Target result: {final_score}")