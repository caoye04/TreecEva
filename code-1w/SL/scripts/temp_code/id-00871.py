def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    efficiency_list = []

    for idx, (hours, status) in enumerate(logs):
        if status == 'active':
            total_hours += hours
            efficiency = hours * (idx + 1)  # weight by session order
            efficiency_list.append(efficiency)
        else:
            idle_count += 1
            # Distractor: track idle but not used later
            placeholder = hours * 0.5

    adjusted_total = total_hours - idle_count * 0.5
    return adjusted_total, efficiency_list


def calculate_complexity(n):
    # Distractor function: looks important but unused
    if n <= 1:
        return 1
    return n * calculate_complexity(n - 2)


def calculate_rating(contributions, penalties):
    base_score = sum(contributions)
    penalty_deduction = 0
    
    for i, penalty in enumerate(penalties):
        if i % 2 == 0:
            penalty_deduction += penalty * 0.9
        else:
            penalty_deduction += penalty * 0.1
    
    # Real logic
    raw_score = base_score - penalty_deduction
    
    # Semi-relevant transformation
    multiplier = len(contributions) / (len(penalties) + 1)
    enhanced_score = raw_score * multiplier
    
    # Distractor: complex-looking but unused calculation
    shadow_score = 0
    for c, p in zip(contributions, penalties + [0] * abs(len(contributions) - len(penalties))):
        shadow_score += c ^ p  # bitwise XOR - irrelevant
    
    return int(enhanced_score)

# Main execution
logs_data = [(2, 'active'), (1, 'idle'), (3, 'active'), (0.5, 'idle'), (4, 'active')]
total_work, efficiencies = analyze_productivity(logs_data)

contributions = [10, 20, 15, 30]
penalties = [5, 10, 2]

intermediate_metric = 0
for e in efficiencies:
    intermediate_metric += e * 1.1  # Distractor accumulation

bonus_flag = True
if len(contributions) > len(penalties):
    bonus_flag = False  # Distractor condition

final_score = calculate_rating(contributions, penalties)
print(f"Result: {final_score}")