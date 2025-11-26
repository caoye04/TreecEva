def analyze_competition_results(data):
    # Calculate base scores
    base_total = sum(entry['score'] for entry in data if entry['active'])
    
    # Intermediate calculation (distractor)
    temp_adjustment = len([entry for entry in data if entry['score'] > 50]) * 2
    
    # Apply bonus rules
    bonus_candidates = [entry for entry in data if entry['category'] == 'expert']
    bonus_total = sum(entry['bonus'] for entry in bonus_candidates) if bonus_candidates else 0
    
    # Final score calculation
    final_score = (base_total + bonus_total) // len(data)
    
    # Unused intermediate (distractor)
    max_possible = max(entry['score'] for entry in data) * 1.5
    
    return final_score

# Competition data
participants_data = [
    {'name': 'Alice', 'score': 85, 'bonus': 10, 'category': 'expert', 'active': True},
    {'name': 'Bob', 'score': 42, 'bonus': 5, 'category': 'novice', 'active': True},
    {'name': 'Charlie', 'score': 78, 'bonus': 15, 'category': 'expert', 'active': True},
    {'name': 'Diana', 'score': 91, 'bonus': 20, 'category': 'expert', 'active': False}
]

# Main execution
result = analyze_competition_results(participants_data)
print(f"Result: {result}")