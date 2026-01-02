def compute_final_score(items, factors):
    base_score = 0
    bonus_points = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    for idx, item in enumerate(items):
        if idx % 2 == 0:
            temp_result.append(item * 1.1)
        else:
            temp_result.append(item * 0.95)
    
    # Actual scoring logic
    weighted_sum = 0
    weight_acc = 0
    for val, wt in zip(items, factors):
        weighted_sum += val * wt
        weight_acc += wt
    
    normalized = weighted_sum / weight_acc if weight_acc != 0 else 0
    
    # Bitwise manipulation as secondary factor (semi-relevant)
    magic_key = 0
    for i in range(len(items)):
        magic_key ^= i + 1  # XOR accumulation over indices
    
    # Bonus rule: if magic_key is odd, add 5
    if magic_key % 2 == 1:
        bonus_points += 5
    
    # Dummy loop with no effect (dead code path)
    debug_trace = []
    for x in items:
        if x > 100:
            debug_trace.append(x // 10)
    
    # Final computation
    base_score = int(normalized)
    final_score = base_score + bonus_points - penalty
    
    return final_score

# Input data
data = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

# Compute result
final_score = compute_final_score(data, weights)
print(f"Result: {final_score}")