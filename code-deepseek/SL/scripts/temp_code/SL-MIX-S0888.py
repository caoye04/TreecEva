def score_check(data):
    base_score = 85
    adjustment = 0
    
    if data.startswith('high'):
        adjustment = 12
    elif data.endswith('plus'):
        adjustment = 8
    
    performance_level = len(data) // 4
    if performance_level > 3:
        adjustment += 5
    
    final_score = base_score + adjustment
    return final_score

performance_data = 'high-performance-plus'
final_score = score_check(performance_data)
print(f"Target result: {final_score}")