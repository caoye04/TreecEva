import math

# Irrelevant utility function (dead code)
def unused_helper(x):
    return x ** 3 + 2 * x

def transform_value(n):
    # Complex transformation with red herring logic
    temp_a = n % 7
    temp_b = (n + 5) // 3
    temp_c = temp_a * temp_b
    if temp_c > 20:
        temp_c = temp_c // 2
    return temp_c

def evaluate_condition(x, y):
    # Logical operation with distractor variables
    threshold = 4.5
    score = x / (y + 1)
    offset = 10  # Unused in final logic
    adjustment = 0.8  # Misleading constant
    return score >= threshold and (x & y) != 0

data_chunk = [14, 23, 9, 31, 18]

# Distractor: irrelevant list processing
temp_results = []
for val in data_chunk:
    transformed = transform_value(val)
    temp_results.append(transformed * 1.5)

# Key computation path begins here
aggregated = 0
for i in range(len(data_chunk)):
    if data_chunk[i] % 2 == 0:
        aggregated += data_chunk[i]
    else:
        aggregated -= data_chunk[i]

# Secondary transformation with tuple unpacking and conditional expression
meta_flag = len(data_chunk) > 4
intermediate_tuple = (aggregated, meta_flag)
value_base, flag_state = intermediate_tuple

scaled_value = value_base * 3 if flag_state else value_base * 2

# Bit manipulation red herring
bit_fiddle = scaled_value ^ 0xFF
shifted_mask = bit_fiddle << 1
ignored_result = shifted_mask & 0xFFFF

# Conditional logic with min/max and rounding
reference_values = [abs(scaled_value), 56, 73]
selected_ref = min(reference_values)
adjusted_scale = round(selected_ref / 3.14159, 2)

# Decoy loop with no effect on output
running_total = 0
for _ in range(3):
    for j in range(5):
        running_total += j * 2
        if running_total > 100:
            break

# Final pipeline function combining multiple concepts
def process_pipeline(data):
    total_sum = sum(data)
    avg_val = total_sum / len(data)
    deviation = abs(avg_val - data[0])
    rounded_dev = int(deviation)
    
    # Logical operations and integer division
    parity_check = (len(data) % 2 == 1) or (total_sum % 3 == 0)
    multiplier = 4 if parity_check else 6
    
    # Core calculation hidden among distractions
    core_signal = (rounded_dev * multiplier) + (data[-1] // 5)
    
    # Use of conditional expression (required Python feature)
    noise_factor = 10 if core_signal < 50 else 0
    
    # Final result derived from non-obvious chain
    result = core_signal - noise_factor
    
    # Multiple assignments (distractor)
    temp_x, temp_y = result + 5, result - 5
    temp_x, temp_y = temp_y, temp_x  # Swapping for no reason
    
    return result

# Execution point of interest
final_output = process_pipeline(data_chunk)

print(f"Target result: {final_output}")