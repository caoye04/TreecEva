from collections import Counter
def process_metrics(conv, stability):
    base = conv * 2
    offset = len(stability) // 2
    temp_result = base + offset
    
    # Irrelevant counter for distraction (minimal interference)
    stat_counter = Counter(stability)
    adjustment = 0
    for val in stability:
        if val > 75:
            adjustment += 1
    
    final_value = temp_result + adjustment
    return final_value

# Simulation parameters
current_reading = 47
convergence = current_reading + 13
stability_set = {80, 92, 67, 71, 89, 95}

# Key computation step
final_score = process_metrics(convergence, stability_set)
print(f"Result: {final_score}")