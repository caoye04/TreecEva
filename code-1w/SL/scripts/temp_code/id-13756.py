def analyze_productivity(logs):
    total_hours = sum([entry['hours'] for entry in logs])
    completed_tasks = len([entry for entry in logs if entry['status'] == 'done'])
    efficiency = completed_tasks / total_hours if total_hours > 0 else 0
    return efficiency

logs_data = [
    {'hours': 8, 'status': 'done', 'tag': 'urgent'},
    {'hours': 3, 'status': 'pending', 'tag': 'minor'},
    {'hours': 5, 'status': 'done', 'tag': 'critical'},
    {'hours': 2, 'status': 'done', 'tag': 'minor'}
]

# Extraneous analysis with unused results
efficiency_ratio = analyze_productivity(logs_data)
overhead_cost = len(logs_data) * 0.5
weight_map = {'urgent': 2, 'critical': 3, 'minor': 1}
score_weights = [weight_map[entry['tag']] for entry in logs_data]
adjusted_effort = sum([w * e['hours'] for w, e in zip(score_weights, logs_data)])

# Real computation begins
base_contribution = sum([entry['hours'] * weight_map[entry['tag']] for entry in logs_data])
task_bonus = 10 if len([e for e in logs_data if e['status'] == 'done']) >= 3 else 5
contributions = base_contribution + task_bonus

# Distractor: irrelevant string processing
raw_tags = ','.join([entry['tag'] for entry in logs_data])
processed_tags = raw_tags.upper().replace('URGENT', 'PRIORITY').split(',')
tag_frequency = {tag: processed_tags.count(tag) for tag in set(processed_tags)}
summary_string = ''.join([t[0] for t in processed_tags])

# More distractions: unused conditional and lambda
is_high_pressure = lambda x: 'yes' if x > 6 else 'no'
diagnostic_flag = is_high_pressure(len(logs_data))

if efficiency_ratio > 0.7:
    contingency_adjustment = 1.2
else:
    contingency_adjustment = 0.9  # Not actually used later

# Actual key logic
penalty_factor = 0.1 * len([e for e in logs_data if e['status'] == 'pending'])
penalty_factor = round(penalty_factor, 2)

# Core calculation function with closure
def calculate_rating(contribs, penalty):
    base_rating = contribs * (1 - penalty)
    
    # Nested logic with red herring
    def apply_curve(value):
        curve = lambda x: x ** 1.1 if x < 50 else x ** 1.05
        return curve(value)
    
    curved_rating = apply_curve(base_rating)
    
    # Conditional expression (Python idiom)
    final = curved_rating if curved_rating >= 40 else 40
    return final

# Key statement
final_score = calculate_rating(contributions, penalty_factor)

# Print result as required
print(f"Result: {final_score}")