from collections import defaultdict

# Simulate sensor data from a thermal-pressure equilibrium experiment
temperatures = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 29.2]
pressures = [101.3, 102.1, 103.5, 104.8, 105.0, 106.2, 107.4]

# Irrelevant auxiliary data (distractor)
sensor_ids = ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007']
duplicate_check = defaultdict(int)
for sid in sensor_ids:
    duplicate_check[sid] += 1

# Misleading transformation (dead computation path)
stdev_estimate = 0
for i in range(len(temperatures)):
    stdev_estimate += (temperatures[i] - sum(temperatures)/len(temperatures)) ** 2
stdev_estimate = (stdev_estimate / len(temperatures)) ** 0.5

# Normalize values for processing (semi-relevant)
normalized_temps = [round((t - min(temperatures)) / (max(temperatures) - min(temperatures)), 3) for t in temperatures]
normalized_press = [round((p - min(pressures)) / (max(pressures) - min(pressures)), 3) for p in pressures]

# Pairwise correlation attempt (distractor)
correlation_sum = 0
for i, (t_norm, p_norm) in enumerate(zip(normalized_temps, normalized_press)):
    correlation_sum += t_norm * p_norm

# Core logic: calculate equilibrium score using alternating operations
def calculate_equilibrium(temp_list, press_list):
    score = 0
    adjustment_factor = 1.0
    
    for idx, (t, p) in enumerate(zip(temp_list, press_list)):
        # State-dependent operation chain
        if idx % 2 == 0:
            intermediate = (t * 1.2 + p * 0.8) // 1  # integer division
            score += int(intermediate)
            adjustment_factor *= 0.95
        else:
            offset = len(temp_list) - idx
            intermediate = (t * 0.7 + p * 1.3) // 1
            score -= int(intermediate)
            adjustment_factor *= 1.05
            
        # Early break condition based on state (control flow)
        if abs(score) > 1000 and idx > 2:
            break
    
    final_score = int(score * adjustment_factor)
    return final_score

# Additional irrelevant string processing (distractor)
data_origin = "EXP-THRM-PRESS-2024"
valid_chars = [c for c in data_origin if c.isalnum()]
label_suffix = ''.join(valid_chars[-4:])

# Key execution point
equilibrium_score = calculate_equilibrium(temperatures, pressures)

# Output result as required
print(f"Result: {equilibrium_score}")