def evaluate_performance(marks):
    passing_threshold = 50
    bonus_grant = 10

    # Apply bonus to marks close to passing
    enhanced_marks = [mark + bonus_grant if mark >= 40 and mark < passing_threshold else mark for mark in marks]
    
    # Determine which students passed after enhancement
    passed_students = [score for score in enhanced_marks if score >= passing_threshold]

    # Filter out any unusually high scores (potential data errors)
    filtered_performance = [score for score in passed_students if score <= 100]

    extra_buffer = 5  # Irrelevant variable, minor distraction
    temp_log = "Evaluation complete"  # Non-impacting logging string

    final_score = sum(filtered_performance)
    print(f"Result: {final_score}")

# Input data
test_scores = [45, 38, 70, 49, 88, 102, 41]
evaluate_performance(test_scores)