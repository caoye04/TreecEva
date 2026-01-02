from collections import defaultdict

# Simulate employee feedback analysis with improvement tracking

employee_data = [
    {'name': 'alice', 'dept': 'engineering', 'ratings': [4, 5, 4, 5], 'skills': ['python', 'design']},
    {'name': 'bob', 'dept': 'engineering', 'ratings': [3, 4, 3, 4], 'skills': ['java', 'testing']},
    {'name': 'carol', 'dept': 'marketing', 'ratings': [5, 5, 4, 5], 'skills': ['copywriting', 'analytics']},
    {'name': 'dave', 'dept': 'marketing', 'ratings': [4, 4, 4, 3], 'skills': ['events', 'social_media']}
]

# Irrelevant aggregation: department-wise skill count (not used in final logic)
department_skills = defaultdict(set)
for emp in employee_data:
    dept = emp['dept']
    for skill in emp['skills']:
        department_skills[dept].add(skill)

# Extract feedback scores per employee as sets to simulate qualitative feedback
feedback_scores = {}
improvement_needed = {}
baseline_threshold = 4

for emp in employee_data:
    name = emp['name']
    avg_rating = sum(emp['ratings']) / len(emp['ratings'])
    feedback_scores[name] = set([r for r in emp['ratings'] if r < baseline_threshold])
    improvement_needed[name] = avg_rating < 4.0

# Simulate historical improvement data (partially relevant)
historical_improvement = {
    'alice': [0.1, 0.2, 0.15],
    'bob': [0.3, 0.25, 0.4],
    'carol': [0.05, 0.1, 0.08],
    'dave': [0.15, 0.12, 0.18]
}

# Compute average improvement rate per employee (semi-relevant)
improvement_map = {}
for name, improvements in historical_improvement.items():
    improvement_map[name] = round(sum(improvements) / len(improvements), 2)

# Dead code: unused function (distraction)
def calculate_tenure_bonus(years):
    return years * 100  # Not used anywhere

# Distractor variable: total_depts (not used later)
total_depts = len(department_skills)

# Key computation begins: define evaluation function
def evaluate_performance(feedback_set, improvement_rates):
    score = 0
    penalty_factor = 0.8
    bonus_factor = 1.2
    
    for name in feedback_set:
        base_deduction = len(feedback_set[name]) * 5
        
        # Apply adjustment based on improvement history
        if name in improvement_rates:
            adjustment = improvement_rates[name] * 10
            net_impact = base_deduction - adjustment
            
            # Clamp negative impact to zero
            effective_penalty = max(0, net_impact)
            score += effective_penalty
        else:
            score += base_deduction
    
    # Invert score: lower penalties should yield higher performance
    normalized_score = 100 - score
    
    # Additional irrelevant smoothing (no effect due to integer conversion)
    smoothed = round(normalized_score, 1)
    
    return int(smoothed)

# Define feedback_set used in key statement
feedback_set = {name: fs for name, fs in feedback_scores.items() if len(fs) > 0}

# Introduce distractor list comprehension
unused_aggregation = [emp['name'] for emp in employee_data if len(emp['skills']) > 1]

# Key statement
final_score = evaluate_performance(feedback_set, improvement_map)

# Print result
print(f"Result: {final_score}")