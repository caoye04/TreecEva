def calculate_performance(base, tweaks):
    adjustment_factor = sum(tweaks) / len(tweaks) if tweaks else 0
    enhanced = base * (1 + adjustment_factor)
    return int(enhanced // 1.5)

baseline = 85
adjustments = [0.2, -0.1, 0.35]

# Irrelevant tracking variables (minimal distraction)
current_mode = "AUTO"
log_entries = 0

final_score = calculate_performance(baseline, adjustments)
print(f"Result: {final_score}")