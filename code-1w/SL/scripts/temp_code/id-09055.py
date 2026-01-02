from collections import Counter

# Simulate student quiz results with question difficulty levels
def analyze_quiz_performance(responses, correct_answers, difficulty_map):
    score = 0
    bonus_points = 0
    effort_metric = len(responses)

    # Count correct answers by difficulty
    correct_by_difficulty = Counter()
    
    for q_id, response in responses.items():
        if response == correct_answers[q_id]:
            difficulty = difficulty_map[q_id]
            correct_by_difficulty[difficulty] += 1
            score += 1
            if difficulty == 'hard':
                bonus_points += 2

    return score, correct_by_difficulty, bonus_points

# Grading rubric based on performance tiers
def calculate_final_score(performance_data):
    base_score = performance_data[0]
    correct_counts = performance_data[1]
    bonus = performance_data[2]
    
    # Apply multiplier for hard question mastery
    hard_correct = correct_counts.get('hard', 0)
    multiplier = 1.2 if hard_correct >= 3 else 1.0
    
    # Small adjustment for consistent medium-level performance
    medium_correct = correct_counts.get('medium', 0)
    consistency_bonus = 0.5 if medium_correct >= 4 else 0
    
    raw_score = (base_score + bonus) * multiplier + consistency_bonus
    
    # Normalize to grading scale
    return int(raw_score * 10)

# Dataset setup
responses = {
    'Q01': 'A', 'Q02': 'B', 'Q03': 'C', 'Q04': 'B',
    'Q05': 'A', 'Q06': 'B', 'Q07': 'C', 'Q08': 'A',
    'Q09': 'B', 'Q10': 'D'
}

correct_answers = {
    'Q01': 'A', 'Q02': 'B', 'Q03': 'B', 'Q04': 'B',
    'Q05': 'C', 'Q06': 'B', 'Q07': 'C', 'Q08': 'A',
    'Q09': 'B', 'Q10': 'D'
}

difficulty_map = {
    'Q01': 'easy',   'Q02': 'easy',   'Q03': 'medium',
    'Q04': 'medium', 'Q05': 'hard',   'Q06': 'medium',
    'Q07': 'hard',   'Q08': 'hard',   'Q09': 'medium',
    'Q10': 'hard'
}

# Irrelevant auxiliary variable (minimal distraction)
temp_analysis = [responses[q] for q in responses if difficulty_map[q] == 'easy']

# Key computation steps
initial_analysis = analyze_quiz_performance(responses, correct_answers, difficulty_map)
final_score = calculate_final_score(initial_analysis)

print(f"Result: {final_score}")