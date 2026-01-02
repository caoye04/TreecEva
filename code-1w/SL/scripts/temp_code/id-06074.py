from collections import defaultdict

# Simulate student exam results with subject-wise scores
def get_exam_data():
    data = defaultdict(list)
    data['math'].extend([85, 90, 78])
    data['physics'].extend([88, 76, 82])
    data['chemistry'].append(91)
    return data

# Calculate average for each subject and apply bonus for consistent performance
def calculate_final_score(results):
    subject_averages = {}
    for subject, scores in results.items():
        avg = sum(scores) / len(scores)
        # Bonus if all scores in subject are above 80
        if all(s >= 80 for s in scores):
            avg += 5  # performance bonus
        subject_averages[subject] = avg
    
    # Compute total weighted score: math (40%), physics (30%), chemistry (30%)
    weights = {'math': 0.4, 'physics': 0.3, 'chemistry': 0.3}
    total_score = sum(subject_averages[sub] * weights[sub] for sub in subject_averages)
    return round(total_score, 3)

# Irrelevant helper (minor distraction)
def unused_helper():
    return "This function is not used"

# Main execution flow
exam_results = get_exam_data()

# Key assignment statement
total_score = calculate_final_score(exam_results)

print(f"Result: {total_score}")