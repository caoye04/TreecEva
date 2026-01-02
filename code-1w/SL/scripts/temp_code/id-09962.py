def calculate_performance(data):
    base_score = 0
    penalties = {'timeout': 3, 'retry': 1, 'fail': 5}
    adjustments = [2, -1, 4]

    for entry in data:
        if entry['status'] == 'success':
            base_score += 10
        elif entry['status'] in penalties:
            base_score -= penalties[entry['status']]
    
    for adj in adjustments:
        base_score += adj if adj > 0 else 0

    multiplier = 1.5 if base_score > 50 else 1.2
    return int(base_score * multiplier)

# Simulated benchmark log
task_log = [
    {'id': 1, 'status': 'success'},
    {'id': 2, 'status': 'timeout'},
    {'id': 3, 'status': 'success'},
    {'id': 4, 'status': 'fail'},
    {'id': 5, 'status': 'success'}
]

initial_offset = 5
final_score = calculate_performance(task_log)
print(f"Result: {final_score}")