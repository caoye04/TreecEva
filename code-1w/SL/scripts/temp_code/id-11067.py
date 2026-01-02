import math

def analyze_pattern(x):
    # Irrelevant helper with misleading calculations
    temp = 0
    for i in range(3):
        temp += (x + i) ** 2 - i
    return temp // 2

# Distractor variables and dead computations
counter_log = [0] * 15
tracking_mask = 0b101010
useless_sum = sum([i**2 for i in range(10)])

# Real data path begins here
data_chunk = [n for n in range(-7, 18) if n % 3 != 0]
processed_flags = []

# Complex transformation with slicing and filtering
for idx in range(len(data_chunk)):
    val = data_chunk[idx]
    if val < 0:
        processed_flags.append(abs(val) % 4 == 2)
    elif val > 10:
        processed_flags.append((val % 5) in [1, 3])
    else:
        processed_flags.append(False)

# Misleading intermediate: looks important but unused later
aggregate_score = sum([i for i, flag in enumerate(processed_flags) if flag]) * 2.5

# Core logic hidden among noise
shifted_view = data_chunk[4:-3]  # Slicing: relevant
filtered_view = [x for x in shifted_view if x > 0 and x % 2 == 1]  # odd positives

# Decoy function call that does nothing to final result
def update_buffer(buf, key):
    if key < 0:
        return buf[::-1]
    return buf[::2]

buffer_state = update_buffer(filtered_view, -1)  # Dead end

# Real accumulation starts here
running_total = 0
for num in filtered_view:
    if num in {3, 7, 13}:
        running_total += int(math.log(num, 2)) if num > 1 else 0
    else:
        running_total += num // 3

# Another red herring: complex bit manipulation but unused
bit_accum = 0
for i in range(5):
    bit_accum ^= (tracking_mask << i) & 0xFF
    bit_accum &= ~(1 << (i % 8))

# Conditional override simulation (not triggered)
threshold_limit = 42
if running_total > threshold_limit:
    final_correction = -1
else:
    final_correction = 1  # Always taken, but obscured

# Key computation
base_reference = sum(shifted_view[:len(filtered_view)])
adjustment_factor = len(processed_flags) - len(filtered_view)

intermediate_result = base_reference * 0.75 + running_total

# Final processing function
def process_sequence(seq):
    cumulative = 0
    for i, v in enumerate(seq):
        if i % 2 == 0:
            cumulative += v * (i + 1)
        else:
            cumulative -= v // (i + 1) if i > 0 else 0
    return int(cumulative * 0.9) + final_correction

# Execution point of interest
final_output = process_sequence(data_chunk)

# Output required format
print(f"Target result: {final_output}")