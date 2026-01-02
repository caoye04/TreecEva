def calculate_final_score(record):
    name, scores, penalties = record
    base = sum(scores)
    penalty_deduction = len([p for p in penalties if p == 'minor']) * 2
    penalty_deduction += len([p for p in penalties if p == 'major']) * 5
    adjustment_factor = 1.1 if 'excellent' in name.lower() else 0.9
    return int((base - penalty_deduction) * adjustment_factor)

# Irrelevant utility function (mild distraction)
def format_name(s):
    return s.strip().title()

# Main data
user_data = {
    'name': 'Excellent Programmer',
    'attempts': 3,
    'active': True
}

data_tuple = (
    user_data['name'],
    [85, 90, 78, 92],
    ['minor', 'minor', 'major']
)

final_score = calculate_final_score(data_tuple)
print(f"Result: {final_score}")