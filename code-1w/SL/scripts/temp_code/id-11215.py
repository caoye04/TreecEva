import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw = [127, 255, 192, 64, 31, 88]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw]
    return adjusted

# Irrelevant function - dead code path (distractor)
def deprecated_filter(data):
    return [x for x in data if x > 100]

# Data transformation with conditional expressions and string methods
def transform_signal(readings):
    readings_str = [str(int(x)) for x in readings]
    padded = [r.zfill(4) for r in readings_str]  # string method usage
    inverted = [int(r[::-1]) for r in padded]  # reverse digits
    normalized = [n / 100.0 for n in inverted]
    return normalized

# Core logic: pattern analysis using bit manipulation and combinatorics
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def generate_combinations(items):
    # Simple combinatorics: count all unique pairs
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            count += 1
    return count

# Misleading diagnostic function (decoy)
def legacy_diagnostic(x):
    temp = 0
    for i in range(10):
        temp += (x * i) % 7
    return temp // 2

# Real processing path obscured by noise
threshold_reference = 4.3
activation_map = {i: i ** 2 for i in range(10)}

# Conditional branches and logical operations
def analyze_pattern(data):
    primary_sum = sum(data[:3])
    secondary_sum = sum(data[3:])
    
    # Logical operations and comparisons
    is_critical = primary_sum > threshold_reference and secondary_sum < 150.0
    is_balanced = abs(primary_sum - secondary_sum) < 40.5
    
    # Bit manipulation on derived integer
    control_flag = int(primary_sum) ^ int(secondary_sum)
    parity_check = count_set_bits(control_flag)
    
    # Conditional expression (ternary-like)
    mode_select = 'A' if is_critical else ('B' if is_balanced else 'C')
    
    # Linear search through activation map
    trigger_value = None
    for k in activation_map:
        if activation_map[k] > primary_sum:
            trigger_value = k
            break
    
    # Dummy usage of string method to mislead
    mode_log = f"Mode: {mode_select}".upper()
    
    # Key calculation: combinatorics on filtered subset
    valid_indices = [i for i, x in enumerate(data) if x > 40.0]
    combination_count = generate_combinations(valid_indices)
    
    # Final diagnostic depends on multiple hidden steps
    base_score = combination_count * 1000
    adjustment = parity_check * 17
    final_result = base_score - adjustment
    
    # Red herring: unused complex expression
    decoy_calc = math.log(secondary_sum + 1) * (control_flag & 0xFF)
    
    return final_result

# Unused variables (distraction)
baseline_calibration = [0.1, 0.2, 0.4]
corrupted_flag_sequence = "ERR01,WRN02,INF03"
emergency_override = False

# Main execution flow
sensor_data = collect_readings()
transformed_data = transform_signal(sensor_data)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Result: {final_diagnostic}")