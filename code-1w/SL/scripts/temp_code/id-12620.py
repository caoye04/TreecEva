from collections import defaultdict

# Simulate student test scores across multiple subjects
def process_student_data():
    raw_scores = [85, 90, 78, 92]
    subject_names = ['math', 'physics', 'chemistry', 'biology']
    weights = {'math': 0.3, 'physics': 0.25, 'chemistry': 0.2, 'biology': 0.25}

    # Irrelevant variable (minor distraction)
    average_score = sum(raw_scores) / len(raw_scores)

    # Map scores to subjects using slicing and case conversion
    subject_map = {name.upper(): score for name, score in zip(subject_names, raw_scores)}

    def calculate_final_score(scores, weight_dict):
        weighted_sum = 0.0
        for i, subject in enumerate(subject_names):
            subject_upper = subject.upper()
            if subject_upper in subject_map:
                weighted_sum += subject_map[subject_upper] * weight_dict[subject]
        return weighted_sum

    final_score = calculate_final_score(raw_scores, weights)
    
    # Distractor: unused variable
    temp_result = [x ** 0.5 for x in raw_scores]
    
    return final_score

result = process_student_data()
print(f"Result: {result}")