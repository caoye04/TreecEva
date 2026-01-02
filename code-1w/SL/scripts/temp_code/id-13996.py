from collections import defaultdict

# Simulate employee review data with nested feedback
employee_data = [
    {'name': 'alice', 'dept': 'eng', 'ratings': [4, 5, 4, 5], 'tags': ['reliable', 'quiet']},
    {'name': 'bob', 'dept': 'eng', 'ratings': [3, 4, 3, 4], 'tags': ['talkative', 'creative']},
    {'name': 'carol', 'dept': 'design', 'ratings': [5, 5, 4, 5], 'tags': ['reliable', 'leader']},
    {'name': 'dave', 'dept': 'design', 'ratings': [2, 3, 3, 4], 'tags': ['struggling', 'quiet']}
]

# Distractor: Unused counters for other analytics
title_count = defaultdict(int)
duplicate_tracker = set()

# Build department-wise feedback map
feedback_map = defaultdict(lambda: defaultdict(list))
for emp in employee_data:
    dept = emp['dept']
    name_lower = emp['name'].lower()
    title_count[emp['dept']] += 1  # Irrelevant to final result
    if name_lower in duplicate_tracker:
        continue  # Dead code path (no duplicates)
duplicate_tracker.add(name_lower)
    
    # Process ratings
    avg_rating = sum(emp['ratings']) / len(emp['ratings'])
    category = 'high' if avg_rating >= 4.0 else 'low'
    feedback_map[dept][category].append(avg_rating)

# Helper function to compute performance score
def calculate_category_score(scores):
    base = sum(scores)
    bonus = 0.0
    if len(scores) > 2:
        bonus = 1.5  # Team size bonus
    adjustment = 0.0
    for s in scores:
        if s > 4.5:
            adjustment += 0.2
    return base + bonus + adjustment

def evaluate_performance(feedback_map):
    total = 0.0
    scaling_factor = 1.1
    
    # Distractor: Initialize unused tracking vars
    temp_results = []
    max_seen = -1
    
    for dept, categories in feedback_map.items():
        dept_score = 0
        if 'high' in categories:
            high_performers = categories['high']
            dept_score += calculate_category_score(high_performers)
        if 'low' in categories:
            low_performers = categories['low']
            # Apply penalty only if more than one low performer
            if len(low_performers) > 1:
                dept_score -= len(low_performers) * 0.5
        
        # Normalize by department count (only two depts)
        normalized = dept_score * scaling_factor
        temp_results.append(normalized)  # Collected but not directly used
        if normalized > max_seen:
            max_seen = normalized
    
    # Final aggregation
    final_component = sum(temp_results) + max_seen * 0.5
    return int(round(final_component))

# Key execution point
final_score = evaluate_performance(feedback_map)
print(f"Result: {final_score}")