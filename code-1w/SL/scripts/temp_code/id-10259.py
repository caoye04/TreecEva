def evaluate_performance(efficiency, fault_ratio):
    base_score = 100
    adjustment = (lambda x, y: x * 0.8 if y > 0.05 else x * 1.2)(efficiency, fault_ratio)
    if efficiency >= 80:
        base_score += 20
    elif efficiency >= 60:
        base_score += 10
    else:
        base_score -= 5
    if fault_ratio < 0.03:
        base_score += 15
    return base_score + adjustment

productivity = 75
error_rate = 0.04
temp_buffer = [0] * 100  # Irrelevant preallocation (distractor)
initial_flag = True  # Unused boolean flag (minor distractor)
final_score = evaluate_performance(productivity, error_rate)
print(f"Result: {final_score}")