import itertools

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x % 3 == 0)

# Another decoy: complex-looking but unused transformation
class ObfuscationLayer:
    def __init__(self, level):
        self.level = level
        self.mask = (level * 7) ^ 0xAA

    def scramble(self, val):
        return (val ^ self.mask) >> 2

# Misleading intermediate computation with no impact
temp_diagnostic = [i * i - 2*i for i in range(15) if i % 4 != 0]
shadow_buffer = list(itertools.accumulate(temp_diagnostic, lambda a, b: a + (b % 5)))

# Real logic begins: signal processing simulation
flow_sequence = [18, 22, 19, 25, 30, 28, 20, 17]
baseline = 20
threshold = 24

# Decoy filter that looks important but isn't used in final logic
high_pass_filtered = [x for x in flow_sequence if x > baseline]

# Actual transformation pipeline
mask_pattern = [1 if x >= threshold else 0 for x in flow_sequence]
shifted_signal = [(x << 1) & 0x3F for x in flow_sequence]  # Bit manipulation: left shift and mask

# Key interference: multiple counting operations, only one matters
event_count = 0
spike_magnitude = 0
control_flag = True

for i, val in enumerate(flow_sequence):
    if val > threshold:
        event_count += 1
        spike_magnitude += val
        control_flag = not control_flag  # Red herring toggle

# Distractor: another accumulation with bitwise twist (unused)
bit_accum = 0
for x in shifted_signal:
    bit_accum ^= (x + 5) & 0xF

# Critical data transformation: uses slicing, filtering, and reduction
def transform_data(data, limit):
    upper_segment = data[2:]  # Slicing: ignore first two readings
    filtered = [x for x in upper_segment if x >= limit]
    
    # Apply XOR folding with prime offset
    if not filtered:
        return 0
    result = filtered[0]
    for j in range(1, len(filtered)):
        result ^= (filtered[j] + 11)  # XOR with offset
    
    # Additional transformation: fold in length via multiplication
    result *= len(filtered)
    
    # Decoy operation: looks like correction but doesn't affect anything
    if result > 100:
        result -= (result // 10) % 9  # Misleading adjustment
    
    return result

# Unused recursive red herring
def recursive_probe(n, depth=0):
    if depth >= 3 or n < 5:
        return n
    return recursive_probe(n // 2, depth + 1) + (n % 2)

# Trigger the real computation
current_state = {"mode": "active", "version": 0x1B}

# Key statement: this is where 'checksum' gets its value
checksum = transform_data(flow_sequence, threshold)

# Print required output
print(f"Result: {checksum}")