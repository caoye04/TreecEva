from collections import defaultdict
from itertools import combinations

# Simulate student test responses and scoring logic
def evaluate_responses(responses, answer_key):
    score = 0
    penalty = 0
    response_count = defaultdict(int)
    
    for i, (response, correct) in enumerate(zip(responses, answer_key)):
        response_count[response] += 1
        if response == correct:
            score += 3
        elif response != 'X':  # 'X' means no attempt
            penalty += 1
    
    # Irrelevant computation: analyze pair patterns (not used in final score)
    pair_analysis = {}
    for pair in combinations(answer_key, 2):
        pair_analysis[pair] = responses.count(pair[0]) + responses.count(pair[1])
    
    # Distraction: unused transformation
    transformed = [chr(ord(c) + 1) if c != 'X' else c for c in responses]
    
    return score - penalty

# Grading curve adjustment (unused path, but looks relevant)
def apply_curve(raw, factor=1.1):
    curved = raw * factor
    if curved > 100:
        curved = 100
    return int(curved)

# Main processing pipeline
def compute_aggregate(test_data, key):
    total_points = 0
    bonus_tracker = []
    
    for idx, entry in enumerate(test_data):
        raw_score = evaluate_responses(entry['answers'], key)
        
        # Conditional bonus logic (partially dead)
        if raw_score >= 70 and len(entry['answers']) == len(key):
            consecutive_correct = 0
            max_consecutive = 0
            for ans, correct in zip(entry['answers'], key):
                if ans == correct:
                    consecutive_correct += 1
                else:
                    max_consecutive = max(max_consecutive, consecutive_correct)
                    consecutive_correct = 0
            max_consecutive = max(max_consecutive, consecutive_correct)
            
            if max_consecutive >= 5:
                bonus_tracker.append(5)  # Hard-coded bonus
        
        # Accumulate primary score
        total_points += raw_score
    
    # Final aggregation with distraction variables
    avg_base = total_points / len(test_data) if test_data else 0
    inflation_factor = 1.05
    adjusted = avg_base * inflation_factor
    
    # Real final score computation
    final_bonus = sum(bonus_tracker)
    final_score = int(adjusted) + final_bonus
    
    # Unused statistical analysis
    stats = defaultdict(float)
    stats['mean'] = avg_base
    stats['bonus_count'] = len(bonus_tracker)
    stats['inflated'] = adjusted
    
    # Critical output
    print(f"Result: {final_score}")
    return final_score

# Dataset setup
test_key = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'D']
student_data = [
    {'id': 'S001', 'answers': ['A', 'B', 'C', 'A', 'X', 'C', 'A', 'D']},
    {'id': 'S002', 'answers': ['A', 'X', 'C', 'A', 'B', 'B', 'A', 'D']},
    {'id': 'S003', 'answers': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'D']},  # Perfect + consecutive
    {'id': 'S004', 'answers': ['X', 'B', 'C', 'A', 'B', 'C', 'X', 'D']},
    {'id': 'S005', 'answers': ['A', 'B', 'X', 'A', 'B', 'C', 'A', 'D']}   # High score, long streak
]

# Execute
final_score = compute_aggregate(student_data, test_key)