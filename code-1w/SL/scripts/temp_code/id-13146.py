def calculate_employee_score():
    base_points = 85
    days_absent = 3
    team_performance = 'high'
    peer_reviews = [4.2, 4.5, 4.0, 4.8]
    review_avg = sum(peer_reviews) / len(peer_reviews)
    
    # Performance category mapping
    performance_map = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
    performance_level = performance_map.get('Alice', 'D')
    
    # Irrelevant string processing
    employee_name = "Alice Johnson"
    name_parts = employee_name.split()
    initials = ''.join([part[0] for part in name_parts])
    formatted_name = f"{name_parts[-1]}, {initials}"
    
    # Distractor: unused function
    def calculate_tenure_bonus(years):
        return years * 100 if years > 5 else 0
    
    # Unused metrics
    login_frequency = {'Mon': 1, 'Tue': 1, 'Wed': 0, 'Thu': 1, 'Fri': 1}
    total_logins = sum(login_frequency.values())
    avg_logins_per_active_day = total_logins / (len(login_frequency) - 1) if login_frequency['Wed'] == 0 else total_logins / len(login_frequency)
    
    # Core logic with interference
    adjustment_factor = 1.0
    if review_avg >= 4.5:
        adjustment_factor = 1.2
    elif review_avg >= 4.0:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 1.0

    apply_bonus = True if performance_level in ['A', 'B'] and not (days_absent > 2) else False
    
    # Extra distraction: unused dictionary operations
    metadata_tags = {'dept': 'eng', 'level': 'mid', 'status': 'active'}
    tag_count = len(metadata_tags)
    metadata_tags['score_version'] = 'v2'
    metadata_tags.pop('status')

    # Final computation
    potential_bonus = 15 if apply_bonus else 0
    final_score = int((base_points * adjustment_factor) + potential_bonus)
    
    # More red herring: irrelevant loop
    cumulative_offset = 0
    for i in range(3):
        for j in range(2):
            cumulative_offset += (i * j) - 1
    
    # Output the target variable
    print(f"Result: {final_score}")
    
    return final_score

# Execute function
calculate_employee_score()