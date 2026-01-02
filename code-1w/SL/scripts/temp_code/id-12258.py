from collections import Counter

def calculate_final_score(records):
    # Extract scores and count occurrences
    scores = [r['score'] for r in records if r['status'] == 'completed']
    score_count = Counter(scores)
    
    # Calculate weighted sum based on frequency
    weighted_sum = 0
    for score, count in score_count.items():
        weighted_sum += score * (count ** 1.5)
    
    # Apply adjustment factor based on unique score count
    unique_adjustment = len(score_count) * 2.5
    intermediate = weighted_sum / (len(scores) + 1)
    final_score = int(intermediate + unique_adjustment)
    
    # Irrelevant distraction: unused variable (minimal interference)
    debug_info = {'processed': len(records), 'dropped': len([r for r in records if r['status'] != 'completed'])}
    
    return final_score

# Main data input
data = [
    {'score': 8, 'status': 'completed'},
    {'score': 6, 'status': 'failed'},
    {'score': 8, 'status': 'completed'},
    {'score': 4, 'status': 'completed'},
    {'score': 6, 'status': 'completed'},
    {'score': 4, 'status': 'completed'},
    {'score': 8, 'status': 'completed'}
]

result = calculate_final_score(data)
print(f"Result: {result}")