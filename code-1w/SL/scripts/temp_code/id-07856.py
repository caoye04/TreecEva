def process_results(grades, thresholds):
    adjusted = [g + 5 for g in grades if g < 75]
    count_enhanced = len(adjusted)
    
    # Irrelevant distraction: unused variable (mild interference)
    max_possible = max(grades) + 10
    
    # Use of enumerate and tuple unpacking
   优秀_students = 0
    for i, grade in enumerate(grades):
        threshold = thresholds[i % len(thresholds)]
        if grade >= threshold:
            优秀_students += 1
    
    # Use of zip and set operations
    paired = list(zip(grades, thresholds * 2))
    passing_set = {g for g, t in paired if g >= t}
    bonus = len(passing_set) * 2
    
    base_score = sum(grades)
    final_score = base_score + bonus - count_enhanced
    return final_score

# Input data
grades = [88, 72, 91, 65, 83]
thresholds = [70, 75, 80]

final_score = process_results(grades, thresholds)
print(f"Result: {final_score}")