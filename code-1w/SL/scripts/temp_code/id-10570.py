def calculate_final_score(data):
    base_score = data['midterm'] * 0.4 + data['final'] * 0.6
    bonus = 0
    if data['attendance'] > 90:
        bonus += 5
    if data['participation']:
        bonus += 3
    adjustments = (data['extra_credit'], bonus)
    final_score = base_score + adjustments[1]
    return final_score

exam_data = {
    'midterm': 85,
    'final': 92,
    'attendance': 95,
    'participation': True,
    'extra_credit': 2
}

irrelevant_counter = 0
for i in range(3):
    irrelevant_counter += i * 2

final_score = calculate_final_score(exam_data)
print(f"Target result: {final_score}")