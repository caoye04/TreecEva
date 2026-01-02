from collections import defaultdict

def calculate_final_score(log_entries):
    # Initialize score and counters
    base_score = 100
    penalty_map = defaultdict(int)
    
    # Process each log entry
    for entry in log_entries:
        action = entry['action']
        duration = entry['duration']
        
        if action == 'login_fail':
            penalty_map['security'] += 10
        elif action == 'timeout':
            penalty_map['usability'] += 5
        elif action == 'idle':
            penalty_map['engagement'] += 3
        
        # Apply time-based bonus decay (modular arithmetic)
        if duration > 60:
            base_score -= (duration // 10) % 7

    # Aggregate penalties
    total_penalty = sum(penalty_map.values())
    
    # Compute final score with floor limit
    final_score = base_score - total_penalty
    final_score = max(final_score, 0)
    
    return final_score

# Simulated user interaction data
log_data = [
    {'action': 'login_fail', 'duration': 15},
    {'action': 'login_fail', 'duration': 22},
    {'action': 'timeout', 'duration': 95},
    {'action': 'idle', 'duration': 120},
    {'action': 'timeout', 'duration': 78}
]

# Irrelevant utility variable (minor distraction - intervention level 5)
temp_buffer = []

final_score = calculate_final_score(log_data)
print(f"Result: {final_score}")