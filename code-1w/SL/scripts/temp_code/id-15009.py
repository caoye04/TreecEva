def normalize_values(data_list):
    # Irrelevant normalization function (dead code path)
    return [x / sum(data_list) for x in data_list]


def decrypt_key(key_str):
    # Distractor: looks important but unused
    return sum(ord(c) for c in key_str) % 7

# Unused constants (red herring)
MAX_THRESHOLD = 850
BASE_OFFSET = 23
TEMP_FACTOR = 1.05

# Simulated sensor data segments (mixed relevance)
segment_data = [
    [12, 15, 14, 13, 16],
    [21, 19, 20, 22, 18],
    [8, 9, 11, 10, 12],
    [33, 31, 34, 30, 32]
]

# Weights with misleading naming (some are ignored)
weights = {
    'w_a': 0.2,
    'w_b': 0.3,
    'w_c': 0.1,  # This weight is not used
    'w_x': 0.4   # Actually used in calculation
}

# Decoy transformation matrix (never called)
mapping_grid = [[i * j for j in range(5)] for i in range(5)]

# Auxiliary function that appears useful but is irrelevant
def generate_lookup():
    return {i: chr(65 + (i % 26)) for i in range(20)}

# Real processing begins here
status_flags = [True, False, True]

for idx, segment in enumerate(segment_data):
    if idx % 2 == 0:
        # Apply transformation only to even-indexed segments
        adjusted = []
        for val in segment:
            if val > 10:
                adjusted.append(val * 1.1)
            else:
                adjusted.append(val * 0.9)
        segment_data[idx] = adjusted

# Another decoy structure
class DataBuffer:
    def __init__(self):
        self.buffer = []
        self.size_limit = 100

    def add(self, x):
        pass  # Never instantiated or used

# Core processing function
def process_segments(segments, config):
    cumulative = 0
    factor = config['w_a'] + config['w_b'] + config['w_x']  # w_c excluded intentionally

    for i, s in enumerate(segments):
        total = sum(s)
        if i == 0:
            total = round(total * 0.85)
        elif i == 1:
            total = int(total * 1.05)
        elif i == 3:
            # Special case: use zip and enumerate together
            offsets = [1, -1, 2, -2, 0]
            corrected = []
            for j, (val, off) in enumerate(zip(s, offsets)):
                corrected.append(val + off)
            total = sum(corrected)

        # Accumulate with conditional scaling
        if i % 2 == 0:
            cumulative += total * factor
        else:
            cumulative += total * 0.9

    # Final adjustment using string logic red herring
    tag = 'CALIBRATE'
    shift = len(tag.lower()) - len(tag.upper()) + 1  # Always 1, but looks tricky
    cumulative = int(cumulative >> shift)  # Bit shift by 1

    return cumulative

# Misleading pre-computation (unused)
baseline = 0
for row in segment_data:
    baseline += sum(r // 2 for r in row if r > 15)

# Actual execution path
final_score = process_segments(segment_data, weights)

# Output result as required
print(f"Target result: {final_score}")