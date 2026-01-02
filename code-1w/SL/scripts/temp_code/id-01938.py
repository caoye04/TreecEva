def calculate_final_score(students, subject):
    base_scores = {name: data[subject] for name, data in students.items() if subject in data}
    
    # Irrelevant distraction: counting names with more than 5 letters
    long_names_count = len([name for name in students.keys() if len(name) > 5])
    
    avg_score = sum(base_scores.values()) / len(base_scores)
    bonus = 5 if avg_score >= 85 else 2
    
    # Apply conditional bonus using string method to check naming convention
    adjusted_names = [name.title() for name in base_scores.keys()]
    title_case_match = sum(1 for name in base_scores.keys() if name == name.title())
    
    final_score = avg_score + bonus + (1 if title_case_match == len(adjusted_names) else 0.5)
    return final_score

students_data = {
    'Alice': {'Math': 92, 'Science': 88},
    'bob': {'Math': 78, 'Science': 91},
    'Charlie': {'Math': 96},
    'Diana': {'Math': 89, 'History': 84}
}
subject_focus = 'Math'

final_score = calculate_final_score(students_data, subject_focus)
print(f"Result: {final_score}")