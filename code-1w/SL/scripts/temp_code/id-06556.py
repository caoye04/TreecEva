from itertools import compress

# Simulate sensor weight readings over time (in kg)
base_weight = 75.0
recent_weights = [74.2, 75.1, 76.5, 73.8, 77.0, 74.9]

# Irrelevant auxiliary calculation (minor distraction)
calibration_offset = sum(recent_weights) / len(recent_weights) - base_weight
adjusted_weights = [w - calibration_offset for w in recent_weights]

# Key logic: detect if any recent reading exceeds 10% of base weight
too_high = [weight > base_weight * 1.1 for weight in recent_weights]
threshold_flag = any(weight > base_weight * 1.1 for weight in recent_weights)

# Print result for evaluation
print(f"Result: {threshold_flag}")