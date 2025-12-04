# Student course registration system analysis

# First student's registered courses
student1_courses = {'Math101', 'Physics202', 'Chemistry101', 'Literature305', 'History101'}

# Second student's registered courses
student2_courses = {'ComputerScience101', 'Physics202', 'Literature305', 'Economics201'}

# Find courses that both students are taking
common_courses = student1_courses.intersection(student2_courses)

# Count total unique courses between both students
total_unique = len(student1_courses.union(student2_courses))

# Calculate percentage of course overlap
if total_unique > 0:
    overlap_percentage = (len(common_courses) / total_unique) * 100
else:
    overlap_percentage = 0

print(f"Result: {len(common_courses)}")