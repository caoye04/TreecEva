def analyze_productivity(logs):
    base_efficiency = 1.0
    surge_multiplier = 1.2
    decay_rate = 0.95
    temp_buffer = []
    
    for day, hours in enumerate(logs):
        if hours > 8:
            overtime_bonus = (hours - 8) * 0.05
            base_efficiency += overtime_bonus
        elif hours < 6:
            deficit_penalty = (6 - hours) * 0.03
            base_efficiency -= deficit_penalty

        # Simulate fluctuating focus levels (distractor)
        focus_drift = (day % 4) * 0.01
        base_efficiency = min(max(base_efficiency, 0.7), 1.5)

    return base_efficiency


def calculate_rating(contribs, penalties):
    raw_total = sum(contribs)
    adjustment = 0
    
    for i, val in enumerate(contribs):
        if i % 2 == 0:
            adjustment += val * 0.1
        else:
            adjustment -= val * 0.05
    
    # Dummy tracking of penalty phases (semi-relevant)
    phase_tracker = []
    cumulative = 0
    for p in penalties:
        cumulative += p
        phase_tracker.append(cumulative)
    
    net_penalty = sum(penalties) * 0.2 if cumulative > 0 else 0

    intermediate_score = raw_total + adjustment - net_penalty
    
    # Final scaling with bounded output
    final_rating = max(intermediate_score * 1.1, 10)
    return int(final_rating)

# Main execution
activity_log = [7, 9, 5, 8, 6]
base_metric = analyze_productivity(activity_log)

contributions = [15, 20, 12, 18]
penalties = [3, 7, 0, 5]

# Irrelevant precomputation (distractor)
shadow_scores = []
for idx, (c, p) in enumerate(zip(contributions, penalties)):
    shadow_scores.append((c - p) * (idx + 1))

auxiliary_sum = sum([x for x in shadow_scores if x > 10])

scaling_factor = len(contributions) / 4.0  # Redundant but plausible

final_score = calculate_rating(contributions, penalties)

print(f"Result: {final_score}")