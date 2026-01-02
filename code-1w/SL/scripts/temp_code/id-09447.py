import math

# Irrelevant helper function (dead code path)
def decrypt_payload(data):
    return [x ^ 7 for x in data]

# Misleading transformation table (partially unused)
transform_map = {i: (i ** 2) % 19 for i in range(30)}

# Unused but plausible-looking cryptographic constants
crypto_seeds = [1103515245, 12345, 69069, 1729]

# Real signal sequence with embedded logic
sequence = [1, 0, 1, 1, 0, 1, 0, 0, 1]

# Distractor: complex-looking but unused bit manipulation
extended_mask = sum([(1 << (i + 1)) ^ (i % 5) for i in range(12)])

# Key schedule with red herring elements
key_schedule = []
for i in range(8):
    val = (i * i + 3 * i + 7) % 16
    if val % 2 == 0:
        key_schedule.append(val + 4)
    else:
        key_schedule.append(val)

# Unused recursive decoy function
def calculate_entropy(data, depth=0):
    if depth > 3 or not data:
        return 0
    mid = len(data) // 2
    return calculate_entropy(data[:mid], depth+1) + (data[mid] if mid < len(data) else 0)

# Real processing begins here
shift_registry = [(k * 2 + 1) % 7 for k in key_schedule[:6]]

# Complex list comprehension with filtering and transformation
filtered_sequence = [
    (idx + 1) * bit 
    for idx, bit in enumerate(sequence) 
    if (idx + 1) % 3 != 0 or bit == 1
]

# Decoy statistical summary (never used)
stat_summary = {
    'mean': sum(filtered_sequence) / len(filtered_sequence),
    'peak': max(filtered_sequence),
    'variance': sum((x - sum(filtered_sequence)/len(filtered_sequence))**2 for x in filtered_sequence) / len(filtered_sequence)
}

# Core logic disguised among distractions
integrated_weight = 0
for i, weight in enumerate(shift_registry):
    if i < len(filtered_sequence):
        # Apply non-linear transformation using trigonometric distraction
        angle = math.pi * weight / 4
        factor = int(math.cos(angle) * 8) or 1
        integrated_weight += filtered_sequence[i] * factor

# Lambda-based conditional resolver (used once)
resolve_offset = lambda x: x if x > 0 else (abs(x) + 2)

# Final processing with tuple unpacking and destructuring
temp_result = resolve_offset(integrated_weight)
interim = temp_result ^ 255  # Bitwise red herring

# Critical statement
final_signal = (interim + sum(key_schedule[::2])) % 10000

# Additional misleading operation (no effect on final_signal)
redundant_check = any(
    (final_signal % prime) == 0 
    for prime in [101, 103, 107, 109, 113] 
    if prime > final_signal / 2
)

print(f"Result: {final_signal}")