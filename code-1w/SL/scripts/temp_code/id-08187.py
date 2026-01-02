import math

# Simulated sensor data preprocessing with diagnostic flags
def collect_sensor_readings():
    raw_values = [127, 255, 192, 64, 31, 88, 143]
    base_offset = 32
    adjusted = [v - base_offset for v in raw_values]
    filtered = [x for x in adjusted if x > 0]
    return filtered

# Irrelevant helper - dead code path (not used)
def legacy_compatibility_mode(data):
    return [d ^ 0xFF for d in data]

# Data transformation with bit manipulation and conditional logic
def transform_signal(x):
    if x & 1:
        return ((x << 2) ^ 0x0F) & 0xFF
    else:
        return (x >> 1) + 10

# Another red herring: checksum that's never called
def validate_integrity(chunk):
    checksum = 0
    for b in chunk:
        checksum = (checksum + b) % 256
    return checksum == 0

# Core processing function with mixed arithmetic and logic
def process_metrics(data, limit):
    temp_results = []
    scaling_factor = 1.75
    
    for val in data:
        # Complex nested condition with distractor variables
        is_power_of_two = (val & (val - 1)) == 0 and val != 0
        magnitude = int(math.log(val, 2)) if val > 1 else 0
        
        # Conditional expression (required python feature)
        adjusted_val = val * scaling_factor if is_power_of_two else (val ** 1.5) // 1
        
        # Bitwise mix and irrelevant rounding
        masked = int(adjusted_val) & 0x7F
        rounded_val = round(masked + 0.49, 0)
        
        # Only append if above dynamic threshold
        if val % 3 != 0:
            temp_results.append(int(rounded_val))
    
    # Secondary filtering and aggregation
    final_sum = sum([t for t in temp_results if t < limit])
    correction = len(temp_results) - len([t for t in temp_results if t > 50])
    
    # Key result computation
    return final_sum - (correction * 3)

# Unused recursive distraction
def recursive_distractor(n):
    if n <= 1:
        return 1
    return recursive_distractor(n-1) + recursive_distractor(n-2)

# Main execution flow
sensor_data = collect_sensor_readings()

# Transform each value using bitwise and shift logic
transformed_data = [transform_signal(x) for x in sensor_data]

# Spurious sorting with no impact (distractor)
sorted_unused = sorted(transformed_data, reverse=True)

# Dummy case conversion on numbers (meaningless but plausible)
case_shifted = [str(d).lower() for d in transformed_data]
converted_back = [int(c) for c in case_shifted]  # No change

# Actual threshold logic
threshold = 70

# Critical statement containing answer
final_diagnostic = process_metrics(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")