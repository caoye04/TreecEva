def analyze_pattern(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

# Irrelevant helper function (dead code path)
def deprecated_calibrate(x):
    temp = 0
    for i in range(len(x)):
        temp += x[i] * (i % 3)
    return temp

# Unused transformation matrix
turbulence_matrix = [[1, -1, 0], [0, 1, -1], [-1, 0, 1]]

# Distractor variables
dummy_weights = [0.1, 0.3, 0.5, 0.7]
scaling_factor = 2.718
correction_offset = -999  # Never used

# Real data inputs
base_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
index_map = {i: val for i, val in enumerate([2, 0, 1, 3, 7, 4, 5, 6])}

# Misleading intermediate calculation (not part of final result)
shadow_accumulator = 0
for idx, value in enumerate(base_sequence):
    if idx % 2 == 0:
        shadow_accumulator += value ** 2
    else:
        shadow_accumulator -= value

# Primary signal processing chain
signal_chain = []
for i, j in zip(index_map.values(), base_sequence):
    computed = (i + j) * (i % 3 + 1)
    if computed > 10:
        signal_chain.append(computed // 2)
    elif computed > 5:
        signal_chain.append(computed + 1)
    else:
        signal_chain.append(computed * 3)

# Encryption key with red herring derivation
key_seed = 0
for x in base_sequence:
    if x in index_map:
        key_seed += index_map[x] % 4
    else:
        key_seed += x % 2
encryption_key = (key_seed ^ 17) & 15  # Final key derived via bit manipulation

# Decoy state tracking
current_state = [0] * 8
temp_buffer = []
for k in range(4):
    temp_buffer.append((k * encryption_key) % 7)

# Core logic: actual computation path
shift_register = [0, 0, 0]
running_sum = 0

for val in signal_chain:
    shift_register.append(val)
    shift_register.pop(0)
    
    # Complex conditional update
    if shift_register[2] > shift_register[1] and shift_register[1] < shift_register[0]:
        running_sum += shift_register[2] - shift_register[1]
    elif shift_register[2] < shift_register[0]:
        running_sum += shift_register[2] ^ encryption_key
    else:
        running_sum += shift_register[1] // (shift_register[0] % 5 + 1)

    if running_sum > 100:  # Early break red herring
        break

# Actual target processing function
def process_transmission(chain, key):
    result = 0
    for pos, item in enumerate(chain):
        if pos % 2 == 0:
            result += item * (key + pos) % 13
        else:
            result -= (item ^ key) % 7
    
    # Additional transformation layer
    final_shift = 0
    for bit_pos in range(4):
        if (key >> bit_pos) & 1:
            final_shift += (result >> bit_pos) & 1
    
    result = (result + final_shift * 8) % 1000
    
    # One more obfuscation step
    if result % 2 == 0:
        result = (result * 7) % 229
    else:
        result = (result * 11) % 197
    
    return result

# Critical execution point
final_signal = process_transmission(signal_chain, encryption_key)

# Output result as required
print(f"Result: {final_signal}")