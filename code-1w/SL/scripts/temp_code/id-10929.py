def evaluate_performance(output, stability):
    base_score = 75
    bonus = 0
    
    # Assess productivity using set operations
    target_outputs = {1, 2, 3, 4, 5, 6}
    achieved_outputs = {x for x in output if x in target_outputs}
    productivity_rate = len(achieved_outputs) / len(target_outputs)
    
    # Evaluate reliability with dictionary and logical checks
    system_logs = {
        'node1': True,
        'node2': True,
        'node3': False
    }
    active_nodes = [status for status in system_logs.values()]
    reliability = all(active_nodes) or (stability and len(active_nodes) > 2)
    
    # Compute final score
    if productivity_rate >= 0.8:
        bonus += 15
    elif productivity_rate >= 0.5:
        bonus += 5
    
    if not reliability:
        bonus -= 10
    
    temp_debug = 999  # Irrelevant debug variable (distractor)
    
    final_score = base_score + bonus
    return final_score

# Input data
productivity = [1, 3, 4, 5, 6, 7, 8]
stability = True

# Execution point
final_score = evaluate_performance(productivity, reliability=stability)
print(f"Result: {final_score}")