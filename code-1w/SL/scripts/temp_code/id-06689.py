def preprocess_signal(raw_data):
    # Irrelevant signal scaling (distractor)
    scaled = [x * 0.01 for x in raw_data]
    normalized = [x / max(scaled) for x in scaled]
    return [int(x * 100) for x in normalized]

# Decoy function – never called
def legacy_calculate_checksum(seq):
    return sum(seq[i] * (i + 1) for i in range(len(seq))) % 256

# Unused transformation matrix (red herring)
transformation_matrix = [
    [1, -1, 0],
    [0, 1, -1],
    [-1, 0, 1]
]

# Simulate sensor data acquisition
raw_sensor_data = [123, 456, 789, 234, 567]
filtered = preprocess_signal(raw_sensor_data)

# Misleading intermediate: looks important but unused later
checksum_diagnosis = sum(filtered) % 100

# Critical data transformation chain
encoded = ''.join([chr(97 + (x % 26)) for x in filtered])  # Map to a-z

# Slicing operation: extract non-contiguous pattern
fragment = encoded[::3] + encoded[1::4]  # Combine two slices – distractor complexity

# Another decoy variable with plausible name
stability_index = len(fragment) / (filtered[0] / 10) if filtered[0] != 0 else 0

# Real processing begins here — deeply nested logic
shift_key = len(encoded) % 5 + 3
rotated = ''
for char in fragment:
    rotated += chr((ord(char) - 97 + shift_key) % 26 + 97)

# Linear search through character frequencies
freq_map = {}
for c in rotated:
    freq_map[c] = freq_map.get(c, 0) + 1

# Extract values and manipulate strings
sorted_chars = sorted(freq_map.keys(), key=lambda x: (-freq_map[x], x))

# String method distraction
concat_result = ''.join(sorted_chars).upper().replace('X', 'Z').lstrip('A')

# Core algorithm hidden among distractions
numeric_sequence = [ord(c) - 96 for c in sorted_chars]  # a=1, b=2, etc.

# Bit manipulation red herring
bitmask = 0
for val in numeric_sequence:
    bitmask ^= (val << 2) | (val >> 1)

# Actual key computation buried deep
def analyze_pattern(seq):
    temp = 0
    for i, v in enumerate(seq):
        if i % 2 == 0:
            temp += v * (i + 1)
        else:
            temp -= v
    # Final twist: use string length from earlier slice
    adjustment = len(fragment) // 4
    return temp + adjustment

# Critical assignment point
final_diagnostic = analyze_pattern(numeric_sequence)

# Output result as required
print(f"Result: {final_diagnostic}")