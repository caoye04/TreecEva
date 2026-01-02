from collections import Counter

def calculate_final_score(records):
    count = Counter([r['status'] for r in records])
    passed = count.get('passed', 0)
    failed = count.get('failed', 0)
    skipped = count.get('skipped', 0)

    base_score = passed * 10 - failed * 5 + skipped * 2
    
    # Apply bonus if more than half passed
    bonus = 25 if passed > (failed + skipped) else 0
    
    # Conditional adjustment based on effort level
    total_tests = passed + failed + skipped
    effort_level = 'high' if total_tests > 10 else 'low'
    scaling_factor = 1.2 if effort_level == 'high' else 1.0

    adjusted_score = base_score + bonus
    final_score = int(adjusted_score * scaling_factor)
    
    return final_score

# Simulated input data
test_data = [
    {'id': 1, 'status': 'passed'},
    {'id': 2, 'status': 'passed'},
    {'id': 3, 'status': 'failed'},
    {'id': 4, 'status': 'passed'},
    {'id': 5, 'status': 'skipped'},
    {'id': 6, 'status': 'passed'},
    {'id': 7, 'status': 'failed'},
    {'id': 8, 'status': 'passed'},
    {'id': 9, 'status': 'passed'},
    {'id': 10, 'status': 'skipped'},
    {'id': 11, 'status': 'passed'}
]

final_score = calculate_final_score(test_data)
print(f"Result: {final_score}")