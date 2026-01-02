def optimize_storage(items, limit):
    processed = [x for x in items if x > limit]
    transform = lambda val: val * 0.9 if val > 50 else val * 1.1
    adjusted = [transform(x) for x in processed]
    total = sum(adjusted)
    return round(total, 3)

# System configuration parameters
threshold = 15
units = [10, 25, 60, 8, 45, 70, 30]

# Irrelevant calibration values (minimal distraction)
calibration_factor = 1.05
offset_buffer = 200

# Core computation
final_capacity = optimize_storage(units, threshold)

print(f"Result: {final_capacity}")