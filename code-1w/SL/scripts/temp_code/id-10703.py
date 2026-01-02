def main():
    # Student performance evaluation system
    exam_scores = [85, 92, 78, 96, 88]
    assignment_completion = ['A:done', 'B:pending', 'C:done', 'D:done']

    # Irrelevant student metadata (minor distraction)
    student_id = 'S12345'
    enrollment_year = 2022

    # Compute average exam score
    avg_exam = sum(exam_scores) / len(exam_scores)
    
    # Determine pass status using lambda
    is_passing = lambda x: 'pass' if x >= 80 else 'fail'
    exam_result = is_passing(avg_exam)
    
    # Count completed assignments using string method
    completed_count = len([task for task in assignment_completion if task.endswith('done')])
    
    # Filter logic based on completion threshold
    assignment_filter = 'high' if completed_count >= 3 else 'low'
    
    # Final scoring logic
    def calculate_final(exam_status, comp_level):
        base = 50
        if exam_status == 'pass':
            base += 30
        if comp_level == 'high':
            base += 20
        return base
    
    final_score = calculate_final(exam_result, assignment_filter)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()