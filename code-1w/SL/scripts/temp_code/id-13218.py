def calculate_final_score(students):
    # Extract passing students using list comprehension
    passing = [s for s in students if s['grade'] >= 70]
    
    # Calculate average grade of passing students
    total = sum(s['grade'] for s in passing)
    avg = total / len(passing) if passing else 0
    
    # Apply curve: add bonus if average is below 85
    curve = 5 if avg < 85 else 0
    curved_avg = avg + curve
    
    # Count how many students have names starting with vowels
    vowels = 'AEIOU'
    vowel_names = len([s for s in passing if s['name'][0].upper() in vowels])
    
    # Final score computation: curved average adjusted by vowel count
    final_score = curved_avg + (vowel_names * 2)
    return final_score

# Dataset
students_data = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 65},
    {'name': 'Eve', 'grade': 75},
    {'name': 'Oliver', 'grade': 80},
    {'name': 'Charlie', 'grade': 60},
    {'name': 'Uma', 'grade': 88}
]

# Execution
final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")