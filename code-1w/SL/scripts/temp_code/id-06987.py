def analyze_soil_composition(elements):
    # Irrelevant computation: calculates unused soil score
    soil_score = sum(ord(ch) for ch in elements) % 7
    return soil_score > 3

# Simulate agricultural plot data
element_list = ['N', 'P', 'K', 'C', 'O']
plot_ids = [101, 102, 103, 104]
moisture_levels = [0.3, 0.5, 0.8, 0.4]
temperature_data = [22, 25, 20, 18]

# Distractor: unused transformation
transformed = [round((t - 15) * 1.8 + 32) for t in temperature_data]

# Actual relevant data
plots = list(zip(plot_ids, moisture_levels))
conditions = [analyze_soil_composition(element_list), True, False, True]

# State tracker with some irrelevant fields
state_log = []
running_total = 0
baseline_offset = len(element_list) * 2  # Unused baseline

# Helper function with conditional expression and enumerate
def calculate_harvest_efficiency(plot_data, env_conditions):
    efficiency = 1.0
    bonus_applied = False
    
    for i, (pid, moisture) in enumerate(plot_data):
        # Relevant condition using boolean logic and comparison
        is_favorable = env_conditions[i] and (0.4 <= moisture <= 0.7)
        
        # Bitwise flag tracking (semi-relevant)
        flag_state = (i + 1) & 3
        
        # Conditional expression affecting result
        adjustment = 1.2 if is_favorable else 0.85
        
        # Accumulate efficiency with modular arithmetic
        efficiency = (efficiency * adjustment * 100) % 97
        
        # Log entry (not used later, but adds cognitive load)
        state_log.append(f"Step {i}: {adjustment}, flag={flag_state}")
        
        # Hidden trigger: on third loop, apply fixed bonus
        if i == 2:
            bonus_applied = True
            efficiency += 5
    
    # Final adjustment using string method (distractor check)
    key = "harvest".upper().replace("S", "X")  # 'HARVEXT'
    if 'V' in key:
        efficiency += len(key) // 2  # Adds 3
    
    return int(efficiency)

# Execute main logic
intermediate_check = sum(moisture_levels) / len(moisture_levels)  # 0.5
final_yield = calculate_harvest_efficiency(plots, conditions)
print(f"Result: {final_yield}")