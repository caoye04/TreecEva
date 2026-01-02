def calculate_final_score(attempts):
    base_points = 10
    bonus_multiplier = 1
    total_score = 0
    
    for attempt in attempts:
        # Clean string processing to extract result and count
        clean_attempt = attempt.strip().lower()
        if 'success' in clean_attempt:
            count_str = ''.join(filter(str.isdigit, clean_attempt))
            count = int(count_str) if count_str else 1
            total_score += base_points * count
            if 'critical' in clean_attempt:
                bonus_multiplier += 0.1
        
    total_score = int(total_score * bonus_multiplier)
    return total_score

# Simulated input log entries from game attempts
attempts_log = [
    'success: 3 enemies defeated',
    'minor success - 1 objective completed',
    'critical success: 2 targets neutralized',
    'success',
    'failure: no impact'
]

# Irrelevant auxiliary variable (minimal distraction)
summary_report = "Analysis complete: {} events processed".format(len(attempts_log))

total_score = calculate_final_score(attempts_log)
print(f"Result: {total_score}")