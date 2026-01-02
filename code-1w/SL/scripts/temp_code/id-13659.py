def calculate_final_score(records):
    total = 0
    penalties = set()
    for record in records:
        action = record['action']
        duration = record['duration']
        if action == 'timeout':
            penalties.add('timeout')
        elif action == 'retry':
            total -= 5
        else:
            total += duration // 2
    
    # Irrelevant string operation (minor distraction)
    status_msg = "Processing complete".upper()
    extra_penalty = len(status_msg) % 3
    
    if 'timeout' in penalties:
        total -= 10
    
    sorted_durations = sorted([r['duration'] for r in records])
    median_duration = sorted_durations[len(sorted_durations) // 2]
    
    # Final adjustment based on median and penalties
    final_adjustment = median_duration // 4
    total -= final_adjustment
    
    return total

# Input data
log_data = [
    {'action': 'start', 'duration': 12},
    {'action': 'retry', 'duration': 8},
    {'action': 'pause', 'duration': 16},
    {'action': 'timeout', 'duration': 20},
    {'action': 'resume', 'duration': 24}
]

final_score = calculate_final_score(log_data)
print(f"Target result: {final_score}")