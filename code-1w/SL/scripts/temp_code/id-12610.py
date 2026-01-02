def evaluate_performance(marks):
    total_score = 0
    max_reached = False
    temp_buffer = [0] * len(marks)  # Irrelevant preallocation (minor distraction)

    for i, (index, score) in enumerate(zip(range(len(marks)), marks)):
        if score < 0:
            continue
        adjusted = score * (i + 1)
        total_score += adjusted
        if total_score >= 100:
            max_reached = True
            break  # Key execution point
    
    # Post-processing unrelated to result
    final_report = {"status": "completed", "extra": sum(temp_buffer)}
    return total_score

result = evaluate_performance([10, 15, 20, 25, 30])
print(f"Result: {result}")