import math

def analyze_phase_shift(freq, amplitude):
    # Irrelevant signal processing helper
    return (amplitude * math.sin(freq)) ** 2

def generate_constraints(base_val):
    # Distractor: generates unused constraint list
    constraints = []
    for i in range(5):
        constraints.append((base_val + i) % 7)
    return constraints

def evaluate_stability(x, y):
    # Dead logic path — never called
    if x < 0 or y > 100:
        return False
    return (x * y) % 3 == 0

# Global tracking state (partially relevant)
counter_state = [0, 0, 0]

threshold_func = lambda x: x > 0.75

# Misleading intermediate computations
temp_offset = 0
for i in range(3):
    temp_offset += (i + 1) * 0.1
    counter_state[i] = int(temp_offset * 10)

# Unused complex structure
constraint_matrix = [
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# Relevant data disguised among distractors
sensor_readings = [0.6, 0.8, 0.72, 0.91, 0.68]
diagnostic_flags = []

for val in sensor_readings:
    # Apply threshold function (relevant)
    diagnostic_flags.append(threshold_func(val))

# Secondary filtering with lambda (relevant)
active_alarms = list(filter(lambda x: x, diagnostic_flags))

# Bitwise integration of alarm state (key step)
flag_sum = 0
for i, flag in enumerate(diagnostic_flags):
    if flag:
        flag_sum |= (1 << i)

# Simulated system scan function
def system_scan(matrix, thresh):
    # Heavily distracted function body
    local_accum = 0
    
    # Useless traversal of matrix
    total_elements = 0
    zero_count = 0
    for row in matrix:
        for elem in row:
            total_elements += 1
            if elem == 0:
                zero_count += 1
    
    # Red herring computation
    spurious_score = (total_elements - zero_count) * 0.33
    
    # Actual relevant logic: count True values in diagnostic_flags from outer scope
    trigger_count = sum(1 for x in diagnostic_flags if x)
    
    # Combine with bit pattern (still not used)
    pattern_weight = bin(flag_sum).count('1')
    
    # Core calculation: arithmetic combo of trigger count and offset
    base_diagnostic = trigger_count * 17
    
    # Additional factor: number of readings above 0.7 (excluding first)
    secondary_filter = len([v for v in sensor_readings[1:] if v > 0.7])
    
    # Final result derived from two key metrics
    result = base_diagnostic + secondary_filter - 2
    
    # Dead assignment
    final_adjustment = math.log(result) if result > 0 else 0
    
    return int(result)

# Key execution point
final_diagnostic = system_scan(constraint_matrix, threshold_func)

# Output required format
print(f"Result: {final_diagnostic}")