from collections import defaultdict

# Simulate student quiz results with bonus logic
correct_answers = [True, False, True, True, False, True]
bonus_awarded = [False, False, True, False, False, True]
scores = defaultdict(int)

for i, (correct, bonus) in enumerate(zip(correct_answers, bonus_awarded)):
    if not correct:
        continue
    scores['base'] += 1
    if bonus:
        scores['bonus'] += 2
    # Early termination when second bonus is awarded
    if scores['bonus'] == 4:
        break

# Irrelevant distractor: unused calculation for another metric
average_time_per_question = 30.5  
extra_point = bonus_awarded.count(True) > 2

total_score = scores['base'] * 3 + scores['bonus']
print(f"Result: {total_score}")