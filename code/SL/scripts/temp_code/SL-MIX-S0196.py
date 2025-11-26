def process_student_scores():
    student_scores = [85, 92, 78, 96, 88, 74, 95, 81, 89, 93]
    passing_threshold = 80
    
    # Filter scores using lambda and conditional expression
    filtered_data = list(filter(lambda x: x >= passing_threshold if x % 2 == 0 else x > passing_threshold, student_scores))
    
    # Simple sorting operation
    filtered_data.sort()
    
    # Target computation - sum first and last filtered elements
    final_count = filtered_data[0] + filtered_data[-1]
    
    print(f"Target result: {final_count}")

process_student_scores()