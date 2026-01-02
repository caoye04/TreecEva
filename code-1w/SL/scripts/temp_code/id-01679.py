from collections import defaultdict

# Simulated employee performance data across quarters
employee_data = [
    {'name': 'Alice', 'dept': 'Engineering', 'ratings': [4.2, 4.5, 4.0, 4.8], 'attendance': 97},
    {'name': 'Bob', 'dept': 'Sales', 'ratings': [3.8, 4.1, 4.3, 4.0], 'attendance': 94},
    {'name': 'Charlie', 'dept': 'Engineering', 'ratings': [4.9, 4.7, 5.0, 4.6], 'attendance': 98},
    {'name': 'Diana', 'dept': 'Marketing', 'ratings': [4.0, 4.2, 3.9, 4.3], 'attendance': 95}
]

# Distractor: Unused metrics
target_quota = 4.0
penalty_factor = 0.9
bonus_eligibility_threshold = 96

# Helper function to calculate quarterly improvement
compute_improvement = lambda ratings: sum(ratings[i] - ratings[i-1] for i in range(1, len(ratings)) if ratings[i] > ratings[i-1])

# Aggregation by department (semi-relevant)
dept_stats = defaultdict(lambda: {'count': 0, 'total_rating': 0.0})
for emp in employee_data:
    dept = emp['dept']
    avg_rating = sum(emp['ratings']) / len(emp['ratings'])
    dept_stats[dept]['count'] += 1
    dept_stats[dept]['total_rating'] += avg_rating

# Distractor: Dead code path (never called)
def adjust_for_bias(data, factor=1.02):
    return [{**entry, 'ratings': [r * factor for r in entry['ratings']]} for entry in data]

# Intermediate computations with some irrelevant variables
improvement_scores = {}
bonus_candidates = []
attendance_penalty = 0

for emp in employee_data:
    name = emp['name']
    ratings = emp['ratings']
    avg_rating = round(sum(ratings) / len(ratings), 2)
    improvement = compute_improvement(ratings)
    
    # Semi-relevant logic: track improvement
    improvement_scores[name] = improvement
    
    # Distractor: attendance penalty not used in final score
    if emp['attendance'] < 95:
        attendance_penalty += 1
    
    if emp['attendance'] >= bonus_eligibility_threshold:
        bonus_candidates.append(name)

# Distractor: unused transformation
shifted_ratings = [[round(r * 1.05, 2) for r in emp['ratings']] for emp in employee_data]

# Core logic: Compute final score based on top performer's smoothed rating and improvement
engineering_avg_improvement = 0.0
eng_count = 0
selected_performances = []

for emp in employee_data:
    if emp['dept'] == 'Engineering':
        avg_impr = compute_improvement(emp['ratings'])
        engineering_avg_improvement += avg_impr
        eng_count += 1
        selected_performances.append(sum(emp['ratings']) / len(emp['ratings']))

if eng_count > 0:
    engineering_avg_improvement /= eng_count

# Final calculation using only Engineering team's data
base_performance = sum(selected_performances) / len(selected_performances)
scaled_bonus = engineering_avg_improvement * 10

# Distractor: unused variables
unused_aggregate = sum(improvement_scores.values())
phantom_threshold = 2.5

# Key statement
final_score = round(base_performance * 100 + scaled_bonus, 2)

print(f"Result: {final_score}")