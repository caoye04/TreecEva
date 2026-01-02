from collections import Counter

def analyze_feedback(reports):
    feedback_counter = Counter()
    temp_tracker = []
    
    for report in reports:
        department = report['dept']
        rating = report['rating']
        feedback_counter[department] += rating
        
        # Distractor: tracking something not used later
        if rating < 3:
            temp_tracker.append(department)
    
    # Irrelevant transformation
    normalized = {k: v / (sum(feedback_counter.values()) + 1e-5) for k, v in feedback_counter.items()}
    
    return feedback_counter

def calculate_efficiency_index(data):
    # Unused helper function — red herring
    total = 0
    count = 0
    for item in data:
        if item > 2:
            total += item * 1.5
        count += 1
    return total / (count + 1)

def compute_growth_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
    return trend  # Not actually used

# Simulated input data
reports_list = [
    {'dept': 'engineering', 'rating': 4},
    {'dept': 'marketing', 'rating': 3},
    {'dept': 'engineering', 'rating': 5},
    {'dept': 'sales', 'rating': 2},
    {'dept': 'marketing', 'rating': 4},
    {'dept': 'sales', 'rating': 3},
    {'dept': 'engineering', 'rating': 4}
]

feedback_counts = analyze_feedback(reports_list)

def evaluate_performance(counter, rate):
    base = sum(counter.values())
    bonus = len([v for v in counter.values() if v >= 8]) * 5
    penalty = 0
    
    # Conditional logic with partial relevance
    if 'sales' in counter and counter['sales'] < 6:
        penalty += 3
    
    # Multiple steps with intermediate variables
    intermediate_total = base + bonus - penalty
    adjustment = 0
    
    # Nested conditionals (2 levels deep)
    if intermediate_total > 15:
        if 'engineering' in counter:
            adjustment += 2
        else:
            adjustment -= 1
    else:
        adjustment += 1
    
    # Final computation
    result = intermediate_total + adjustment
    return result

# Secondary distractor calculation
ratings_only = [r['rating'] for r in reports_list]
growth = compute_growth_trend(ratings_only)
efficiency = calculate_efficiency_index(ratings_only)

improvement_rate = sum(ratings_only) / len(ratings_only)

# Key statement
final_score = evaluate_performance(feedback_counts, improvement_rate)

Result: final_score