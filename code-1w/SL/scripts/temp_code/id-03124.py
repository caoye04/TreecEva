from collections import defaultdict

def calculate_final_score(participants):
    scores = defaultdict(float)
    adjustments = {'easy': 1.1, 'medium': 1.25, 'hard': 1.5}
    
    for name, data in participants.items():
        level = data['level']
        base = data['base_score']
        multiplier = adjustments.get(level, 1.0)
        bonus = 5 if data['completed_on_time'] else 0
        penalty = 10 if data['errors'] > 2 else 0
        
        raw_score = base * multiplier + bonus - penalty
        scores[name] = max(raw_score, 0)  # No negative scores
    
    total = sum(scores.values())
    count = len(scores)
    average = total / count if count else 0
    
    final_score = round(average, 2)
    return final_score

# Participant data
contestants = {
    'Alice': {'base_score': 80, 'level': 'hard', 'completed_on_time': True, 'errors': 1},
    'Bob': {'base_score': 75, 'level': 'medium', 'completed_on_time': False, 'errors': 3},
    'Charlie': {'base_score': 90, 'level': 'hard', 'completed_on_time': True, 'errors': 0}
}

irrelevant_counter = 0
for i in range(3):
    irrelevant_counter += i

final_score = calculate_final_score(contestants)
print(f"Result: {final_score}")