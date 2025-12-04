# University course registration system
import itertools

# Courses each student is registered for
student1_courses = {'Math101', 'Physics202', 'CompSci303', 'English101'}
student2_courses = {'Biology101', 'Chemistry201', 'CompSci303', 'Math101'}

# Potential courses for next semester
future_courses = {'AdvancedAI404', 'DataScience505', 'Robotics303'}

# Count courses that only one of the students is taking (exclusive courses)
unique_courses = len(student1_courses.symmetric_difference(student2_courses))

# Find common courses
shared_courses = student1_courses.intersection(student2_courses)
shared_count = len(shared_courses)

# Create pairs of current and potential future courses
course_combinations = list(itertools.product(shared_courses, future_courses))
recommendation_count = len(course_combinations)

print(f"Result: {unique_courses}")