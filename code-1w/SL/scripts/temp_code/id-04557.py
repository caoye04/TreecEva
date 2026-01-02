def evaluate_performance(records):
    total_score = 0
    bonus_applied = False
    temp_buffer = [0, 0, 0]  # unused buffer (minor distraction)

    for i, (success, latency) in enumerate(zip(records, [120, 85, 95, 110])):
        if success == 0:
            continue
        
        base_points = 10
        if latency < 100:
            base_points += 5

        total_score += base_points
        
        if i >= 2 and not bonus_applied:
            total_score += 20
            bonus_applied = True
            break  # Key execution point

    return total_score

# Simulated input data
data_records = [1, 1, 1, 0]
result = evaluate_performance(data_records)
print(f"Result: {result}")