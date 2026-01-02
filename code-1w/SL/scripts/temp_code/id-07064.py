def calculate_performance(base, mods):
    temp_score = 0
    penalty_offset = 0.1  # unused distraction
    for i, mod in enumerate(mods):
        if i % 2 == 0:
            temp_score += base * (mod / 100)
        else:
            temp_score -= base * (mod / 200)
    
    # Distractor block: dead computation with no effect
    debug_value = 0
    for x in range(3):
        debug_value += x ** 3  # Irrelevant accumulation
    
    adjustment_factor = len(mods) > 5 else 0.9  # conditional expression
    
    intermediate = temp_score * adjustment_factor
    final_score = int(intermediate + 0.5)  # round to nearest integer
    
    # Extra noise: unused transformation
    normalized = [val / sum(mods) for val in mods] if sum(mods) != 0 else [0] * len(mods)
    
    return final_score

# Main execution
baseline = 1200
adjustments = [10, -5, 20, 15, -10, 25]

# Spurious variable assignments
threshold = 1000
delta_check = baseline - threshold
status_flag = "active" if delta_check > 0 else "inactive"

result_buffer = []
for val in adjustments:
    if val > 0:
        result_buffer.append(val ** 0.5)  # irrelevant sqrt tracking

final_score = calculate_performance(baseline, adjustments)
print(f"Target result: {final_score}")