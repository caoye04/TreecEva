# Student course enrollment analysis
def analyze_course_enrollment():
    # Core courses taken by student A
    student_a_courses = {"Math101", "Physics202", "CS150", "English101", "History105"}
    
    # Core courses taken by student B
    student_b_courses = {"Math101", "Chemistry201", "CS150", "Psychology100"}
    
    # Find courses common to both students
    common_courses = student_a_courses.intersection(student_b_courses)
    
    # Elective courses available this semester
    elective_courses = {"Art110", "Music120", "CS150", "Physics202"}
    
    # Find courses that are in exactly one of common_courses and elective_courses
    # (symmetric difference)
    unique_elements = len(common_courses.symmetric_difference(elective_courses))
    
    # Calculate total course options
    total_options = len(student_a_courses.union(student_b_courses).union(elective_courses))
    
    return unique_elements

result = analyze_course_enrollment()
print(f"Result: {result}")