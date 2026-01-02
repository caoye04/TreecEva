def calculate_final_score(data):
    base_points = data['level'] * 10
    bonus = 5 if data['rank'] in ['A', 'B'] else 0
    penalty = 2 if data['errors'] > 0 else 0
    
    # Irrelevant tracking variable (minor distraction)
    temp_log = f'Processing user {data.get("user_id", "N/A")}'
    
    adjusted = base_points + bonus - penalty
    
    # Conditional expression for multiplier
    multiplier = 1.5 if data['streak'] >= 3 else 1.0
    return int(adjusted * multiplier)

# Main execution
rank_data = {
    'level': 7,
    'rank': 'A',
    'errors': 1,
    'streak': 4,
    'user_id': 'USR9876'
}

final_score = calculate_final_score(rank_data)
print(f"Result: {final_score}")