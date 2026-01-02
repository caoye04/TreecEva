from collections import defaultdict

def calculate_rating(contribs, penalties):
    base_score = 0
    bonus = 0
    deduction = 0
    
    # Process contributions using dictionary operations
    effort_map = defaultdict(int)
    for category, items in contribs.items():
        effort_map[category] = sum([len(item) for item in items])
    
    total_effort = sum(effort_map.values())
    
    if total_effort > 20:
        bonus = 15
    elif total_effort > 10:
        bonus = 5

    # Apply penalty deductions using defaultdict fallback
    for category in contribs.keys():
        deduction += penalties[category]  # default to 0 if not present
    
    base_score = total_effort * 2 + bonus - deduction
    
    # Irrelevant distraction: unused calculation (minimal interference)
    max_category = max(effort_map, key=effort_map.get) if effort_map else None
    temp_factor = len(max_category) if max_category else 0  # Not used
    
    final_score = base_score + 10  # Final adjustment
    return final_score

# Input data
contributions = {
    'documentation': ['setup', 'usage', 'faq'],
    'testing': ['unit', 'integration', 'e2e', 'coverage'],
    'refactoring': ['module_split', 'cleanup', 'optimization', 'restructure', 'naming']
}

penalty_map = defaultdict(int)
penalty_map['dependencies'] = 7
penalty_map['tech_debt'] = 12

# Key execution point
final_score = calculate_rating(contributions, penalty_map)
print(f"Target result: {final_score}")