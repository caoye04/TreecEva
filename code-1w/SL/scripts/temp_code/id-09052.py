def calculate_performance(records):
    weights = [0.2, 0.3, 0.5]
    adjusted_scores = []
    
    for i, record in enumerate(records):
        score = record['score']
        category = record['category']
        multiplier = weights[i]
        adjusted = score * multiplier
        adjusted_scores.append(adjusted)
    
    base_total = sum(adjusted_scores)
    bonus = 0.0
    
    # Bonus logic based on performance consistency
    deviations = list(map(lambda x: abs(x['score'] - 70), records))
    avg_deviation = sum(deviations) / len(deviations)
    
    if avg_deviation < 15:
        bonus = 5.0
    
    final = base_total + bonus
    return round(final, 3)

# Irrelevant auxiliary variable (minimal distraction)
status_messages = ['OK', 'WARNING', 'ERROR']

assessments = [
    {'score': 80, 'category': 'technical'},
    {'score': 75, 'category': 'behavioral'},
    {'score': 65, 'category': 'cultural'}
]

final_score = calculate_performance(assessments)
print(f"Result: {final_score}")