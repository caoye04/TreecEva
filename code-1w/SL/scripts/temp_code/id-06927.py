def calculate_final_score(results):
    scores = {}
    for subject, data in results.items():
        raw_score = sum(data['grades'])
        bonus = len(data['awards']) * 2
        scores[subject] = raw_score + bonus
    
    # Normalize scores using max scaling
    max_score = max(scores.values())
    normalized = {s: (score / max_score) * 100 for s, score in scores.items()}
    
    # Apply attendance adjustment
    total_adjustment = 0
    for subject, data in results.items():
        attendance_rate = data['attendance'] / 40  # out of 40 sessions
        if attendance_rate < 0.75:
            total_adjustment -= 5
    
    final_score = int(sum(normalized.values()) / len(normalized)) + total_adjustment
    return final_score

# Dataset
results = {
    'math': {
        'grades': [85, 90, 78],
        'awards': ['honor_roll'],
        'attendance': 38
    },
    'physics': {
        'grades': [88, 85, 82],
        'awards': ['science_fair', 'honor_roll'],
        'attendance': 36
    },
    'chemistry': {
        'grades': [92, 80, 85],
        'awards': [],
        'attendance': 32
    }
}

final_score = calculate_final_score(results)
print(f"Target result: {final_score}")