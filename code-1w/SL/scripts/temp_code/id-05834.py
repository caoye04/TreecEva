from collections import defaultdict

# Simulate employee review data with multiple metrics
employee_data = [
    {'name': 'alice', 'dept': 'eng', 'rating': 4.2, 'peer_reviews': [4, 5, 4], 'projects': 3},
    {'name': 'bob', 'dept': 'mkt', 'rating': 3.8, 'peer_reviews': [3, 4], 'projects': 5},
    {'name': 'carol', 'dept': 'eng', 'rating': 4.5, 'peer_reviews': [5, 5, 4], 'projects': 4},
    {'name': 'dave', 'dept': 'mkt', 'rating': 3.1, 'peer_reviews': [3, 2], 'projects': 6}
]

# Mapping for department bonuses
bonus_factor = {'eng': 1.2, 'mkt': 1.1}

# Accumulate total ratings per department
dept_totals = defaultdict(float)
dept_counts = defaultdict(int)

for emp in employee_data:
    dept = emp['dept']
    dept_totals[dept] += emp['rating']
    dept_counts[dept] += 1

# Compute average rating by department
avg_dept_rating = {dept: dept_totals[dept] / dept_counts[dept] for dept in dept_totals}

# Misleading distraction: unused transformation
transformed_ratings = [round(r ** 1.1 - 0.5, 2) for r in dept_totals.values()]
dropped_projects = sum(e['projects'] for e in employee_data if e['rating'] < 3.5)

# Feedback aggregation map (key structure for evaluation)
feedback_map = {}
for emp in employee_data:
    name = emp['name']
    base = emp['rating']
    peer_avg = sum(emp['peer_reviews']) / len(emp['peer_reviews'])
    adjusted = (base * 0.7) + (peer_avg * 0.3)
    feedback_map[name] = {
        'base': base,
        'peer_avg': peer_avg,
        'adjusted': adjusted,
        'dept': emp['dept']
    }

# Unused helper function (dead code path)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core evaluation logic
extra_credits = []
for name, data in feedback_map.items():
    dept_bonus = bonus_factor[data['dept']]
    credit = data['adjusted'] * dept_bonus
    if data['adjusted'] > 4.0:
        credit += 0.2  # high performer incentive
    extra_credits.append(credit)

# Final performance score calculation
raw_sum = sum(extra_credits)
normalizer = len(employee_data) * 1.5
penalty = 0.0
if len(transformed_ratings) > 2:
    penalty = 0.15

intermediate_result = (raw_sum - penalty) / normalizer

# Secondary adjustment based on project load
project_weights = [e['projects'] / 10 for e in employee_data]
weight_correction = sum(project_weights) * 0.05

final_score = round(intermediate_result + weight_correction, 4)

# Output result as required
print(f"Result: {final_score}")