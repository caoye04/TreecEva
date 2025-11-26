import itertools

# Process student assessment data
def process_assessments(student_scores):
    intermediate_results = []
    temp_storage = []
    
    # Calculate running averages (distractor)
    for i in range(len(student_scores)):
        running_avg = sum(student_scores[:i+1]) / (i+1)
        temp_storage.append(running_avg)
    
    # Main processing with itertools
    processed_data = []
    for score_pair in itertools.pairwise(student_scores):
        improvement_factor = score_pair[1] - score_pair[0]
        processed_data.append(improvement_factor)
    
    # Some intermediate calculations that don't affect final result
    backup_calc = sum(student_scores) * 0.1
    validation_check = max(student_scores) - min(student_scores)
    
    return processed_data, backup_calc

# Initial student scores
assessment_data = [85, 92, 78, 96, 88]
backup_value = 42

# Process the data
processed_data, unused_backup = process_assessments(assessment_data)

# Final calculation with conditional logic
final_score = processed_data[-1] if processed_data else backup_value

# Print the result
print(f"Result: {final_score}")