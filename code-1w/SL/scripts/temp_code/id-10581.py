def calculate_final_score(students, thresholds):
    final_scores = []
    extra_weight = 1.1
    bonus_flag = False
    
    for idx, (name, score) in enumerate(students):
        adjusted_score = score * extra_weight
        
        if idx % 2 == 0:
            adjusted_score += 2
        
        category = 'low'
        if adjusted_score >= thresholds['high']:
            category = 'high'
        elif adjusted_score >= thresholds['medium']:
            category = 'medium'

        penalty = 3 if category == 'low' and 'x' in name else 0
        adjusted_score -= penalty
        
        final_scores.append(adjusted_score)
    
    total = sum(final_scores)
    final_score = int(total / len(final_scores))
    return final_score

students_list = [('alice', 85), ('bob', 76), ('carol', 80), ('dave', 70)]
thresholds_dict = {'low': 60, 'medium': 75, 'high': 85}
irrelevant_counter = 0

for s in students_list:
    if len(s[0]) > 4:
        irrelevant_counter += 1

result = calculate_final_score(students_list, thresholds_dict)
print(f"Target result: {result}")