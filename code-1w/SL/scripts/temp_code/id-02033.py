from collections import Counter

def calculate_final_score(records):
    counts = Counter([r['status'] for r in records])
    pending_weight = counts.get('pending', 0) * 1.5
    completed_weight = counts.get('completed', 0) * 2
    total_score = pending_weight + completed_weight
    
    # Irrelevant distraction: unused variable
    max_possible = len(records) * 2
    
    if total_score > 20:
        total_score = int(total_score // 1.8)
    
    return total_score

# Data setup
submission_data = [
    {'id': 1, 'status': 'completed'},
    {'id': 2, 'status': 'pending'},
    {'id': 3, 'status': 'completed'},
    {'id': 4, 'status': 'pending'},
    {'id': 5, 'status': 'completed'},
    {'id': 6, 'status': 'failed'},
    {'id': 7, 'status': 'completed'},
    {'id': 8, 'status': 'pending'}
]

# Additional irrelevant variable
processing_mode = "batch"

final_score = calculate_final_score(submission_data)
print(f"Result: {final_score}")