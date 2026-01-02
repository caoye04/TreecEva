def calculate_final_score(results):
    base_points = 0
    bonuses = {}
    for category, entries in results.items():
        count = len(entries)
        if count > 2:
            bonuses[category] = count * 2
        else:
            bonuses[category] = count
        base_points += count
    
    adjustment = 0
    for val in bonuses.values():
        adjustment += val
        
    final_score = base_points + adjustment
    return final_score

# Simulation data for user activity scoring
task_results = {
    "login_attempts": ["success", "fail"],
    "file_uploads": ["doc", "img", "archive", "log"],
    "permissions_changed": ["read", "write"]
}

final_score = calculate_final_score(task_results)
print(f"Result: {final_score}")