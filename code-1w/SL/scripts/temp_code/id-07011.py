def process_results(marks, limits):
    above_threshold = list(map(lambda x: x > limits[0], marks))
    weighted = [marks[i] * 0.5 for i in range(len(marks)) if above_threshold[i]]
    adjusted = sum(weighted) + len([x for x in marks if x <= limits[1]])
    return round(adjusted, 3)

# Irrelevant auxiliary data (minor distraction)
student_names = ['Alice', 'Bob', 'Charlie', 'Diana']
temp_data = [10, 20, 30]

grades = [88, 72, 91, 65, 83]
thresholds = (80, 70)

# Key computation
final_score = process_results(grades, thresholds)
print(f"Result: {final_score}")