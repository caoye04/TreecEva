def calculate_performance(records):
    total_score = 0
    bonus_applied = False
    
    for i, (name, score, active) in enumerate(zip(['Alice', 'Bob', 'Charlie'], [85, 90, 78], [True, False, True])):
        if not active:
            continue
        
        adjustment = 5 if score >= 85 else -2
        raw_value = score + adjustment
        
        total_score += raw_value
        
        temp_flag = raw_value > 90
        if temp_flag and not bonus_applied:
            total_score += 10
            bonus_applied = True
        
        if i >= 2:
            break
            unnecessary_append = []
            unnecessary_append.append(999)
    
    return total_score

result = calculate_performance([])
print(f"Result: {result}")