def evaluate_performance(log_entries):
    total_actions = len(log_entries)
    success_count = sum(1 for entry in log_entries if entry['status'] == 'SUCCESS')
    failure_count = total_actions - success_count

    base_rate = success_count / total_actions if total_actions > 0 else 0
    raw_score = base_rate * 100

    # Extract recent outcomes for trend analysis using slicing
    recent_outcomes = log_entries[-5:]
    recent_successes = [r['status'] == 'SUCCESS' for r in recent_outcomes]
    
    # Convert booleans to numeric for processing (case conversion equivalent)
    recent_flags = [int(s) for s in recent_successes]

    # Trend bonus if last three are all successes
    trend_bonus = 10 if len(recent_flags) >= 3 and sum(recent_flags[-3:]) == 3 else 0

    # Apply arithmetic adjustment based on failure count
    penalty_adjustment = -2 * failure_count

    final_base = raw_score + trend_bonus
    adjusted_score = final_base + penalty_adjustment

    return adjusted_score

# Simulated log data
logs = [
    {'timestamp': '001', 'status': 'SUCCESS'},
    {'timestamp': '002', 'status': 'FAILURE'},
    {'timestamp': '003', 'status': 'SUCCESS'},
    {'timestamp': '004', 'status': 'SUCCESS'},
    {'timestamp': '005', 'status': 'SUCCESS'},
    {'timestamp': '006', 'status': 'SUCCESS'}
]

result = evaluate_performance(logs)
print(f"Result: {result}")