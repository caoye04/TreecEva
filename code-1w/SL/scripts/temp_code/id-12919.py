def calculate_performance(rewards):
    base_points = 85
    multiplier = 1.2
    
    # Extract performance modifiers
    speed_bonus = rewards['speed']
    accuracy_bonus = rewards['accuracy']
    consistency_bonus = rewards['consistency']
    
    # Apply conditional scaling based on achievement level
    if speed_bonus > 7:
        base_points += 10
    
    if accuracy_bonus >= 5 and consistency_bonus >= 6:
        base_points += 15
    
    raw_score = (base_points + speed_bonus) * multiplier
    
    # Final adjustment using string-based rule lookup
    tier = 'A' if raw_score >= 120 else 'B'
    adjustments = {'A': 8, 'B': -2}
    final_score = raw_score + adjustments[tier]
    
    return final_score

# Bonus data from evaluation cycle
data_log = {"speed": 8, "accuracy": 6, "consistency": 7}
irrelevant_entry = "debug: timestamp_2023"

temp_value = len(irrelevant_entry)  # Minor distraction

final_score = calculate_performance(data_log)
print(f"Result: {final_score}")