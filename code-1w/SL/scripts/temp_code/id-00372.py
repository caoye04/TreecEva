def rotate_left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

# Irrelevant helper function for distraction
def mirror_bits(val):
    result = 0
    for _ in range(32):
        result = (result << 1) | (val & 1)
        val >>= 1
    return result

# Simulate data preprocessing with distractors
data_stream = [17, 25, 33, 41, 50, 59]
offset_map = {i: val % 8 for i, val in enumerate(data_stream)}
scrambled = []
for idx, val in enumerate(data_stream):
    if idx % 2 == 0:
        scrambled.append(val ^ (idx * 3))
    else:
        scrambled.append(val + idx)

# Unused but misleading transformation
decay_weights = [round(0.9 ** i, 4) for i in range(len(data_stream))]
total_weighted = sum(w * v for w, v in zip(decay_weights, data_stream))

# Key schedule generation - relevant part
def generate_key_schedule(seed_seq):
    schedule = []
    state = seed_seq[0] % 31
    for i in range(10):
        state = (state * 17 + 257) % 1024
        if i in [2, 5, 7]:
            schedule.append(state | 0x100)
        else:
            schedule.append(state)
    return schedule

key_schedule = generate_key_schedule(scrambled)

# Real processing begins here
temp_buffer = 0
for val in reversed(scrambled[:4]):
    temp_buffer ^= (val * 13)

temp_buffer = rotate_left(temp_buffer, 5)

# Auxiliary checksum (distractor)
current_crc = 0
for byte in data_stream:
    current_crc ^= byte
    for _ in range(8):
        if current_crc & 1:
            current_crc = (current_crc >> 1) ^ 0xEDB88320
        else:
            current_crc >>= 1

# Another red herring: unused recursive function
def compute_depth(n):
    if n <= 1:
        return 1
    return compute_depth(n-1) + compute_depth(n-2)

# Actual computation of interest
def process_segment(buf, keys):
    intermediate = buf
    for i, k in enumerate(keys):
        if i % 3 == 0:
            intermediate = (intermediate + k) & 0xFFFFFFFF
        elif i % 3 == 1:
            intermediate = (intermediate ^ k) & 0xFFFFFFFF
        else:
            intermediate = rotate_left(intermediate, k % 7)
    return intermediate % 10000

final_checksum = process_segment(temp_buffer, key_schedule)
print(f"Result: {final_checksum}")