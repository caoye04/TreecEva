def process_performance(att_str, levels):
    present_days = len(att_str.strip(' -'))
    avg_activity = sum(levels) / len(levels)
    boosted_score = avg_activity * 10
    if 'FULL' in att_str.upper():
        boosted_score += 5
    return int(boosted_score + present_days)

# Simulate weekly attendance and daily activity scores
attendance_str = 'MON-WED-FRI-FULL'
activity_levels = [0.85, 0.91, 0.76, 0.88, 0.95]

final_score = process_performance(attendance_str, activity_levels)
print(f"Result: {final_score}")