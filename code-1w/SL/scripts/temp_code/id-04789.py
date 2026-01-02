def calculate_performance(base, log):
    adjustments = 0
    peak_activity = max(log.values())
    threshold = base * 0.75
    compliance_count = 0

    # Irrelevant pre-processing (distractor)
    normalized = {k: v / (sum(log.values()) + 1e-5) for k, v in log.items()}
    entropy = 0
    for prob in normalized.values():
        entropy -= prob * prob  # Not used later

    temp_offset = 0
    for day, value in log.items():
        if value > threshold:
            adjustments += 1
        if value >= peak_activity * 0.9:
            compliance_count += 1
        
        # Red herring calculation
        temp_offset += (value // 10) % 3
        
    # Unused helper logic (dead path)
    def debug_status():
        return "OK" if adjustments > 2 else "LOW"
    
    # Core logic embedded with noise
    multiplier = 2 if compliance_count >= 3 else 1
    score = base + (adjustments * multiplier)
    
    # Conditional expression (required Python feature)
    final_bonus = 10 if all(v > 0 for v in log.values()) else 0
    
    return score + final_bonus

# Main execution
baseline = 50
activity_log = {
    'monday': 42,
    'tuesday': 67,
    'wednesday': 55,
    'thursday': 73,
    'friday': 60
}

# Misleading intermediate calculations
phantom_load = sum(v ** 0.5 for v in activity_log.values())
dummy_flag = (phantom_load > 30) ? 1 : 0  # Invalid syntax intentionally avoided

running_total = 0
for val in activity_log.values():
    running_total += val // 5

# Key statement
final_score = calculate_performance(baseline, activity_log)

print(f"Result: {final_score}")