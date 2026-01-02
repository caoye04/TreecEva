def evaluate_performance(marks, thresholds):
    adjusted_values = []
    bonus_applied = False
    
    for i, (mark, threshold) in enumerate(zip(marks, thresholds)):
        if mark >= threshold:
            adjusted_mark = mark * 1.1
        else:
            adjusted_mark = mark * 0.9
        
        # Apply conditional bonus on every third passing score
        if (i + 1) % 3 == 0 and mark >= threshold:
            adjusted_mark += 5
            bonus_applied = True
            
        adjusted_values.append(round(adjusted_mark))
    
    total_score = sum(adjusted_values)
    return total_score

# Input data
marks_list = [78, 85, 90, 60, 72, 88]
thresholds_list = [75, 80, 85, 65, 70, 85]

result = evaluate_performance(marks_list, thresholds_list)
print(f"Target result: {result}")