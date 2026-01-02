def calculate_efficiency(value, cost):
    base_efficiency = value * 0.85
    adjustment_factor = 1.2 if value > 100 else 0.9
    overhead = 15 if cost > 50 else 5
    
    # Distractor: Irrelevant computation for alternate system
    hypothetical_yield = (value + cost) * 0.75
    deprecated_scale = hypothetical_yield * 0.1  # Unused
    
    intermediate_score = base_efficiency * adjustment_factor - overhead
    return int(intermediate_score)

# Simulate performance metrics
data_points = [78, 92, 88, 96, 73]
score = sum([x for x in data_points if x >= 85])  # List comprehension
penalty = len(data_points) * 2

# Misleading conditional block (dead path)
if score < 50:
    energy_threshold = -1
else:
    temp_flag = True if penalty % 2 == 0 else False  # Conditional expression
    backup_mode = False
    energy_threshold = calculate_efficiency(score, penalty)

# Additional distractor variables
auxiliary_buffer = [score * 0.1, penalty * 0.05]
log_entry = f"Final check: {score}, {penalty}"

print(f"Result: {energy_threshold}")