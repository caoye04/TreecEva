def calculate_performance():
    # Simulate team member performance scores
    members = ['Alice', 'Bob', 'Charlie', 'Diana']
    raw_scores = [85, 92, 78, 96]
    
    # Apply attendance factor (string method used to clean data)
    attendance_records = "  present,present,absent,present  "
    status_list = attendance_records.strip().split(',')
    attendance_bonus = [5 if stat.strip() == 'present' else -2 for stat in status_list]
    
    # Compute adjusted individual scores
    adjusted_scores = [raw_scores[i] + attendance_bonus[i] for i in range(len(raw_scores))]
    
    # Assign scores to team members using dictionary
    team_scores = {members[i]: adjusted_scores[i] for i in range(len(members))}
    
    # Calculate base adjustment from score differences
    score_range = max(adjusted_scores) - min(adjusted_scores)
    adjustment = len([s for s in adjusted_scores if s >= 90])
    
    # Critical statement: determine final score based on minimum team performance and bonus
    final_score = min(team_scores.values()) + adjustment
    
    # Irrelevant distraction: sort names alphabetically (no impact)
    sorted_names = sorted(members, reverse=True)
    temp_value = sum([len(name) for name in sorted_names])
    
    print(f"Result: {final_score}")

calculate_performance()