def evaluate_performance(efficiency, risk):
    base_multiplier = 1.5
    adjustment_factor = 0.8 if efficiency > 75 else 1.1
    penalty = 10 if risk > 50 else 0
    
    # Irrelevant intermediate calculation (distractor)
    hypothetical_gain = (efficiency * adjustment_factor) - penalty
    decay_rate = 0.95
    projected = hypothetical_gain * decay_rate  # Not used later

    # Core logic
    raw_score = efficiency * base_multiplier
    if risk < 30:
        raw_score += 20
    elif risk < 70:
        raw_score += 5
    else:
        raw_score -= 15

    # Another red herring: complex unused lambda
    analyze_trend = lambda x, y: (x ** 1.1) / (y + 1) if y != 0 else x
    trend_value = analyze_trend(efficiency, risk)  # Computed but not used

    return int(raw_score)

# Simulated input data
productivity = 88
risk_factor = 42

# Dead code path (misleading control flow)
if productivity < 0:
    productivity = 0
    backup_mode = True
    fallback_score = 50

# Key computation
final_score = evaluate_performance(productivity, risk_factor)

# Sorting a list that's not used (distractor)
recent_metrics = [78, 92, 88, 76, 95]
sorted_metrics = sorted(recent_metrics, reverse=True)
ranked = [x * 0.9 for x in sorted_metrics]  # Unused

# Simple combinatorics: number of pairs (not directly related)
n_employees = 5
potential_pairs = n_employees * (n_employees - 1) // 2  # Distractor

print(f"Result: {final_score}")