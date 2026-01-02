def filter_valid_entries(data_log):
    # Irrelevant filtering based on decoy criteria
    anomalies = [x for x in data_log if x < 0]
    temp_scale = 2.5
    scaled = [int(x * temp_scale) for x in data_log if x > 10]  # Distractor transformation
    
    # Actual relevant logic buried here
    valid = [x for x in data_log if 15 <= (x % 100) < 40 and x % 3 == 0]
    return valid

# Decoy function that looks important but is unused
def analyze_pattern(seq):
    return sum([seq[i] ^ seq[-i-1] for i in range(len(seq)//2)])

# Another red herring: complex bit manipulation with no impact
flag_mask = 0b1101
status_flags = [flag_mask << i for i in range(5)]
active_states = list(map(lambda x: x & 0xFF, status_flags))

# Dummy accumulation with misleading naming
rolling_total = 0
for value in [12, 18, 24, 36]:
    rolling_total += value * 2 - 5  # Looks like it matters

# Real data input
log_data = [23, 30, 33, 15, 45, 18, 99, 102, 39, 111, 120, 123]

# Obfuscated summation via higher-order function
sum = lambda lst: lst[0] if len(lst) == 1 else lst[0] + sum(lst[1:]) if lst else 0

# Conditional expression with mixed relevance
threshold_met = True if sum([1 for x in log_data if x > 100]) >= 3 else False

# Nested control flow with distractors
if threshold_met:
    adjustment = -5
    secondary = [x for x in log_data if x % 5 == 0]
    secondary_sum = sum(secondary)  # Dead-end computation
else:
    adjustment = 10

# Core logic hidden in layered calls
baseline = sum(filter_valid_entries(log_data))
offset = (lambda: 7 if baseline > 50 else 3)()  # Conditional expression

def finalize(value):
    # Bit manipulation decoy
    bits = bin(value)[2:]
    parity = sum(int(b) for b in bits) % 2
    
    # Multiple irrelevant operations
    expanded = [value + i for i in range(parity + 1)]
    trimmed = expanded[:len(expanded)//2 + 1]
    
    # Actual finalization step
    result = value + offset + adjustment
    return result * 2  # Key transformation

# Critical execution point
checksum = finalize(sum(filter_valid_entries(log_data)))

# Output requirement
print(f"Result: {checksum}")