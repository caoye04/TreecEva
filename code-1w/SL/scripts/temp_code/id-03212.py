from collections import defaultdict

def calculate_final_score():
    # Simulate student quiz results with multiple attempts
    attempts = ['pass', 'fail', 'pass', 'pass']
    scores = [75, 60, 80, 85]
    
    # Count pass/fail outcomes
    outcome_count = defaultdict(int)
    for outcome in attempts:
        outcome_count[outcome] += 1
    
    # Compute base score average (only passing attempts)
    passing_scores = [score for score, outcome in zip(scores, attempts) if outcome == 'pass']
    base_average = sum(passing_scores) / len(passing_scores)
    
    # Bonus logic: extra points if first attempt was fail but overall passes >= 3
    bonus = 0
    if attempts[0] == 'fail' and outcome_count['pass'] >= 3:
        bonus = 10
    
    # Apply bonus and cap final score at 100
    final_score = min(base_average + bonus, 100)
    
    return final_score

# Irrelevant distraction: unused variable (mild interference)
dummy_list = [1, 2, 3]

result = calculate_final_score()
print(f"Result: {result}")