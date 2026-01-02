def analyze_productivity(logs):
    total_hours = sum(logs)
    peak_day = max(logs)
    avg_daily = total_hours / len(logs) if logs else 0
    efficiency_ratio = (peak_day / total_hours) if total_hours > 0 else 0
    return avg_daily, efficiency_ratio

logs_data = [8, 5, 7, 9, 6]

# Irrelevant computation: simulate burnout risk (not used later)
burnout_risk = sum(1 for h in logs_data if h > 7) * 0.1
baseline_stress = 2.5
adjusted_stress = baseline_stress + burnout_risk

avg_prod, eff_ratio = analyze_productivity(logs_data)

contributions = [12, 15, 10, 18, 14]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Weighted contribution with distractor logic
weighted_total = sum(contributions[i] * weights[i] for i in range(len(contributions)))
bonus_award = 10 if weighted_total > 12 else 5

# Unused helper lambda (distractor)
calculate_bonus = lambda x, mult: x * mult if x > 10 else 0
unused_bonus = calculate_bonus(weighted_total, 0.2)

# Simulate penalty factor based on efficiency
penalty_factor = 0.9 if eff_ratio < 0.3 else 0.95

# Core logic hidden among distractions
def calculate_rating(contribs, penalty):
    raw_sum = sum(contribs)
    adjustment = raw_sum * 0.1
    adjusted_sum = raw_sum - adjustment
    normalized = adjusted_sum / len(contribs)
    multiplier = 1.2 if normalized > 12 else 1.1
    # Additional irrelevant check
    if normalized < 10:
        return 0
    return int((normalized * multiplier) * penalty)

interim_check = weighted_total * 0.5  # dead-end variable

final_score = calculate_rating(contributions, penalty_factor)
print(f"Result: {final_score}")