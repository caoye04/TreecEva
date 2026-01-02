def calculate_performance(base, tweaks):
    adjustment_sum = sum(abs(x) for x in tweaks)
    modifier = len(tweaks) % 3
    if modifier == 0:
        base += adjustment_sum // 2
    elif modifier == 1:
        base -= adjustment_sum // 4
    else:
        base += adjustment_sum // 5
    
    # Irrelevant string processing (distractor, minimal interference)
    status_msg = "Processing complete"
    status_msg.upper()
    status_msg.replace("complete", "finished")
    
    return base

# Initial parameters
baseline = 87
adjustments = [-4, 12, -9, 3]

# Key computation step
temp_result = baseline * 2
final_score = calculate_performance(baseline, adjustments)

print(f"Result: {final_score}")