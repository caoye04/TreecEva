def evaluate_performance(log_entries):
    total_chars = 0
    valid_records = 0
    temp_sum = 0
    base_points = 0
    outlier_count = 0
    cumulative_length = 0

    for i, entry in enumerate(log_entries):
        stripped = entry.strip()
        if not stripped:
            continue
        
        parts = stripped.split('|')
        if len(parts) < 2:
            outlier_count += 1
            continue
            
        action = parts[0].lower()
        timestamp_str = parts[1]
        
        char_count = len(entry)
        total_chars += char_count
        cumulative_length += len(stripped.replace('|', ''))
        
        if 'login' in action and timestamp_str.isdigit():
            valid_records += 1
            temp_sum += len(timestamp_str)
        
        if i % 3 == 0:
            temp_sum -= len(action) % 5

    avg_length = total_chars // (valid_records or 1)
    base_points = valid_records * 7 + (cumulative_length % 13)

    # Bonus calculation with distractors
    modifier = 1
    debug_total = 0
    for j in range(valid_records):
        debug_total += j * 2
    
    bonus_adjustment = 0
    if avg_length > 10:
        bonus_adjustment += 15
    if valid_records >= 3:
        bonus_adjustment += 10
    
    redundant_calc = (debug_total * 0.01)  # Irrelevant to final result
    intermediate_flag = True if outlier_count < 2 else False  # Not used later
    
    final_score = base_points + bonus_adjustment
    
    # Extra unrelated operations
    unused_list = [x for x in range(5) if x % 2 == 0]
    shadow_value = sum(unused_list) * 3
    
    print(f"Result: {final_score}")

# Simulated input
logs = [
    "login|1623456", 
    "", 
    "logout|abc", 
    "LOGIN|7890123", 
    "error|invalid", 
    "user_login|112233"
]

evaluate_performance(logs)