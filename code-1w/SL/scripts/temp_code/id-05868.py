import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 192, 64, 32, 160, 96, 224]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant utility - distractor
def string_compression(s):
    if not s:
        return ''
    result = []
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(current + (str(count) if count > 1 else ''))
            current = char
            count = 1
    result.append(current + (str(count) if count > 1 else ''))
    return ''.join(result)

# Bit manipulation filter - relevant
def apply_mask(data, mask=0b1101):
    masked_values = []
    for val in data:
        int_val = int(val)
        masked = int_val & mask
        masked_values.append(masked)
    return masked_values

# Decoy function - never used
def deprecated_analysis(x):
    return sum([i**2 for i in range(len(x))]) if len(x) > 5 else 0

# Core transformation chain
transformed_data = []
readings = collect_readings()

# Apply nonlinear transformation
for r in readings:
    transformed = math.log(r + 1) ** 2
    transformed_data.append(int(transformed))

# Add decoy list
auxiliary_cache = [x ^ 255 for x in readings]  # unused path

# Use lambda for filtering - relevant
valid_check = lambda x: x > 4
filtered_data = list(filter(valid_check, transformed_data))

# Set operation to remove duplicates - relevant
unique_data = list(set(filtered_data))

# Dummy recursive countdown - irrelevant
def countdown(n):
    return 1 if n <= 0 else n - countdown(n - 1)
countdown(10)

# Tuple-based state tracking - relevant
status_flags = (True, False, True)
enabled_modes = {flag for flag in status_flags}

# Another red herring: string processing on numbers
strange_op = string_compression(''.join([str(int(math.sqrt(x))) for x in transformed_data[:3]]))

# Bitwise analysis core
masked_result = apply_mask(unique_data, mask=0b1111)

# Real computation path starts here
rolling_sum = 0
for idx, val in enumerate(masked_result):
    rolling_sum += val * (idx + 1)

# Conditional mutation
if len(unique_data) > 3 and status_flags[2]:
    rolling_sum += 17

# Final diagnostic via recursion - relevant
def analyze_pattern(seq):
    if not seq:
        return 0
    if len(seq) == 1:
        return seq[0] & 0b111  # last 3 bits
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]
    return (analyze_pattern(left) ^ analyze_pattern(right)) + len(right)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Dead code branch - misleading
if rolling_sum < 0:
    final_diagnostic *= -1
elif rolling_sum == 42:
    final_diagnostic = 999

# Output result
print(f"Result: {final_diagnostic}")