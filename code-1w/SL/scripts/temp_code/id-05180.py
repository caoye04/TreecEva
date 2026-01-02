from collections import defaultdict

# Simulate employee task tracking with some irrelevant counters
task_log = defaultdict(int)
irrelevant_counter = 0

productivity = 0
risk_factor = 1.0
bonus_flag = False

# Simulated daily tasks completed by an employee
daily_tasks = [8, 5, 12, 7, 10]
errors = [1, 0, 3, 2, 1]

for i in range(len(daily_tasks)):
    task_log[f'day_{i+1}'] += daily_tasks[i]  # logging, not used later
    productivity += daily_tasks[i]
    
    if errors[i] > 0:
        risk_factor *= (1 + errors[i] * 0.05)
        irrelevant_counter += errors[i]  # red herring

    # Distraction: unrelated conditional computation
    temp_adjustment = 0
    if daily_tasks[i] > 6:
        temp_adjustment = (daily_tasks[i] - 6) * 0.1
        bonus_flag = True  # looks important but isn't used

# Another distraction: unused helper calculation
hypothetical_risk = sum(errors) / len(errors) if errors else 0
useless_sum = sum([x**2 for x in daily_tasks if x % 2 == 0])  # dead-end calc

# Core logic: performance score based on productivity and adjusted risk
base_score = productivity * 10
penalty = int(base_score * (risk_factor - 1))
final_score = base_score - penalty

# Conditional expression (Python idiom) - actually affects result
final_score = final_score + 50 if bonus_flag and productivity >= 40 else final_score

# Print result as required
print(f"Result: {final_score}")