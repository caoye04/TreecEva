def evaluate_performance(output, risk):
    efficiency = output / (risk + 1)
    bonus = 10 if efficiency > 5 else 0
    penalty = 5 if 'low' in str(risk).lower() else 0
    return int(efficiency + bonus - penalty)

# Simulated employee performance metrics
team_data = [{'name': 'Alice', 'tasks': 45, 'errors': 3}, {'name': 'Bob', 'tasks': 30, 'errors': 1}, {'name': 'Charlie', 'tasks': 50, 'errors': 8}]

# Irrelevant aggregation (distractor)
total_tasks = sum(emp['tasks'] for emp in team_data)
error_rates = {emp['name']: emp['errors']/emp['tasks'] for emp in team_data}

# Focus on Alice's productivity
productivity = team_data[0]['tasks'] - team_data[0]['errors']

# Secondary metric with misleading path
performance_flags = set()
if team_data[0]['errors'] < 5:
    performance_flags.add('high_quality')
if team_data[0]['tasks'] > 40:
    performance_flags.add('high_volume')

# Dummy risk calculation path (partially irrelevant)
base_risk = len(performance_flags) * 2
adjustment_factor = 1.5 if 'high_volume' in performance_flags else 0.8
adjusted_risk = base_risk * adjustment_factor

# Unused intermediate calculations (dead code red herring)
scaled_output = productivity * adjustment_factor
theoretical_max = 50 * 1.2
utilization_ratio = scaled_output / theoretical_max if theoretical_max else 0

# Core logic step
risk_factor = adjusted_risk if adjusted_risk > 0 else 1

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")