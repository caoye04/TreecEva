def analyze_performance(records):
    total_tests = len(records)
    passing_scores = [r for r in records if r['score'] >= 60]
    avg_passing = sum(p['score'] for p in passing_scores) / len(passing_scores) if passing_scores else 0
    
    # Distractor: irrelevant computation on timestamps
    timestamps = [r['timestamp'] for r in records]
    time_range = max(timestamps) - min(timestamps) if timestamps else 0
    avg_time_gap = time_range / (len(timestamps) - 1) if len(timestamps) > 1 else 0

    # More distraction: categorizing by name length (unused)
    long_names = {r['name'] for r in records if len(r['name']) > 7}
    short_names = {r['name'] for r in records if len(r['name']) <= 7}
    name_category_ratio = len(long_names) / (len(short_names) + 1)

    return avg_passing, total_tests


def calculate_final_score(data):
    # Extract relevant scores and normalize
    normalized = []
    for entry in data:
        raw_score = entry['score']
        if raw_score < 0:
            raw_score = 0
        elif raw_score > 100:
            raw_score = 100
        normalized.append(raw_score * entry['weight'])
    
    # Real logic: weighted average
    total_weighted = sum(normalized)
    total_weight = sum(entry['weight'] for entry in data)
    weighted_avg = total_weighted / total_weight if total_weight > 0 else 0
    
    # Secondary metric: consistency bonus (if score variance is low)
    squared_diff = sum((entry['score'] - weighted_avg) ** 2 for entry in data)
    variance = squared_diff / len(data) if data else 0
    consistency_bonus = 10 if variance < 50 else 0
    
    # Tertiary: adjustment based on attempt count (distractor logic, not applied)
    attempts = [e['attempt'] for e in data]
    max_attempt = max(attempts) if attempts else 1
    penalty_per_late = 0.5
    mock_penalty = max_attempt * penalty_per_late  # calculated but unused
    
    # Final calculation
    final_score = weighted_avg + consistency_bonus
    return int(final_score)

# Main data input
student_data = [
    {'name': 'Alice', 'score': 85, 'weight': 0.3, 'timestamp': 1625000000, 'attempt': 1},
    {'name': 'Bob', 'score': 92, 'weight': 0.4, 'timestamp': 1625003600, 'attempt': 2},
    {'name': 'Charlie', 'score': 78, 'weight': 0.2, 'timestamp': 1625007200, 'attempt': 1},
    {'name': 'Diana', 'score': 96, 'weight': 0.1, 'timestamp': 1625010800, 'attempt': 3}
]

# Analyze but don't use result (distractor call)
analyze_performance(student_data)

# Actual target computation
final_score = calculate_final_score(student_data)
print(f"Target result: {final_score}")