def transform_grades(grades_list, curve_factor=0):
    # Apply curve and normalize grades
    transformed = [min(100, max(0, g + curve_factor)) for g in grades_list]
    # This normalization isn't actually used
    normalized = [(g - min(transformed)) / (max(transformed) - min(transformed)) 
                 if max(transformed) != min(transformed) else 0.5 
                 for g in transformed]
    return transformed

def calculate_weighted_average(values, weights):
    # Calculate weighted average with validation
    if len(values) != len(weights):
        return sum(values) / len(values)  # Fallback to simple average
    
    # Misleading calculation that isn't used
    geometric_mean = 1
    for v in values:
        if v > 0:  # Avoid zero values for geometric mean
            geometric_mean *= v ** (1/len(values))
    
    # Actual weighted average calculation
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def extract_student_performance(data):
    # Extract relevant metrics from student data
    attendance = data.get('attendance', [])
    participation = data.get('participation', [])
    
    # Calculate misleading metrics
    consistency_score = 0
    if attendance:
        consistency_score = sum(1 for a in attendance if a > 0.8) / len(attendance)
    
    # Extract grades and apply transformations
    grades = data.get('grades', [])
    weighted_grades = data.get('weighted_grades', {})
    
    return {
        'attendance_rate': sum(attendance) / len(attendance) if attendance else 0,
        'participation_score': sum(participation) / len(participation) if participation else 0,
        'grades': grades,
        'weighted_grades': weighted_grades,
        'consistency': consistency_score  # Unused metric
    }

def calculate_final_score(student_data):
    # Process student performance data
    performance = extract_student_performance(student_data)
    
    # Apply curve to grades based on attendance
    attendance_factor = performance['attendance_rate'] * 5
    curved_grades = transform_grades(performance['grades'], 
                                    curve_factor=attendance_factor if attendance_factor > 2 else 0)
    
    # Calculate component scores
    exam_score = calculate_weighted_average(curved_grades, [1] * len(curved_grades))
    
    # Process weighted assignments
    weighted_scores = []
    weighted_factors = []
    
    for category, details in performance['weighted_grades'].items():
        if category == 'projects':
            # Special handling for projects
            project_scores = details['scores']
            project_weights = details['weights']
            # Misleading calculation - not actually used
            best_project = max(project_scores) if project_scores else 0
            
            # Use conditional expression to determine which scores to include
            filtered_scores = [s for s, w in zip(project_scores, project_weights) 
                              if w >= 0.15 or s > 85]
            
            # This is what actually gets used
            if filtered_scores:
                project_avg = sum(filtered_scores) / len(filtered_scores)
                weighted_scores.append(project_avg)
                weighted_factors.append(details['category_weight'])
        else:
            # Handle other categories
            cat_scores = details.get('scores', [])
            if cat_scores:
                # Another misleading calculation
                median_score = sorted(cat_scores)[len(cat_scores)//2] if cat_scores else 0
                
                # Actual calculation used
                category_avg = sum(cat_scores) / len(cat_scores)
                weighted_scores.append(category_avg)
                weighted_factors.append(details.get('category_weight', 1))
    
    # Calculate final weighted score
    weighted_component = 0
    if weighted_scores:
        weighted_component = calculate_weighted_average(weighted_scores, weighted_factors)
    
    # Calculate participation adjustment
    participation_adjustment = performance['participation_score'] * 3
    
    # Combine components for final score
    raw_score = exam_score * 0.4 + weighted_component * 0.6
    
    # Apply adjustments
    adjusted_score = raw_score + participation_adjustment
    
    # Final score capped at 100
    return min(100, adjusted_score)

# Student data with various metrics
student_data = {
    'attendance': [0.9, 1.0, 0.8, 0.7, 1.0, 0.9, 0.9],
    'participation': [0.5, 0.7, 0.6, 0.8, 0.9],
    'grades': [78, 82, 91, 65, 88],
    'weighted_grades': {
        'projects': {
            'scores': [91, 84, 77, 95],
            'weights': [0.2, 0.1, 0.3, 0.2],
            'category_weight': 2.5
        },
        'assignments': {
            'scores': [88, 92, 85, 79, 90],
            'category_weight': 1.5
        },
        'discussions': {
            'scores': [95, 88, 92, 97],
            'category_weight': 1.0
        }
    }
}

# Calculate the final score
target_score = calculate_final_score(student_data)
print(f"Result: {target_score}")