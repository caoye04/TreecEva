from collections import defaultdict

# Simulate employee feedback analysis across departments
def analyze_feedback():
    raw_data = [4, 5, 2, 3, 5, 4, 1, 3, 2, 5, 4, 4, 3, 2]
    department_map = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'A', 'C', 'B']
    
    # Distractor: irrelevant aggregation
    temp_sum = sum(x * 1.5 for x in raw_data if x > 2)
    temp_list = [x for x in raw_data if x != 1]
    
    # Group feedback by department
    dept_feedback = defaultdict(list)
    for i, dept in enumerate(department_map):
        dept_feedback[dept].append(raw_data[i])
    
    # Compute average per department (semi-relevant)
    avg_feedback = {}
    for dept, scores in dept_feedback.items():
        avg_feedback[dept] = round(sum(scores) / len(scores), 2)
    
    # Distractor: unused transformation
    scaled_avg = {k: v * 1.1 for k, v in avg_feedback.items()}
    
    # Key logic: count how many departments have average >= 3.0
    qualifying_depts = len([v for v in avg_feedback.values() if v >= 3.0])
    
    # Another distractor: complex but unused calculation
    zipped = list(zip(temp_list, [x % 3 for x in range(len(temp_list))]))
    processed = list(map(lambda pair: pair[0] + pair[1], zipped))
    total_offset = sum(processed[::2]) // 2 if processed else 0
    
    # Early return not taken (dead code path)
    if len(avg_feedback) == 10:
        return -1
    
    # Core metric: base score from qualifying departments
    base_score = qualifying_depts * 10
    
    # Bonus for high-performing individual reviews
    excellent_count = sum(1 for x in raw_data if x == 5)
    bonus = 5 if excellent_count >= 3 else 0
    
    # Final score computation
    final_score = base_score + bonus
    
    # Print result as required
    print(f"Result: {final_score}")
    
    return final_score

# Additional distractor function (never called)
def compute_efficiency_rate(data):
    return sum(data) / (len(data) + 1)

# Execute main logic
def evaluate_performance(feedback_levels):
    return analyze_feedback()

feedback_levels = [4, 5, 2, 3, 5, 4, 1, 3, 2, 5, 4, 4, 3, 2]
final_score = evaluate_performance(feedback_levels)