from collections import Counter
def analyze_performance(logs):
    success_count = 0
    total_attempts = len(logs)
    for log in logs:
        if log['status'] == 'success':
            success_count += 1
    return success_count / total_attempts if total_attempts > 0 else 0

def calculate_final_score(results, multiplier):
    count = Counter(results)
    base_score = sum(count[grade] * (idx + 1) for idx, grade in enumerate('ABCDE') if grade in count)
    adjustment = 10 if count['A'] > count['C'] else -5
    return int((base_score + adjustment) * multiplier)

def main():
    # System logs (irrelevant to final score but part of data flow)
    system_logs = [
        {'timestamp': '00:01', 'status': 'success'},
        {'timestamp': '00:02', 'status': 'failure'},
        {'timestamp': '00:03', 'status': 'success'}
    ]
    
    performance_ratio = analyze_performance(system_logs)
    
    # Actual grading results used in calculation
    student_results = ['A', 'B', 'A', 'C', 'D', 'A', 'B']
    bonus_multiplier = 1.5 if performance_ratio >= 0.5 else 1.0
    
    final_score = calculate_final_score(student_results, bonus_multiplier)
    
    # Debug print (not counted in logic)
    debug_info = {'processed_count': len(student_results), 'multiplier_used': bonus_multiplier}
    
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()