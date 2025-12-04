def process_enrollment_data(student_ids, enrolled_ids):
    # Calculate various enrollment statistics
    total_students = len(student_ids)
    total_enrolled = len(enrolled_ids)
    
    # Find students who are in both lists
    common_elements = len(set(student_ids).intersection(set(enrolled_ids)))
    
    # Calculate students who didn't enroll
    not_enrolled = total_students - common_elements
    
    return common_elements, not_enrolled

# Student IDs from the database
student_ids = (101, 102, 103, 105, 107, 109, 110)

# IDs of students who enrolled in the course
enrolled_ids = (102, 104, 105, 109, 111)

# Process the data
common_elements, not_enrolled = process_enrollment_data(student_ids, enrolled_ids)

print(f"Result: {common_elements}")