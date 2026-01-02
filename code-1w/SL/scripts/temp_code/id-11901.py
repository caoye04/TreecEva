def analyze_conditions(x, y, z):
    temp_a = (x + y) % 7
    temp_b = (y * 2) ^ z
    flag_check = (temp_a > 3) and (temp_b < 10)
    return flag_check


def process_sequence(values):
    accumulator = 0
    shift_factor = 3
    for val in values:
        if val % 2 == 0:
            accumulator += val >> shift_factor
        else:
            accumulator -= val & 5
    return accumulator


def calculate_final_score(raw_data):
    # Core computation path
    base_sum = sum(raw_data)
    filtered = [x for x in raw_data if x % 3 == 0]
    adjustment = len(filtered) * 4
    
    # Distractor: irrelevant transformation
    transformed = [((x << 2) ^ 7) % 100 for x in raw_data]
    dummy_total = sum(transformed) // 10  # Not used later
    
    # Conditional expression usage
    modifier = 10 if any(analyze_conditions(x, x+1, x*2) for x in filtered) else -5
    
    # Additional distraction: dead logic with unused variables
    peak = max(raw_data) if raw_data else 0
    shadow_copy = raw_data.copy()
    shadow_copy.reverse()
    median_twin = (shadow_copy[1] + shadow_copy[2]) // 2  # Computed but not used
    
    # Main calculation chain
    intermediate = base_sum + adjustment
    if intermediate % 2 == 0:
        intermediate = process_sequence([intermediate, adjustment, 12])
    else:
        intermediate *= 2
    
    final_score = intermediate + modifier
    
    # Irrelevant loop with side-effect-free operations
    checksum = 0
    for i in range(3):
        checksum ^= (peak + i) & 15
    
    return final_score

# Input data
input_data = [9, 6, 15, 4, 21, 8]

# Execution point
final_score = calculate_final_score(input_data)
print(f"Result: {final_score}")