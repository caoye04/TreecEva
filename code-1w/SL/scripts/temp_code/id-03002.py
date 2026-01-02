from itertools import compress

def calculate_total(marks, penalties):
    # Apply diminishing penalty based on position
    adjusted_marks = [marks[i] * (0.95 ** i) for i in range(len(marks))]
    
    # Determine valid entries using a filter mask
    threshold_mask = [mark >= 70 for mark in marks]
    filtered_marks = list(compress(adjusted_marks, threshold_mask))
    
    # Calculate base total
    base_total = sum(filtered_marks)
    
    # Apply cumulative penalty factor
    penalty_factor = sum(penalties) * 0.1
    final_score = base_total - penalty_factor
    
    # Irrelevant distraction: string manipulation not affecting logic
    report_summary = "Final evaluation complete. Score: " + str(round(final_score))
    summary_length = len(report_summary)
    
    return final_score

# Main data
marks = [85, 90, 72, 65, 93]
penalties = [2, 1, 3]

# Execution point
final_score = calculate_total(marks, penalties)
print(f"Result: {final_score}")