def process_input(raw_data):
    cleaned = ''.join([c for c in raw_data if c.isdigit() or c in '-.'])
    return float(cleaned) if cleaned else 0.0

raw_log = "Error: invalid input -3.45 detected at line 21"

parsed_value = process_input(raw_log)
delta = abs(parsed_value)
offset = delta * 2.5

convergence_factor = 0
for i in range(3):
    temp_val = (delta + i) ** 0.5
    if temp_val > 2:
        convergence_factor += temp_val / (i + 1)
    else:
        convergence_factor -= temp_val

# Irrelevant tracking variables (distractors)
data_points = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
weighted_sum = sum(w * d for w, d in zip(weights, data_points))

scaling_factor = len(data_points) // 2
buffer_array = [x * scaling_factor for x in data_points if x % 2 == 0]

# Unused computation path (dead code, mild red herring)
def unused_helper(arr):
    return [a ** 2 for a in arr if a > 2]

# Actual logic buried among distractions
def calculate_rating(factor, points):
    base = factor * len(points)
    adjustment = 0
    for p in points:
        if p % 2 == 0:
            adjustment += p // 2
        else:
            adjustment -= p
    return int(base + adjustment)

# Key assignment with complex dependencies
final_score = calculate_rating(convergence_factor, data_points)

# Print required output
print(f"Result: {final_score}")