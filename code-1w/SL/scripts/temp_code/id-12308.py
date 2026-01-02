def process_item(x):
    if x % 2 == 0:
        return x ** 2 - 3 * x + 2
    else:
        return x ** 3 + 2 * x - 1

# Simulate sensor readings with noise filtering
data = [i for i in range(15) if i % 3 != 0]

# Irrelevant transformation (distractor)
transformed = list(map(lambda val: (val + 5) * 2 if val < 10 else val / 2, data))

# Noise threshold simulation (unused)
noise_floor = sum([d for d in data if d > 5]) / len(data)
baseline_offset = 0.78

# Secondary processing with partial overlap
temps = [process_item(d) for d in data if d % 4 != 3]

# Accumulate weighted contributions
def calculate_final_score(values):
    score = 0
    weights = [0.5, 1.0, 1.5, 2.0]
    
    for i, v in enumerate(values):
        temp_val = abs(v) % 100
        if temp_val > 20:
            score += temp_val * weights[i % 4]
        elif temp_val > 10:
            score += temp_val * 0.5
        else:
            score += temp_val * 1.2
            
        # Dead code branch (distractor)
        if v < 0 and temp_val < 5:
            score -= 100  # Never reached

    # Extra logic that doesn't affect final result
    adjustment = sum([t for t in temps if t < 0]) // 10 if any(t < 0 for t in temps) else 0
    score += adjustment  # This will always be 0 since no negative temps
    
    return int(score)

# Execute main logic
final_score = calculate_final_score(temps)

# Print result as required
print(f"Target result: {final_score}")