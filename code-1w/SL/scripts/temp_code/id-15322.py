def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    for log in logs:
        entries = log.split(';')
        daily_hours = 0
        for entry in entries:
            if 'work' in entry:
                time_spent = int(entry.split(':')[1])
                daily_hours += time_spent
            elif 'idle' in entry:
                idle_count += 1
        total_hours += daily_hours
    return total_hours, idle_count

logs_data = [
    'work:2;work:3;idle:1;work:1',
    'work:4;idle:2;work:2',
    'work:1;work:1;work:1;idle:1'
]

hours_worked, interruptions = analyze_productivity(logs_data)

# Distractor variables
baseline_efficiency = 8.0
theoretical_max = baseline_efficiency * len(logs_data)
dummy_ratio = theoretical_max / (hours_worked + 1) if hours_worked != 7 else 0

# Real computation begins
contributions = []
for i in range(len(logs_data)):
    contribution = (hours_worked // 3) % (i + 1) if i > 0 else hours_worked // 4
    contributions.append(contribution)

adjustment_factor = sum([c**0.5 for c in contributions if c > 0])
penalty_factor = max(1, interruptions // 2)

# Auxiliary distractor function
compute_waste = lambda x: sum([i for i in x if i % 2 == 0])
wasted_effort = compute_waste(contributions)  # Not used later

scaling_constant = 3.14159
shadow_var = scaling_constant * adjustment_factor  # Unused

# Core logic disguised among distractions
def calculate_rating(contribs, penalty):
    base_rating = sum(contribs)
    adjusted = base_rating * adjustment_factor
    normalized = adjusted / (penalty + 1e-5)
    return int(normalized + 0.5)

final_score = calculate_rating(contributions, penalty_factor)
print(f"Target result: {final_score}")