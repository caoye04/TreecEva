# Student course registration system analysis

def calculate_registration_stats(courses_data):
    total_registrations = sum(len(students) for course, students in courses_data.items())
    avg_class_size = total_registrations / len(courses_data) if courses_data else 0
    return total_registrations, avg_class_size

# Course offerings with registered students
courses = {
    'CS101': ['Alice', 'Bob', 'Charlie', 'David'],
    'MATH200': ['Alice', 'Eve', 'Frank', 'Grace'],
    'PHYS150': ['Bob', 'David', 'Heidi'],
    'ENG220': ['Charlie', 'Grace', 'Ivan'],
    'HIST110': ['Alice', 'Bob', 'Frank', 'Ivan']
}

# Calculate overall statistics
total_reg, avg_size = calculate_registration_stats(courses)

# Map students to their courses
student_to_courses = {}
for course, students in courses.items():
    for student in students:
        if student not in student_to_courses:
            student_to_courses[student] = set()
        student_to_courses[student].add(course)

# Find students with most and least courses
max_courses = 0
min_courses = float('inf')
for student, enrolled in student_to_courses.items():
    course_count = len(enrolled)
    max_courses = max(max_courses, course_count)
    min_courses = min(min_courses, course_count)

# Analyze course overlap between two specific students
student1 = 'Alice'
student2 = 'Bob'

student1_courses = student_to_courses.get(student1, set())
student2_courses = student_to_courses.get(student2, set())

# Calculate unique courses for each student
student1_unique = student1_courses.difference(student2_courses)
student2_unique = student2_courses.difference(student1_courses)

# Calculate courses taken by both students
common_courses = len(student1_courses.intersection(student2_courses))

# Identify popular courses (3+ students)
popular_courses = [course for course, students in courses.items() if len(students) >= 3]
popular_count = len(popular_courses)

# Calculate registration diversity score (not used in final result)
diversity_score = sum(len(set(students)) for course, students in courses.items()) / len(courses)

print(f"Result: {common_courses}")