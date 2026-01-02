def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for day, hours in enumerate(logs):
        total_hours += hours
        if hours < 2:
            idle_periods += 1
    efficiency = total_hours / len(logs) if logs else 0
    return total_hours, efficiency, idle_periods

logs_data = [8, 5, 3, 7, 1, 6, 4]

# Extract analysis metrics
total_hrs, avg_efficiency, downtime = analyze_productivity(logs_data)

# Simulate task contribution weights
task_weights = [1.2, 0.8, 1.5, 1.0, 0.5]
weighted_contributions = []
for i, weight in enumerate(task_weights):
    contribution = weight * (total_hrs % 10)
    weighted_contributions.append(contribution)

# Auxiliary computation - not directly used
temp_analysis = []
for val in weighted_contributions:
    temp_analysis.append(val ** 2 + 3 * val - 1)

# Core data structures
base_set = {i for i in range(1, int(avg_efficiency) + 5)}
penalty_set = {x for x in base_set if x % 3 == 0}
bonus_tracker = dict(zip(range(len(weighted_contributions)), [w * 0.1 for w in weighted_contributions]))

contributions = sum(weighted_contributions) + len(bonus_tracker)

# Misleading intermediate calculation (dead-end)
external_factor = 0
for k, v in bonus_tracker.items():
    if k > 3:
        external_factor += v * 2

# Critical statement
final_score = calculate_rating(contributions, penalty_set)

# Dummy function to resolve final score
def calculate_rating(contribs, penalties):
    base_rating = contribs / (len(penalties) + 1)
    adjustment = 0
    for i, log_val in enumerate(logs_data):
        if log_val >= 5 and i in penalties:
            adjustment += 1.5
    return int(base_rating + adjustment)

# Print result
print(f"Result: {final_score}")