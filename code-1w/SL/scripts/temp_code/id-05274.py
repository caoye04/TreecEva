from collections import defaultdict

# Simulate employee review data across departments
def generate_feedback():
    employees = ['alice', 'bob', 'carol', 'dave', 'eve']
    reviews = defaultdict(list)
    
    for emp in employees:
        if emp == 'alice':
            reviews[emp].extend([4, 5, 5, 4])
        elif emp == 'bob':
            reviews[emp].extend([3, 3, 4, 5])
        else:
            reviews[emp].extend([4, 4, 4, 4])
    
    return reviews

def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count if count > 0 else 0
    
    # Irrelevant intermediate calculation (distractor)
    squared_sum = sum(x ** 2 for x in scores)
    norm_factor = squared_sum ** 0.5 if squared_sum > 0 else 1
    
    return average

def analyze_trends(avg_dict):
    trend_values = []
    for i, (k, v) in enumerate(avg_dict.items()):
        adjusted = v + (i * 0.1)  # Slight adjustment based on order
        trend_values.append(adjusted)
    
    # Dead code path - never used later (distractor)
    if len(trend_values) > 10:
        return sum(trend_values) / len(trend_values)
    
    return None

def evaluate_performance(feedback_map):
    averages = {}
    feedback_levels = []
    
    # Extract and compute per-employee averages
    for name, scores in feedback_map.items():
        avg = calculate_average(scores)
        averages[name] = avg
        
        # Categorize performance level
        if avg >= 4.5:
            level = 'exceeds'
        elif avg >= 3.5:
            level = 'meets'
        else:
            level = 'needs_improvement'
        feedback_levels.append(level)
    
    # Misleading variable - looks important but unused in final logic (distractor)
    performance_stats = {lvl: feedback_levels.count(lvl) for lvl in set(feedback_levels)}
    
    # Analyze trends - returns None but called anyway (distractor)
    _ = analyze_trends(averages)
    
    # Core logic: count how many have 'exceeds' or 'meets', then apply weighting
    strong_performers = sum(1 for lvl in feedback_levels if lvl in ['exceeds', 'meets'])
    base_score = strong_performers * 100
    
    # Apply bonus only if alice is present and exceeds
    if 'alice' in feedback_map:
        alice_avg = calculate_average(feedback_map['alice'])
        if alice_avg >= 4.5:
            base_score += 25
    
    # Final transformation
    final_score = base_score + 10
    return final_score

# Main execution flow
data = generate_feedback()
feedback_summary = defaultdict(int)
for k, v in data.items():
    feedback_summary[len(v)] += 1  # Count frequency of review counts (irrelevant)

# Key computation step
temp_list = [calculate_average(v) for v in data.values()]
final_score = evaluate_performance(data)
print(f"Result: {final_score}")