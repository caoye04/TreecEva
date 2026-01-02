from collections import defaultdict

def calculate_final_score(students):
    scores = defaultdict(float)
    counts = defaultdict(int)
    
    # Process each student's test results
    for student in students:
        name = student['name']
        for subject, grade in student['grades'].items():
            if grade >= 60:  # Passing threshold
                scores[name] += grade
                counts[name] += 1
    
    # Compute average only for students with passing grades
    averages = {}
    for name in scores:
        if counts[name] > 0:
            averages[name] = scores[name] / counts[name]
    
    # Base final score on number of passing subjects and average
    total_passing = sum(counts.values())
    overall_avg = sum(averages.values()) / len(averages) if averages else 0
    
    # Final composite score
    final_score = int(total_passing * overall_avg / 10)
    
    # Irrelevant utility (minimal distraction)
    temp_log = [f'{k}: {v:.1f}' for k, v in averages.items()]
    log_size = len(temp_log)
    
    return final_score

# Data setup
students = [
    {
        'name': 'Alice',
        'grades': {'math': 85, 'physics': 78, 'chemistry': 92}
    },
    {
        'name': 'Bob',
        'grades': {'math': 55, 'physics': 81, 'chemistry': 73}
    },
    {
        'name': 'Charlie',
        'grades': {'math': 90, 'physics': 45, 'chemistry': 88}
    }
]

final_score = calculate_final_score(students)
print(f"Result: {final_score}")