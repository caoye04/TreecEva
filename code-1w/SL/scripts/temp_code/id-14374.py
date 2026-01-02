from itertools import compress

def process_performance(days_present, activities):
    # Calculate engagement score based on presence and active participation
    base_score = sum(days_present)
    
    # Use itertools.compress to filter activities where student was present
    filtered_activities = list(compress(activities, days_present))
    bonus_points = len([act for act in filtered_activities if act == 'high']) * 2
    
    # Deduct points for consecutive low-activity days
    consecutive_low_penalty = 0
    count_low = 0
    for act in filtered_activities:
        if act == 'low':
            count_low += 1
            if count_low == 3:
                consecutive_low_penalty += 5
                break  # Early return equivalent in loop
        else:
            count_low = 0
    
    final_score = base_score + bonus_points - consecutive_low_penalty
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = len(days_present) * 3
    
    return final_score

# Simulate student data over 7 school days
attendance = [1, 1, 0, 1, 1, 1, 0]  # 1 = present, 0 = absent
activity_levels = ['high', 'medium', 'low', 'low', 'high', 'low', 'high']

final_score = process_performance(attendance, activity_levels)
print(f"Result: {final_score}")