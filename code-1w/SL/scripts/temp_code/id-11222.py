import math

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(d ^ 7 for d in data) % 13

# Decoy transformation with misleading intermediate results
def decoy_transform(sequence):
    shifted = [(x << 2) & 255 for x in sequence]
    inverted = [255 - s for s in shifted]
    return [inv ^ 170 for inv in inverted]  # Never actually used

# Real transformation: applies bit reversal and offsets
def reverse_bits(n, width=8):
    return int(bin(n)[2:].zfill(width)[::-1], 2)

def transform_input(raw):
    bit_reversed = [reverse_bits(x) for x in raw]
    offset_applied = [(b + 13) % 256 for b in bit_reversed]
    return [o * 2 if o % 2 == 0 else o // 3 for o in offset_applied]

# Conditional logic with red herring branches
threshold = 42

# Simulated sensor readings (distractor data)
sensor_a = [17, 89, 121, 205]
sensor_b = [63, 142, 191, 244]
sensor_c = [11, 37, 73, 109]

# Unused but plausible-looking fusion logic
fusion_mode = 'adaptive'

if fusion_mode == 'average':
    fused = [sum(vals)/3 for vals in zip(sensor_a, sensor_b, sensor_c)]
elif fusion_mode == 'median':
    fused = sorted([sensor_a[i], sensor_b[i], sensor_c[i]])[1] for i in range(4)
else:
    fused = [a ^ b ^ c for a, b, c in zip(sensor_a, sensor_b, sensor_c)]  # Looks important, unused

# Core data pipeline
raw_signal = [16, 32, 48, 64]

# Bit manipulation mixed with arithmetic
processed = []
for val in raw_signal:
    temp = val ^ 255                           # bitwise XOR
    temp = (temp + 17) % 256                    # modular arithmetic
    temp = temp >> 1                            # right shift
    if temp > 100:
        temp = int(math.sqrt(temp))            # conditional math
    processed.append(temp)

# Apply real transformation
transformed_data = transform_input(processed)

# Set operation to filter anomalous values
allowed_range = set(range(10, 150))
anomalies = {x for x in transformed_data if x not in allowed_range}
cleaned_data = [x for x in transformed_data if x in allowed_range]

# Lambda-based dynamic weight assignment (only some weights matter)
weights = list(map(lambda x: (x % 7) + 1, cleaned_data))
weighted_values = [a * b for a, b in zip(cleaned_data, weights)]

# Recursive reduction function (simple but distracts from core flow)
def recursive_reduce(arr, acc=0):
    if not arr:
        return acc
    return recursive_reduce(arr[1:], acc ^ (arr[0] & 63))

# Spurious recursive call on decoy data
_ = recursive_reduce(sensor_a)
_ = recursive_reduce(sensor_b)

# Actual relevant recursion
reduction_key = recursive_reduce(weighted_values)

# Final analysis using conditional expression and set intersection
baseline_profile = {22, 45, 67, 88, 103}
observed_set = set(cleaned_data)
match_count = len(observed_set.intersection(baseline_profile))

def analyze_pattern(data):
    base_score = sum(data) // len(data) if data else 0
    bonus = 25 if match_count >= 2 else 0
    penalty = 10 if any(x < 0 for x in data) else 0
    # Key logic hidden in conditional expression
    adjustment = 50 if reduction_key in {12, 15, 19, 23} else -30
    return base_score + bonus - penalty + adjustment

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")