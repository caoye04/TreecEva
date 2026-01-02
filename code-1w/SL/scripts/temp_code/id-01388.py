import math

# Simulate ranking-based scoring system for academic performance
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
raw_scores = [85, 92, 78, 96, 88]
participation = [4.2, 3.8, 4.5, 4.0, 3.9]  # out of 5
attendance_rate = [0.95, 0.87, 0.93, 0.98, 0.82]
task_completion = [10, 8, 12, 9, 11]  # number of tasks completed

# Irrelevant data (distractor)
extracurriculars = [3, 1, 4, 2, 5]
bonus_awards = [1, 0, 2, 1, 3]

# Normalize raw scores to 0-100 scale (already in range, but recompute)
normalized_scores = [round((s / 100.0) * 100, 2) for s in raw_scores]

# Compute rank based on raw score (lower index = higher rank)
sorted_indices = sorted(range(len(raw_scores)), key=lambda i: raw_scores[i], reverse=True)
rankings = [0] * len(students)
for rank, idx in enumerate(sorted_indices):
    rankings[idx] = rank + 1

# Weight components for final evaluation
base_weights = {
    'exam': 0.5,
    'participation': 0.2,
    'attendance': 0.15,
    'tasks': 0.15
}

# Adjust weights slightly based on rank position (top performers get more task weight)
adjusted_weights = []
for r in rankings:
    factor = 1.0 + (0.1 if r == 1 else -0.05 if r == 5 else 0)
    new_weights = {k: v * factor for k, v in base_weights.items()}
    # Renormalize
    total = sum(new_weights.values())
    normalized_new_weights = {k: round(v / total, 3) for k, v in new_weights.items()}
    adjusted_weights.append(normalized_new_weights)

# Distractor: unused function
def compute_gpa(score):
    if score >= 90: return 4.0
    elif score >= 80: return 3.0
    elif score >= 70: return 2.0
    else: return 1.0

# Another distractor variable
class_rank_percentile = [round((len(students) - r) / len(students) * 100, 1) for r in rankings]

# Create composite rank data
rank_data = []
for i in range(len(students)):
    data = {
        'student': students[i],
        'raw_score': raw_scores[i],
        'normalized_score': normalized_scores[i],
        'rank': rankings[i],
        'participation': participation[i],
        'attendance': attendance_rate[i],
        'tasks_completed': task_completion[i],
        'weight_set': adjusted_weights[i]
    }
    rank_data.append(data)

# Helper function to calculate weighted score with conditional logic
def calculate_component_score(component, value, weight):
    # Cap values at reasonable maxima
    capped_value = min(value, 5.0) if component == 'participation' else value
    capped_value = min(capped_value, 1.0) if component == 'attendance' else capped_value
    
    # Apply nonlinear scaling for participation using logarithmic boost
    if component == 'participation':
        scaled = 10 * math.log(1 + capped_value, 1 + 5 / 3)  # asymptotic toward 10
    elif component == 'attendance':
        scaled = 100 * capped_value
    elif component == 'tasks':
        scaled = min(capped_value * 8.33, 100)  # ~12 tasks = 100
    else:  # exam
        scaled = capped_value
    
    return scaled * weight

# Main calculation function
def calculate_final_score(data_list, base_weights):
    results = []
    for entry in data_list:
        total = 0.0
        w = entry['weight_set']
        
        # Exam score (primary)
        total += calculate_component_score('exam', entry['normalized_score'], w['exam'])
        
        # Participation
        total += calculate_component_score('participation', entry['participation'], w['participation'])
        
        # Attendance
        attendance_score = entry['attendance'] * 100
        adjusted_attendance = max(attendance_score * w['attendance'], 0)
        total += adjusted_attendance
        
        # Tasks
        task_points = min(entry['tasks_completed'] * 8.33, 100)
        total += task_points * w['tasks']
        
        # Conditional bonus for perfect attendance (distractor: rarely triggered)
        if abs(entry['attendance'] - 1.0) < 1e-5:
            total += 2.5  # small bonus
        
        # Apply curve adjustment based on rank (higher rank gets slight bump)
        rank_boost = max(0, (5 - entry['rank']) * 0.5)
        total += rank_boost
        
        # Cap final score at 100
        capped_total = min(total, 100.0)
        
        # Round only if above threshold (conditional expression)
        rounded_score = round(capped_total, 1) if capped_total > 50 else capped_total
        results.append(rounded_score)
    
    # Return average final score across all students
    average_final = sum(results) / len(results)
    
    # Additional distraction: compute median (unused)
    sorted_results = sorted(results)
    mid = len(sorted_results) // 2
    median_final = (sorted_results[mid] if len(sorted_results) % 2 == 1 
                   else (sorted_results[mid-1] + sorted_results[mid]) / 2)
    
    return average_final

# Execute main computation
final_score = calculate_final_score(rank_data, base_weights)

# Print result as required
print(f"Result: {final_score}")