def determine_outcome(data):
    avg = sum(x for x in data if x > 0) / len(data)
    is_stable = (lambda x: x >= 3.5)(avg)
    adjustment = 1.2 if is_stable else -0.8
    return int(avg + adjustment)

measurements = [2.1, 3.6, 4.0, 3.8, 2.9]
baseline = 3.0
offset = 0.5
threshold_score = baseline + offset
depth_factor = 2
final_evaluation = determine_outcome(measurements)
threshold_score = final_evaluation * depth_factor
print(f"Result: {threshold_score}")