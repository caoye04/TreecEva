def bonus_calc(func, value):
    temp_multiplier = 2.0  # Distractor - not used
    intermediate = value + 5  # Distractor - not used in final
    return func(value)

base_score = 25
metrics_data = {"efficiency": 8.2, "reliability": 9.1, "performance": 12.5}

# Processing steps with some irrelevant operations
processed_metrics = {}
for key, val in metrics_data.items():
    if key.startswith('p'):
        processed_metrics[key] = val * 1.1
    elif key.startswith('r'):
        processed_metrics[key] = val - 0.5  # Distractor - unused
    else:
        processed_metrics[key] = val + 2.0  # Distractor - unused

adjusted_metrics = {k: v * 0.8 for k, v in processed_metrics.items()}
temp_calc = sum(adjusted_metrics.values())  # Distractor - not used

# The critical execution point
final_score = adjusted_metrics.get("performance", 0) + bonus_calc(lambda x: x * 1.5, base_score)

print(f"Target result: {final_score}")